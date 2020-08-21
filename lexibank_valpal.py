import pathlib
import sqlite3
import itertools
import contextlib
import collections

from pycldf.sources import Source
import attr

import pylexibank
from pylexibank import Concept, Lexeme, Language


@attr.s
class CustomConcept(Concept):
    typical_context = attr.ib(default=None)
    role_frame = attr.ib(default=None)
    meaning_list = attr.ib(default=None)
    label_for_url = attr.ib(default=None)


@attr.s
class CustomLexeme(Lexeme):
    verb_type = attr.ib(default=None)
    original_script = attr.ib(default=None)
    simplex_or_complex = attr.ib(default=None)


@attr.s
class CustomLanguage(Language):
    contributors = attr.ib(default=None)
    continent = attr.ib(default=None)
    Comment = attr.ib(default=None)


class Dataset(pylexibank.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "valpal"
    lexeme_class = CustomLexeme
    concept_class = CustomConcept
    language_class = CustomLanguage

    # define the way in which forms should be handled
    form_spec = pylexibank.FormSpec(
        brackets={"(": ")"},  # characters that function as brackets
        separators="/",  # characters that split forms e.g. "a, b".
        missing_data=('?', '-'),  # characters that denote missing data.
        strip_inside_brackets=True,   # do you want data removed in brackets or not?
    )

    def cmd_download(self, args):
        self.raw_dir.download_and_unpack('http://valpal.info/public/valency.sqlite.zip')

    def query(self, sql):
        with contextlib.closing(sqlite3.connect(str(self.raw_dir / 'valency.sqlite'))) as db:
            cu = db.cursor()
            cu.execute(sql)
            names = list(map(lambda x: x[0], cu.description))
            return [collections.OrderedDict(zip(names, row)) for row in cu.fetchall()]

    def cmd_makecldf(self, args):
        self.create_schema(args.writer.cldf)

        rmap = collections.defaultdict(list)
        for row in self.query('select * from "references"'):
            rmap[row['language_id']].append(row['id'])
            kw = {}
            for key, bkey in {
                'authors': 'author',
                'year': 'year',
                'article_title': 'title',
                'editors': 'editor',
                'book_title': 'booktitle',
                'city': 'address',
                'issue': 'issue',
                'journal': 'journal',
                'pages': 'pages',
                'publisher': 'publisher',
                'series_title': 'series',
                'url': 'url',
                'volume': 'volume',
                'additional_information': 'note',
            }.items():
                if row[key]:
                    kw[bkey] = row[key]
            args.writer.add_sources(Source(row['bibtex_type'] or 'misc', str(row['id']), **kw))
        all_sources = {
            rid
            for lang_refs in rmap.values()
            for rid in lang_refs}

        contributors = {
            r['id']: r['name'] for r in self.raw_dir.read_csv('contributors.csv', dicts=True)}
        contributions = {}
        for lid, rows in itertools.groupby(
            sorted(
                self.raw_dir.read_csv('contributions.csv', dicts=True),
                key=lambda d: (d['language_id'], int(d['sort_order_number'] or 0))),
            lambda d: d['language_id'],
        ):
            contributions[int(lid)] = ' and '.join(
                [contributors[d['person_id']] for d in rows if d['person_id'] in contributors])

        lang2gl = {l['Name']: l['Glottocode'] for l in self.languages}
        lmap = {}
        for lang in self.query('select * from languages order by name'):
            lang['glottolog_code'] = lang2gl.get(lang['name'], lang['glottolog_code'])
            lmap[lang['id']] = lang['glottolog_code']
            name = lang['name']
            if lang['variety']:
                name += ' ({0})'.format(lang['variety'])
            args.writer.add_language(
                ID=lang['glottolog_code'],
                Name=name,
                Glottocode=lang['glottolog_code'],
                ISO639P3code=lang['iso_code'],
                Latitude=lang['latitude'],
                Longitude=lang['longitude'],
                Comment=lang['comments'],
                contributors=contributions[lang['id']],
                continent=lang['continent'],
            )

        args.writer.add_concepts(
            id_factory=lambda c: c.attributes['label_for_url'].replace('/', '_'))
        cmap = {}
        for meaning in self.query("select * from meanings order by label"):
            cmap[meaning['id']] = meaning['label_for_url'].replace('/', '_')
            args.writer.add_concept(
                ID=meaning['label_for_url'].replace('/', '_'),
                Name=meaning['label'],
                typical_context=meaning['typical_context'],
            )

        fmap = {}
        forms = """\
select
    v.id, 
    v.verb_form,
    v.original_script,
    v.comment,
    v.simplex_or_complex,
    v.verb_type,
    v.language_id,
    mv.meaning_id
from 
    verbs as v, meanings_verbs as mv 
where
    v.id = mv.verb_id
order by v.language_id, mv.meaning_id;"""
        for row in self.query(forms):
            #
            # FIXME: flesh out data!
            #
            res = args.writer.add_forms_from_value(
                Value=row['verb_form'],
                Language_ID=lmap[row['language_id']],
                Parameter_ID=cmap[row['meaning_id']],
                Comment=row['comment'],
                Source=rmap[row['language_id']],
                verb_type=row['verb_type'],
                original_script=row['original_script'],
                simplex_or_complex=row['simplex_or_complex'],
                #
                # FIXME: mark singular (SG) and plural (PL)?
                #
            )
            fmap[row['id']] = [r['ID'] for r in res]

        #CREATE TABLE "examples" (
        # "id" integer(8),
        # "reference_id" integer(8),
        # "person_id" integer(8),
        # "original_orthography" text,
        # "media_file_name" varchar(255),
        # "media_file_timecode" varchar(255),
        # "reference_pages" varchar(255),
        # "number" integer);
        gloss_fix = {
            'find.out-NTR<STV>-OBJ-3.ERG DET= boy': 'find.out-NTR<STV>-OBJ-3.ERG DET=boy',
            'scream<STV> DET= PL-child': 'scream<STV> DET=PL-child',
            'boy.ERG brother.OBL-INSTR girl.OBL-LAT embrace(IV).ABS IV-fill-CAUS- PST':
            'boy.ERG brother.OBL-INSTR girl.OBL-LAT embrace(IV).ABS IV-fill-CAUS-PST',
        }
        morphemes_fix = {
            r'tande-mne brbr-äm y/ram\te': 'tande-mne brbr-äm y/ram_te',
        }
        ex2verb = {}
        for row in self.query("""\
select e.id, group_concat(ev.verb_id, ' ') as vids
from examples as e, examples_verbs as ev 
where e.id = ev.example_id group by e.id"""):
            ex2verb[row['id']] = []
            for vid in set(row['vids'].split()):
                ex2verb[row['id']].extend(fmap[int(vid)])

        maxnum = {}
        for row in self.query("select * from examples order by language_id, number desc"):
            if row['language_id'] not in maxnum:
                maxnum[row['language_id']] = row['number']
            if row['number'] == 0:
                row['number'] = maxnum[row['language_id']] = maxnum[row['language_id']] + 1
            row['gloss'] = gloss_fix.get(row['gloss'], row['gloss'])
            row['analyzed_text'] = morphemes_fix.get(row['analyzed_text'], row['analyzed_text'])
            source = None
            if row.get('reference_id') and row.get('reference_id') in all_sources:
                source = [str(row['reference_id'])]
            args.writer.objects['ExampleTable'].append(dict(
                ID='{0}-{1}'.format(lmap[row['language_id']], row['number']),
                Language_ID=lmap[row['language_id']],
                Primary_Text=row['primary_text'],
                Analyzed_Word=row['analyzed_text'].split(),
                Gloss=row['gloss'].split(),
                Translated_Text=row['translation'],
                Comment=row['comment'],
                Example_Type=row['example_type'],
                Source=source,
                Form_IDs=sorted(ex2verb.get(row['id'], [])),
            ))

        for row in self.query("select * from microroles order by meaning_id, id"):
            args.writer.objects['microroles.csv'].append(dict(
                ID=row['id'],
                Name=row['name'],
                Parameter_ID=cmap[row['meaning_id']],
                Role_Letter=row['role_letter'],
                Original_Or_New=row['original_or_new'],
                Name_For_URL=row['name_for_url'],
            ))

        for row in self.query("select * from coding_sets order by language_id, id"):
            lang_id = lmap.get(row['language_id'])
            if lang_id:
                args.writer.objects['coding-sets.csv'].append(dict(
                    ID=row['id'],
                    Name=row['name'],
                    Comment=row['comment'],
                    Language_ID=lang_id,
                ))

        arg_types = collections.defaultdict(dict)
        frame_codingsets = collections.defaultdict(dict)
        for row in self.query(
            'select coding_frame_id,index_number,argument_type,coding_set_id'
            '  from coding_frame_index_numbers join argument_types'
            '  on argument_type_id = argument_types.id'
            '  order by coding_frame_id, index_number'
        ):
            frame_codingsets[row['coding_frame_id']][row['index_number'] - 1] =\
                row['coding_set_id']
            arg_types[row['coding_frame_id']][row['index_number'] - 1] =\
                row['argument_type']

        for row in self.query('select * from coding_frames order by language_id, id'):
            arg_type_list = None
            if row['id'] in arg_types:
                arg_type_list = [
                    arg_types[row['id']].get(i) or ''
                    for i in range(max(arg_types[row['id']]))]
            coding_set_list = None
            if row['id'] in frame_codingsets:
                coding_set_list = [
                    frame_codingsets[row['id']].get(i) or ''
                    for i in range(max(frame_codingsets[row['id']]))]
            args.writer.objects['coding-frames.csv'].append(dict(
                ID=row['id'],
                Language_ID=lmap[row['language_id']],
                Coding_Frame_Schema=row['coding_frame_schema'],
                Description=row['description'],
                Comment=row['comment'],
                Derived=row['derived'],
                Argument_Types=arg_type_list,
                Coding_Set_IDs=coding_set_list,
            ))

        for row in self.query("select * from alternations order by language_id, id"):
            args.writer.objects['alternations.csv'].append(dict(
                ID=row['id'],
                Name=row['name'],
                Description=row['description'],
                Language_ID=lmap[row['language_id']],
                Alternation_Type=row['alternation_type'],
                Coding_Frames_Text=row['coding_frames_text'],
                Complexity=row['complexity'],
            ))

        for row in self.query('select * from alternation_values order by verb_id, alternation_id, id'):
            vid = int(row['verb_id'])
            if vid in fmap and fmap[vid]:
                args.writer.objects['alternation-values.csv'].append(dict(
                    ID=row['id'],
                    Form_ID=fmap[vid][0],
                    Alternation_ID=row['alternation_id'],
                    Alternation_Occurs=row['alternation_occurs'],
                    Comment=row['comment'],
                    Derived_Code_Frame_ID=row['derived_coding_frame_id'],
                ))

    def create_schema(self, cldf):
        cldf.add_component(
            'ExampleTable',
            'Example_Type',
            'http://cldf.clld.org/v1.0/terms.rdf#source',
            {
                "name": "Form_IDs",
                "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#formReference",
                "separator": ";",
            })

        cldf.add_table(
            'microroles.csv',
            'http://cldf.clld.org/v1.0/terms.rdf#id',
            'http://cldf.clld.org/v1.0/terms.rdf#name',
            {
                'name': 'Parameter_ID',
                'titles': 'Concept_ID',
                'propertyUrl': 'http://cldf.clld.org/v1.0/terms.rdf#parameterReference',
            },
            'Role_Letter',
            'Original_Or_New',
            'Name_For_URL')

        cldf.add_table(
            'coding-sets.csv',
            'http://cldf.clld.org/v1.0/terms.rdf#id',
            'http://cldf.clld.org/v1.0/terms.rdf#languageReference',
            'http://cldf.clld.org/v1.0/terms.rdf#name',
            'http://cldf.clld.org/v1.0/terms.rdf#comment')

        cldf.add_table(
            'coding-frames.csv',
            'http://cldf.clld.org/v1.0/terms.rdf#id',
            'http://cldf.clld.org/v1.0/terms.rdf#languageReference',
            'Coding_Frame_Schema',
            'http://cldf.clld.org/v1.0/terms.rdf#description',
            'http://cldf.clld.org/v1.0/terms.rdf#comment',
            'Derived',
            {
                'name': 'Argument_Types',
                'datatype': 'string',
                'separator': ';',
            },
            {
                'name': 'Coding_Set_IDs',
                'datatype': 'string',
                'separator': ';',
            })

        cldf.add_table(
            'alternations.csv',
            'http://cldf.clld.org/v1.0/terms.rdf#id',
            'http://cldf.clld.org/v1.0/terms.rdf#languageReference',
            'http://cldf.clld.org/v1.0/terms.rdf#name',
            'http://cldf.clld.org/v1.0/terms.rdf#description',
            'Alternation_Type',
            'Coding_Frames_Text',
            'Complexity')

        cldf.add_table(
            'alternation-values.csv',
            'http://cldf.clld.org/v1.0/terms.rdf#id',
            'http://cldf.clld.org/v1.0/terms.rdf#formReference',
            'Alternation_ID',
            'Alternation_Occurs',
            'http://cldf.clld.org/v1.0/terms.rdf#comment',
            'Derived_Code_Frame_ID')

        cldf.add_foreign_key('coding-frames.csv', 'Coding_Set_IDs', 'coding-sets.csv', 'ID')
        cldf.add_foreign_key('alternation-values.csv', 'Alternation_ID', 'alternations.csv', 'ID')
        cldf.add_foreign_key('alternation-values.csv', 'Derived_Code_Frame_ID', 'coding-frames.csv', 'ID')

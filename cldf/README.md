<a name="ds-cldfmetadatajson"> </a>

# Wordlist CLDF dataset derived from Hartmann et al.'s "Valency Patterns Leipzig" from 2013

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Hartmann, Iren & Haspelmath, Martin & Taylor, Bradley (eds.) 2013. Valency Patterns Leipzig. Leipzig: Max Planck Institute for Evolutionary Anthropology. (Available online at http://valpal.info)
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Wordlist](http://cldf.clld.org/v1.0/terms.rdf#Wordlist)
[dc:format](http://purl.org/dc/terms/format) | <ol><li>http://concepticon.clld.org/contributions/Hartmann-2013-162</li></ol>
[dc:identifier](http://purl.org/dc/terms/identifier) | http://valpal.info/
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/3.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/lexibank/valpal
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/lexibank/valpal/tree/601021b">lexibank/valpal 601021b</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.4">Glottolog v4.4</a></li><li><a href="https://github.com/concepticon/concepticon-data/tree/v2.5.0">Concepticon v2.5.0</a></li><li><a href="https://github.com/cldf-clts/clts/tree/v2.1.0">CLTS v2.1.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>lingpy-rcParams</strong>: <a href="./lingpy-rcParams.json">lingpy-rcParams.json</a></li><li><strong>python</strong>: 3.8.10</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | valpal
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3599


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Local_ID](http://purl.org/dc/terms/identifier) | `string` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | 
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Cognacy` | `string` | 
`Loan` | `boolean` | 
`Graphemes` | `string` | 
`Profile` | `string` | 
`verb_type` | `string` | 
`original_script` | `string` | 
`simplex_or_complex` | `string` | 
`Basic_Coding_Frame_ID` | `string` | References [coding-frames.csv::ID](#table-codingframescsv)

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 36


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
`Glottolog_Name` | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
`Family` | `string` | 
`contributors` | `string` | 
`continent` | `string` | 
`Comment` | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 162


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Concepticon_ID](http://cldf.clld.org/v1.0/terms.rdf#concepticonReference) | `string` | 
`Concepticon_Gloss` | `string` | 
`typical_context` | `string` | 
`role_frame` | `string` | 
`meaning_list` | `string` | 
`label_for_url` | `string` | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 10837


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References the language of the translated text<br>References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Original_Orthography` | `string` | 
`Translation_Other` | `string` | 
`Number` | `integer` | 
`Example_Type` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Form_IDs](http://cldf.clld.org/v1.0/terms.rdf#formReference) | list of `string` (separated by `;`) | References [forms.csv::ID](#table-formscsv)

## <a name="table-microrolescsv"></a>Table [microroles.csv](./microroles.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 563


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
`Role_Letter` | `string` | 
`Original_Or_New` | `string` | 
`Name_For_URL` | `string` | 

## <a name="table-codingsetscsv"></a>Table [coding-sets.csv](./coding-sets.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 391


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 

## <a name="table-codingframescsv"></a>Table [coding-frames.csv](./coding-frames.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 1204


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
`Coding_Frame_Schema` | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Derived` | `string` | 

## <a name="table-codingframeindexnumberscsv"></a>Table [coding-frame-index-numbers.csv](./coding-frame-index-numbers.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 2830


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Coding_Frame_ID` | `string` | References [coding-frames.csv::ID](#table-codingframescsv)
`Index_Number` | `integer` | 
`Coding_Set_ID` | `string` | References [coding-sets.csv::ID](#table-codingsetscsv)
`Argument_Type` | `string` | 
`Microrole_IDs` | list of `string` (separated by `;`) | References [microroles.csv::ID](#table-microrolescsv)

## <a name="table-formcodingframemicrorolescsv"></a>Table [form-coding-frame-microroles.csv](./form-coding-frame-microroles.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 6069


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | References [forms.csv::ID](#table-formscsv)
`Coding_Frame_ID` | `string` | References [coding-frames.csv::ID](#table-codingframescsv)
`Microrole_IDs` | list of `string` (separated by `;`) | References [microroles.csv::ID](#table-microrolescsv)

## <a name="table-codingframeexamplescsv"></a>Table [coding-frame-examples.csv](./coding-frame-examples.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 3377


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | References [forms.csv::ID](#table-formscsv)
`Coding_Frame_ID` | `string` | References [coding-frames.csv::ID](#table-codingframescsv)
[Example_IDs](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) | list of `string` (separated by `;`) | References [examples.csv::ID](#table-examplescsv)

## <a name="table-alternationscsv"></a>Table [alternations.csv](./alternations.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 483


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
`Alternation_Type` | `string` | 
`Coding_Frames_Text` | `string` | 
`Complexity` | `string` | 

## <a name="table-alternationvaluescsv"></a>Table [alternation-values.csv](./alternation-values.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 46137


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | References [forms.csv::ID](#table-formscsv)
`Alternation_ID` | `string` | References [alternations.csv::ID](#table-alternationscsv)
`Alternation_Occurs` | `string` | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Derived_Code_Frame_ID` | `string` | References [coding-frames.csv::ID](#table-codingframescsv)
[Example_IDs](http://cldf.clld.org/v1.0/terms.rdf#exampleReference) | list of `string` (separated by `;`) | References [examples.csv::ID](#table-examplescsv)


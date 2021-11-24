ValPaL data model
=================


## Verbs and meanings

At its heart the dataset is a wordlist, so it follows the conventions used in
other CLDF Wordlists (see [the lexibank organisation on Github][lexibank-org]
for more examples):

[lexibank-org]: https://github.com/lexibank

 * `parameters.csv`: List of meanings
 * `languages.csv`: List of languages
 * `forms.csv`: List of verb forms expressing a given meaning in a given
   language

## Coding frames

`coding-frames.csv` contains a list of all coding frames.  This includes *basic
coding frames* for each verb (referenced in the `Basic_Coding_Frame_ID` column
in the `forms.csv` table), as well as *derived coding frames*, which are the
result of alternations.

## Coding sets and argument types

`coding-frame-index-numbers.csv` links the coding sets and argument types to
each coding frame.  Each argument gets its own row, mapping the assigned number
to a reference to `coding-sets.csv` and a string representation of the argument
type (`A`, `P`, etc.).  Here is an illustrated example (with string
representations instead of IDs for readability):

| ID           | Coding frame          | Index number | Coding set    | Argument type |
| ------------ | --------------------- | ------------ | ------------- | ------------- |
| 2710206975-1 | 1-nom V.subj[1] 2-acc | 1            | NP-nom V.subj | A             |
| 2710206975-2 | 1-nom V.subj[1] 2-acc | 2            | NP-acc        | P             |

## Microroles

`microroles.csv` contains a list of all microroles.  Microroles are referenced
in two places:

 * in the `Microrole_IDs` column `coding-frame-index-numbers.csv` table, linking
   microroles to specific arguments of a coding frame

 * in `form-coding-frame-microroles.csv`, linking microroles to coding frames of
   specific verbs

## Alternations

Alternations are implemented using two tables:

 * `alternations.csv`: List of possible alternations
 * `alternation-values.csv`: Specific alternations for specific verbs, and the
   resulting derived coding frame

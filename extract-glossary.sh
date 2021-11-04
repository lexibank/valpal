#!/bin/sh

sqlite3 raw/valency.sqlite 'select * from terms' -header --csv \
    | sed 's/<\/\?SPAN[^>]*>//g' \
    | csvformat \
    > etc/terms.csv

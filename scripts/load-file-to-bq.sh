#!/bin/bash
set -eu

location="$1"
dataset="$2"
table="$3"
path_to_source="$4"

bq --location="$location" load \
    --headless \
    --source_format=NEWLINE_DELIMITED_JSON \
    --autodetect \
    "$dataset.$table" \
    "$path_to_source"

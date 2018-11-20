#!/bin/bash
set -e

function dump {
    project="elife-data-pipeline"
    dataset="nifidemo4_temp"
    table=$1
    bq show --format prettyjson "$project:$dataset.$table" | jq .schema > ./schemas/$table.json
}

dump 380_datascience_early_career_researchers
dump 455_datascience_editors
dump 489_datascience_editor_keywords
dump 705_datascience_reviewer_identity_revealed_last_week

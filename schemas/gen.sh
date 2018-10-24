#!/bin/bash
bq show --format=json elife-data-pipeline:nifidemo4_temp.705_datascience_reviewer_identity_revealed__last_week | jq '.schema'

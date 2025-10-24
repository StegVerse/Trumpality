#!/usr/bin/env bash
set -e
python CORE/ingest_pipeline/url_list_ingest.py   --subject "Donald J. Trump"   --topic_cluster general   --urls seeds/sources.urls.txt

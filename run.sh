#!/bin/bash

MEDLINE_EXTRACTS="MEDLINE_phosphoproteomics_ras/all.txt"
# python doc_filter.py <$MEDLINE_EXTRACTS

python search_term_study.py <$MEDLINE_EXTRACTS



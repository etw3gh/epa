#!/bin/bash
cat www.epa.gov.csv | awk {'print $1'} | tr "," " "  | grep -v ".pdf" | grep -v ".zip" | grep -v ".docx" | grep -v  ".xls" | grep -v ".txt" | grep -v ".gz" | uniq | sort > cleaned_nofiles.txt


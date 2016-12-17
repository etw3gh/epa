#!/usr/bin/env python3
final = []
final.append('url, lastmod')
with open('www.epa.gov.xml', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (line.startswith("<url>")):
            clean = line.replace("<url><loc>", "")
            clean = clean.replace("</loc><lastmod>", ", ")
            clean = clean.replace("</lastmod></url>", "")
            final.append(clean)

with open('www.epa.gov.csv', 'w') as csv:
    for line in final:
        csv.write(line)

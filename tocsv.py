#!/usr/bin/env python3
final = []
header_line = 'url, lastmod\n'
with open('www.epa.gov.xml', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (line.startswith("<url>")):
            clean = line.replace("<url><loc>", "")
            clean = clean.replace("</loc><lastmod>", ", ")
            clean = clean.replace("</lastmod></url>", "")
            final.append(clean)

with open('www.epa.gov.csv', 'w') as csv:
    csv.write(header_line)
    for line in sorted(final):
        csv.write(line)

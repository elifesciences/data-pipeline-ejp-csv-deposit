"""WARN: this code is run without a virtualenv
it must not have any dependencies other than Python3"""

import json, sys, csv, fileinput, datetime
from datetime import timezone

def readlines(fh, n):
    return [fh.readline().rstrip() for _ in range(0, n)]

def extra_header(fh):
    # I'm hoping this will just be the first two lines in every csv file
    return list(readlines(fh, 3))

def normalise(colheader):
    return colheader.lower().strip().replace(' ', '_')

def parse_date(string):
    prefix = "Generated on "
    dtstr = string.strip('"')[len(prefix):]
    dtobj = datetime.datetime.strptime(dtstr, "%B %d, %Y")
    return dtobj.strftime("%Y-%m-%d")

def now():
    dtobj = datetime.datetime.now(timezone.utc)
    return dtobj.strftime("%Y-%m-%dT%H:%M:%SZ")

def main(input=None, output=None):
    fh = input or fileinput.input()
    out = output or print

    _, generated_date_header, _ = extra_header(fh)
    date_generated = parse_date(generated_date_header)
    time_now = now()

    header_reader = csv.reader(fh)
    header = list(map(normalise, next(header_reader)))

    reader = csv.DictReader(fh, fieldnames=header)
    for row in reader:
        row["generated_date"] = date_generated
        row["imported_timestamp"] = time_now
        out(json.dumps(row))

if __name__ == '__main__':
    main()

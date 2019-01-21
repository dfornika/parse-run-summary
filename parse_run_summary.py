#!/usr/bin/python

import sys
import re
import json

def parse_read_summary(summary_path):
    read_summary_headers = []
    read_summary_lines = []
    # Basic approach to parsing text between two specific lines
    # described here: https://stackoverflow.com/a/7559542/780188
    with open(summary_path) as summary:
        for line in summary:
            if re.match("^Level", line):
                read_summary_headers = re.split("\s*,", line.rstrip())
                read_summary_headers = [
                    x.lower().replace(" ", "_") for x in read_summary_headers
                ]
                read_summary_headers = [
                    x.replace("%>=q30", "percent_greater_than_q30") for x in read_summary_headers
                ]
                break
        for line in summary:
            if re.match("^Total", line):
                read_summary_lines.append(re.split("\s*,", line.rstrip()))
                break
            read_summary_lines.append(re.split("\s*,", line.rstrip()))

    read_summary = []
    for line in read_summary_lines:
        read_summary_line_dict = {}
        for idx, header in enumerate(read_summary_headers):
            if header == 'level':
                read_summary_line_dict[header] = line[idx]
            elif header == 'intensity_c1':
                read_summary_line_dict[header] = int(line[idx])
            else:
                read_summary_line_dict[header] = float(line[idx])
        read_summary.append(read_summary_line_dict)
    
    return read_summary

def parse_read_summary_detail(summary_path):
    delimiters = [
        ("^Read 1$", "Read 2 \(I\)$"),
        ("^Read 2 \(I\)$", "^Read 3 \(I\)$"),
        ("^Read 3 \(I\)$", "^Read 4$"),
        ("^Read 4$", "^Extracted:"),
    ]
    headers = []
    int_fields = {
        'lane',
        'tiles',
    }
    float_fields = {
        'legacy_phasing_rate',
        'legacy_prephasing_rate',
        'reads',
        'reads_pf',
        'percent_greater_than_q30',
        'yield',
    }
    read_summary_detail = {}
    # Basic approach to parsing text between two specific lines
    # described here: https://stackoverflow.com/a/7559542/780188
    for start, stop in delimiters:
        lines = []
        with open(summary_path) as summary:
            for line in summary:
                if re.match(start, line):
                    break
            for line in summary:
                if re.match(stop, line):
                    break
                if re.match("^Lane", line):
                    headers = re.split("\s*,", line.rstrip())
                    headers = [
                        x.lower().replace(" ", "_") for x in headers
                    ]
                    headers = [
                        x.replace("%>=q30", "percent_greater_than_q30") for x in headers
                    ]
                else:
                    lines.append(re.split("\s*,", line.rstrip()))

        section_list = []
        for line in lines:
            line_dict = {}
            for idx, header in enumerate(headers):
                if header in float_fields:
                    line_dict[header] = float(line[idx])
                elif header in int_fields:
                    line_dict[header] = int(line[idx])
                else:
                    line_dict[header] = line[idx]
            section_list.append(line_dict)
        read_summary_detail_key = re.sub("\^|\\\\|\(|\)", "", start).replace("$", "").replace(" ", "_").lower()
        read_summary_detail[read_summary_detail_key] = section_list 
    
    return read_summary_detail

def main():
    summary_path = sys.argv[1]
    read_summary = parse_read_summary(summary_path)
    read_summary_detail = parse_read_summary_detail(summary_path)
    # print(json.dumps(read_summary))
    print(json.dumps(read_summary_detail))
    
if __name__ == '__main__':
    main()

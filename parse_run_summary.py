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
    headers = []
    lines = []
    # Basic approach to parsing text between two specific lines
    # described here: https://stackoverflow.com/a/7559542/780188
    with open(summary_path) as summary:
        for line in summary:
            if re.match("^Read 1$", line):
                break
        for line in summary:
            if re.match("^Read 2 \(I\)$", line):
                break
            print(line)

    read_summary_detail = []
    for line in lines:
        line_dict = {}
        for idx, header in enumerate(headers):
            if header == '':
                read_summary_line_dict[header] = line[idx]
            elif header == '':
                read_summary_line_dict[header] = int(line[idx])
            else:
                read_summary_line_dict[header] = float(line[idx])
        read_summary_detail.append(line_dict)
    
    return read_summary_detail

def main():
    summary_path = sys.argv[1]
    read_summary = parse_read_summary(summary_path)
    # parse_read_summary_detail(summary_path)
    print(json.dumps(read_summary))
    
if __name__ == '__main__':
    main()

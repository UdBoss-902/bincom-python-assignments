# 2nd Contact Session Assignment - Package Setup
# SSA Baby Names 2008 Parser

A Python script to parse and extract popular baby name rankings for the year 2008 from Social Security Administration HTML data (`baby2008.html`)[cite: 7].

## Features

- Extracts ranks, male names, and female names from `baby2008.html`[cite: 7].
- Exports parsed data into structured formats (CSV, JSON).
- Allows searching for specific names and rank lookup.

## Project Structure

```text
.
├── baby2008.html       # Raw SSA source dataset[cite: 7]
├── parse_names.py      # Python extraction script
├── requirements.txt    # External dependencies
├── .gitignore          # Version control ignore rules
└── README.md           # Documentation
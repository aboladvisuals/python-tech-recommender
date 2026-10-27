# Tech Stack Recommender

A command-line recommender that ranks job roles from the skills you type. It compares your skills with each role and prints the top 3.

## How to run

    python recommend.py

Type at least three skills, separated by commas. Example: `python, sql, excel`

## Example result

    Data Analyst: 1.00
    Data Scientist: 0.67
    Backend Developer: 0.67

## How it works

- Roles and their skills are stored in a dictionary. There is no downloaded dataset.
- Fewer than three skills is rejected. An empty profile would score 0 against every role.
- Each role is a row of 1s and 0s. Cosine similarity measures how aligned that row is with yours.
- Scores are sorted from high to low. Only the top 3 are shown.
- This does not use other people's history. The match comes from the skills written on the role.

## Files

| File | What it is |
| --- | --- |
| recommend.py | The program |
| README.md | This page |
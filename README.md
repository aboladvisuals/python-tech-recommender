## Tech Stack Recommender

A command-line recommender that ranks job roles from the skills you type. It compares your skills with each role and prints the top 3.

## How to run

`powershell
python recommend.py Data Analyst: 1.00
Data Scientist: 0.67
Backend Developer: 0.67 How it works
Roles and their skills are stored in a dictionary. There is no downloaded dataset.
Fewer than three skills is rejected. An empty profile would score 0 against every role.
Each role is a row of 1s and 0s. Cosine similarity measures how aligned that row is with yours.
Scores are sorted from high to low. Only the top 3 are shown.
This does not use other people's history. The match comes from the skills written on the role.
Files
















FileWhat it isrecommend.pyThe programREADME.mdThis page

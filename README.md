# [OUTDATED]
As of 3rd October 2022, this script will not work for the new OSCP exercises (with topic exercises) due to a new numbering convention.

# About this script 
This is a python script that checks your lab report to see if there are any unincluded/missing exercises. It DOES NOT check whether the exercise(s) are completed, it simply checks if the exercise number is included in your lab report.

# Pre-requisites
- docx2txt library (will be required to read your .docx lab report)
```text
$ pip install docx2txt
```
# Running the script
Run this python script with the absolute path to your .docx file as the first argument.
```text
$ python OSCP-Check-Exercises.py [file.docx]
```

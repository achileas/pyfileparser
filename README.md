pyfileparser
============

Parses a series of subject CSVs and attempts to match same subjects together

Specifically, when run with a given number of CSV files (as .txts), it merges the information into a single dictionary,
then matches all subjects with the same subject name value. Because these are unique to the person in this particular
dataset, it is a simple check for repeat subjects. It writes new CSVs for each subject with a collection of every trial
they completed. In short, it converts a series of CSVs ordered by each subject's 1st, 2nd, 3rd, etc. sessions (1 file
per session) to a series of CSVs grouped by a single subject. Since subject numbers are ordinal, the order of sessions
is preserved. 

For my particular application, it will allow for further data processing within MATLAB. 

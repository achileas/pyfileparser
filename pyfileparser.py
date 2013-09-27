# pyfileparser
# reads through reapeat subject files
# groups same subjects together for later analysis via matlab
# inputs 1.txt, 2.txt,..., 3.txt

import csv

def loadSubjects(iter_num):
    """
    Returns a dictionary mapping subject name to full lines from files
    """

    helper_list = []
    subj_dict = {}
    for i in range(1,iter_num+1):
        filename = str(i) + '.txt'
        try:
            inputFile = open(filename)
            for line in inputFile:
                helper_list.append(line.split(','))

            for element in helper_list:
                element[-1] = element[-1].rstrip('\n')
                subj_dict[element[0]] = (element[1:-1])

        

        except:
            print "Error: File not found"

    return subj_dict


def matchSubjects(subj_dict):
    """
    Matches subjects in class_dict to other instances of themselves.
    Checks if subject names are the same, as they are unique to subject
    (a number is appended if 
    """
    for subject in subj_dict.keys():  
        subdict = dict((k,v) for k, v in subj_dict.iteritems() if subj_dict[k][0] == subj_dict[subject][0])
        ## call method to add subdict to printFile fxn
        printFile(subdict)


def printFile(subdict):
    filename = subdict.values()[0][0] + '.csv'
    with open(filename,'wb') as f:
        w = csv.writer(f)
        w.writerows(subdict.items())
    
    
iternum = int(raw_input("Please enter number of files to iterate through: "))
subject_dict = loadSubjects(iternum)
matchSubjects(subject_dict)

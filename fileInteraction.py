"""fileInteraction.py provides functions to pull the contents from all
files in a given directory into a dictionary of them form 
{'filename' : word_set}, where the content is saved as a set of 
unique words contained in the file.  Common punctuation items are removed
from the words to allow meaningful comparison to other documents.
"""

import glob

directory = "C:\\Users\\student\\Documents\\Python\\Document Grouping\\Documents"

def readAllFilesToSets(directory):
    directory_list =directory + "\\*"
    fileList = glob.glob(directory_list)
    documents ={}
    for file in fileList:
        documents[file] = readSingleFileToSet(file)
    return documents

def readSingleFileToSet(file):
    with open(file, 'r', encoding='ascii', errors='ignore') as f:
        content = f.read().lower()
    content = stripPunctuation(content)
    return set(content.split())

def stripPunctuation(content):
    content = content.replace('. ', ' ')
    if content[-1] == '.':
        content = content[:-1]
    content = content.replace('.\n', ' ')
    content = content.replace(',', '')
    content = content.replace('!', '')
    content = content.replace('?', '')
    content = content.replace('"', '')
    content = content.replace("'", '')
    content = content.replace('/', ' ')
    content = content.replace('\\', ' ')
    return content

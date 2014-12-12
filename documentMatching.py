"""documentMatching.py receieves a dictionary of the form 
{'filename' : word_set}, where the word_set is the set of all unique
words contained in 'filename'.  Commonly used words are removed from
these lists.  These files are then placed into groups based on 
similarity in contents (word_set).  The goal is: given a document,
find other documents that have similar content.
"""
import fileInteraction

min_similarity = 10  # Minimum similarity score needed to count as match


def removeCommonWords(document_word_set):
    articles = ['a', 'an', 'the']
    conjunctions = ['and', 'but', 'or', 'nor', 'for', 'yet', 'so']
    helpingVerbs = ['is', 'are', 'was', 'were', 'be', 'been', 'am', 'do',
                    'does', 'did', 'has', 'had', 'have', 'having', 'can',
                    'could', 'shall', 'should', 'will', 'would' 'may', 
                    'might', 'must']
    pronouns = ['i', 'me', 'we', 'us', 'you', 'he', 'him', 'she', 'her',
                'it', 'they', 'them', 'our', 'ours', 'there', 'this', 
                'some', 'who']
    prepositions = ['a', 'about', 'aboard', 'above', 'across', 'after',
                    'against', 'along', 'alongside', 'amid', 'among',
                    'amongst', 'around', 'as', 'aside', 'astride', 'at',
                    'atop','barring', 'before', 'behind', 'below', 'beneath',
                    'beside', 'besides', 'between', 'beyond', 'but', 'by', 
                    'concerning', 'despite', 'down', 'during', 'except', 
                    'excluding', 'failing', 'following', 'for', 'from', 
                    'given', 'in', 'including', 'inside', 'into', 'like',
                    'midst', 'near', 'next', 'notwithstanding', 'o', 'of', 
                    'off', 'on', 'onto', 'opposite', 'out', 'outside', 'over',
                    'past', 'per', 'plus', 'pro', 'qua', 'regarding', 'round', 
                    'sans', 'save', 'since', 'than', 'through', 'thru', 
                    'throughout', 'thruout', "'till", 'to', 'toward', 'towards',
                    'under', 'underneath', 'unlike', 'until', 'unto', 'up', 
                    'upon', 'versus', 'via','with', 'within', 'without', 'worth']
    miscelaneous = []
    common_words = set(articles + conjunctions + helpingVerbs + pronouns + prepositions + miscelaneous)

    return document_word_set - common_words

def getTextAndCleanIt(directory):
    document_dict = fileInteraction.readAllFilesToSets(directory)  # Will need to change this line based on data source
    for document in document_dict:
        word_set = document_dict[document]
        document_dict[document] = removeCommonWords(word_set)
    return document_dict

def generateWordCount(document_dict):
    word_count = {}
    for document in document_dict:
        for word in document_dict[document]:
            word_count[word] = word_count[word] + 1 if word in word_count else 1
    return word_count

def createGroups(document_dict, word_count):
    groups = {}
    for document in document_dict:
        doc_name = document[60:]  #  Slice depends on file path
        groups[doc_name] = []
        addDocumentsToGroup(groups, document, document_dict, word_count)
    printGroups(groups)

def addDocumentsToGroup(groups, document_to_compare_to, document_dict, word_count):
    compare_to_word_set = document_dict[document_to_compare_to]
    compare_to_name = document_to_compare_to[60:]  #  Slice depends on file path
    all_other_docs = [doc for doc in document_dict]
    all_other_docs.remove(document_to_compare_to)
    #print('all_other_docs is:')
    #print(all_other_docs)
    for document in all_other_docs:
        comparee_word_set = document_dict[document]
        comparee_name = document[60:]  #  Slice depends on file path.
        #print('We are comparing {} to {}'.format(comparee_name, compare_to_name))
        #print('The {} group currently consists of: '.format(compare_to_name))
        #print(groups[compare_to_name])
        if comparee_name not in groups[compare_to_name]:
            sub_set = comparee_word_set & compare_to_word_set
            similarity = 0
            for word in sub_set:
                similarity += 1/word_count[word]
            print(similarity)  #for checking, remove this line
            if similarity >=  min_similarity:
                groups[compare_to_name].append(comparee_name)

def printGroups(groups):
    for group in groups:
        print('The {} group is:'.format(group))
        print(groups[group])
        print('')

if __name__ == '__main__':
    directory = "C:\\Users\\student\\Documents\\Python\\Document Grouping\\Resumes"
    document_dict = getTextAndCleanIt(directory)
    word_count = generateWordCount(document_dict)
    groups = createGroups(document_dict, word_count)

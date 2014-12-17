"""documentMatching.py receieves a dictionary of the form 
{'filename' : word_set}, where the word_set is the set of all unique
words contained in 'filename'.  Commonly used words are removed from
these lists.  These files are then placed into groups based on 
similarity in contents (word_set).  The goal is: given a document,
find other documents that have similar content.
"""
import fileInteraction

min_jaccard_coef = 0.025  #  Minimum Jaccard Similarity Coefficient to count as related

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
        doc_name = document[60:]  #  Slice size depends on file path
        groups[doc_name] = []
        addDocumentsToGroup(groups, document, document_dict, word_count)
    printGroups(groups)

def addDocumentsToGroup(groups, document_to_compare_to, document_dict, word_count):
    compare_to_word_set = document_dict[document_to_compare_to]
    compare_to_name = document_to_compare_to[60:]  #  Slice size depends on file path
    all_other_docs = [doc for doc in document_dict]
    all_other_docs.remove(document_to_compare_to)
    
    for document in all_other_docs:
        comparee_word_set = document_dict[document]
        comparee_name = document[60:]  #  Slice size depends on file path.
        jaccard_coef = getJaccardCoefficient(compare_to_word_set, comparee_word_set, word_count)
        print(jaccard_coef)
        if jaccard_coef >= min_jaccard_coef:
            groups[compare_to_name].append(comparee_name)

def getJaccardCoefficient(word_set_1, word_set_2, word_count):
    union = word_set_1 | word_set_2
    intersection = word_set_1 & word_set_2
    union_magnitude = getWeightedMagnitude(union, word_count)
    intersection_magnitude = getWeightedMagnitude(intersection, word_count)
    return intersection_magnitude/union_magnitude

def getWeightedMagnitude(word_set, word_count):
    magnitude = 0
    for word in word_set:
        magnitude += 1/word_count[word]
    return magnitude

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

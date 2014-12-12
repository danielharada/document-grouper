"""documentMatching.py receieves a dictionary of the form 
{'filename' : word_set}, where the word_set is the set of all unique
words contained in 'filename'.  Commonly used words are removed from
these lists.  These files are then placed into groups based on 
similarity in contents (word_set).  The goal is: given a document,
find other documents that have similar content.
"""
import FileInteraction

grouping_ratio = 0.25  # Need to match on 25% of the words in a document list to count as related


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
    document_dict = FileInteraction.readAllFilesToSets(directory)  # Will need to change this line based on data source
    for document in document_dict:
        word_set = document_dict[document]
        document_dict[document] = removeCommonWords(word_set)
    return document_dict

def createGroups(document_dict):
    groups = {}
    i = 1
    for document in document_dict:
        groups['group{}'.format(i)] = [key for key in document_dict]
        removeUnrelatedDocumentsFromGroup(groups['group{}'.format(i)], document_dict, document)
        i += 1
    printGroups(groups)

def removeUnrelatedDocumentsFromGroup(group, document_dict, document_to_compare_to):
    delete_list = []
    for document in group:
        comparee_word_set = document_dict[document]
        compare_to_word_set = document_dict[document_to_compare_to]
        sub_set = comparee_word_set & compare_to_word_set
        if len(sub_set) < grouping_ratio*len(compare_to_word_set):
            delete_list.append(document)

    removeElements(group, delete_list)

def removeElements(remove_from_list, remove_these_items):
    for item in remove_these_items:
        remove_from_list.remove(item)


def printGroups(groups):
    for group in groups:
        print('{} is:'.format(group))
        print(groups[group])
        print('')

if __name__ == '__main__':
    directory = "C:\\Users\\student\\Documents\\Python\\Document Grouping\\Resumes"
    document_dict = getTextAndCleanIt(directory)
    groups = createGroups(document_dict)

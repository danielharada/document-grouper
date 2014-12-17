document-grouper
========

This program is used to group text documents based off of similarities in their contents.  Intended to provide automatic matching for a site which pairs mentors and mentees.  Currently the pairing happens by manual review of free form text responses from candidates regarding mission statements and CVs.

documentMatching.py utilizes the file accessing functions in fileInteraction.py to pull document data from a folder, then applies some data cleaning, and then groups the files based on content similarity.

Version 3 of documentMatching.py uses a Jaccard similarity coefficient to determine if documents are related or not.  Instead of using the length of the word sets as their magnitudes, each word is given a weight based off of its frequnecy of appearance across all documents.  If the word appears n times, then the weighting given to that word is 1/n.  This serves to de-value commonly used words, giving more emphasis to domain specific words.

A minimum Jaccard coefficient is set to determine if two documents should be considered related.  A training set should be used to help determine an appropriate value for this minimum.  The current value of 0.025 was chosen based on the sample resume set contained in this repository.

All members of a group should be related to the document seeding the group, but may not have a strong similarity to other members of the group.  Grouping is symmetric, i.e. if Document1 is added to Document2's group, then Document2 will also be added to Document1's group.

---
__*Planned improvements*__:

Explore shingling to help check for multi-word phrases.  Current matching is based only on individual words, no capabality to check the context of that word.

---
__*Historic Versions*__:

**Version 2** of documentMatching.py counts the number of documents which use a given word to weight its importance when forming groups.  The weighting is 1/n, where n is the number of documents in which the word appears.  This causes words that appear more frequently to be of less weight, as it is more likely to be noise which does not convey a unique skill.  Each document is assigned a similarity score compared to each other documents, which is the sum of all weights for its word set.  A minimum similarity score is set in documentMatching.py, if the similarity is higher than this minimum then the two documents are grouped together as being related.

The minimum similarity score is still being tested to determine what a good cutoff score is.

All members of a group should be related to the document seeding the group, but may not have a strong similarity to other members of the group.  Grouping is symmetric, i.e. if Document1 is added to Document2's group, then Document2 will also be added to Document1's group.

**Version 1** examines the set of unique words in a document, and then checks this set against all other documents' word sets.  If a certain percentage of these words match (currently set to 25%, percentage based on length of initial document's word set), then the two documents are grouped together.  Each document seeds its own group.  Since the matching is based off of the seeding document's word set length, the matching is not necessarily symmetric, i.e. Document1's matching group could contain Document2, but Document2's matching group does not contain Document1.


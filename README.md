document-grouper
========

This program is used to group text documents based off of similarities in their contents.  Intended to provide automatic matching for a site which pairs mentors and mentees.  Currently the pairing happens by manual review of free form text responses from candidates regarding mission statements and CVs.

documentMatching.py utilizes the file accessing functions in fileInteraction.py to pull document data from a folder, then applies some data cleaning, and then groups the files based on content similarity.

Version 2 of documentMatching.py counts the number of documents which use a given word to weight its importance when forming groups.  The weighting is 1/n, where n is the number of documents in which the word appears.  This causes words that appear more frequently to be of less weight, as it is more likely to be noise which does not convey a unique skill.  Each document is assigned a similarity score compared to each other documents, which is the sum of all weights for its word set.  A minimum similarity score is set in documentMatching.py, if the similarity is higher than this minimum then the two documents are grouped together as being related.

The minimum similarity score is still being tested to determine what a good cutoff score is.

All members of a group should be related to the document seeding the group, but may not have a strong similarity to other members of the group.  Grouping is symmetric, i.e. if Document1 is added to Document2's group, then Document2 will also be added to Document1's group.

---
Planned improvements:

Use the Jaccard similarity coefficient to measure similarity between groups, with the current similarity score of the sum of word weights as the norm of a set.  Should improve similarity rankings for documents with small unique word sets, and act as a better overall indicator of similarity.  Will need to determine an appropriate cut off similarity value for groups.

---
Historic Versions

Version 1 examines the set of unique words in a document, and then checks this set against all other documents' word sets.  If a certain percentage of these words match (currently set to 25%, percentage based on length of initial document's word set), then the two documents are grouped together.  Each document seeds its own group.  Since the matching is based off of the seeding document's word set length, the matching is not necessarily symmetric, i.e. Document1's matching group could contain Document2, but Document2's matching group does not contain Document1.


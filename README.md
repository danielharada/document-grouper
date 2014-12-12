document-grouper
========

This program is used to group text documents based off of similarities in their contents.  Intended to provide automatic matching for a site which pairs mentors and mentees.  Currently the pairing happens by manual review of free form text responses from candidates regarding mission statements and CVs.

Version 1 examines the set of unique words in a document, and then checks this set against all other documents' word sets.  If a certain percentage of these words match (currently set to 25%, percentage based on length of initial document's word set), then the two documents are grouped together.  Each document seeds its own group.  Since the matching is based off of the seeding document's word set length, the matching is not necessarily symmetric, i.e. Document1's matching group could contain Document2, but Document2's matching group does not contain Document1.


Plans for improvement:

Create a weighting list based off of frequency of a given word across all of the documents' word sets.  If a word appears more frequently, it is less likely to be a good indicator of related content.  Words with higher count will get a lower weight.

When assigning groups, will apply these weights to the count of matching items to generate a similarity score.  Will then set a minimum similarity score to count as a match.

If one document gets matched to another, add the respective documents to both of the documents' groups, i.e. force the relation to be symmetric.

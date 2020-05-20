from itertools import permutations


class Finder(object):

    def __init__(self, collection=[]):
        # super().__init__()
        self.collection = collection

    def find(self, string=None):
        """
          Finds matches from collection on the base of provided string
           - Checks if passed string is a valid token
           - Makes permutations of String
           - Traverse the permutations, finds and collection all possible matches to result list
           - return result list
        """
        result = []
        if string:
            permutes = [''.join(p) for p in permutations(string)]
            for collection_element in self.collection:
                for token in permutes:
                    if token in collection_element:
                        result.append(collection_element)
        return result

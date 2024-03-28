class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort the people list with the specified rules:
        # x[0] and x[1] respectively mean the first and second element in people list.
        # Sort by [x0] in descending order, and if x[0] are equal, sort by x[1] in ascending order. 
        people.sort(key = lambda x : (-x[0], x[1]))
        
        result = []
        for p in people:
            # insert the element p to the index p[1].
            result.insert(p[1], p)
            
        return result
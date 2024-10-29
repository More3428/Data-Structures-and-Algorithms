
def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # initialize n to be the size of len(citations)
        n = len(citations)
        # this count array will count the number of citations a paper has
        # create an array with 0s the size of n + 1
        count = [0] * (n + 1)

        
        # for loop that counts the number of papers with each citation count
        # for c in citations c is the value
        for c in citations:
            # if a paper has more citations than the total number of papers
            # it is treated as if it has n citations since h-index cant be larger than n 
            # so we add 1 to the last index in count
            if c >= n:  
                count[n] += 1
            # else we increment the value at index c by one
            # c will be the index at count
            else:
                count[c] += 1
        # Here we calculate the H-index
        # we initialize a total to 0
        total = 0
        # for loop that iterates backwards starting at the last index in the range of n
        for i in range(n, -1, -1):
            # we add the total value with the current value at count array at i
            total += count[i]
            # if the total is greater than or equal to the ith index 
            # return i
            # i is currently the index number not the value
            if total >= i:
                return i
        
        return 0
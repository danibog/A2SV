class Solution(object):
    def sortSentence(self, s):
        arr = s.split(" ")
        sortedSentence = ['']*len(arr)

        for i in arr:
            sortedSentence[int(i[-1])-1] = i[0:-1]
        
        return ((" ".join(sortedSentence)))

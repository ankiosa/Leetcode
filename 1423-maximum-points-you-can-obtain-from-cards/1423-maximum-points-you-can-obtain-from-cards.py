class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if(k>=len(cardPoints)):
            return sum(cardPoints)
        first_sum = sum(cardPoints[-k:])
        max_sum = first_sum
        print(first_sum)
        for i in range(k):
            print(cardPoints[i],cardPoints[len(cardPoints)-k])
            first_sum = cardPoints[i]-cardPoints[len(cardPoints)-k+i]+first_sum
            max_sum = max(max_sum,first_sum)
            
        return max_sum
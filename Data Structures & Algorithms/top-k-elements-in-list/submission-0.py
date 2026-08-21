class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = {}
        for i in nums:
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1 
        sorted_freq = sorted(freq, key = freq.get,reverse = True)
        return sorted_freq[:k]

        
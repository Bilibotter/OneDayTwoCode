class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            prev = 1
            for num in nums:
                if num + prev == 0:
                    return True
                prev = num
            return False
        dic = {0:-1}
        count = 0
        j = 0
        for num in nums:
            count = (count+num) % k
            if count in dic:
                if j - dic[count] > 1:
                    return True
            else:
                dic[count] = j
            j += 1
        return False

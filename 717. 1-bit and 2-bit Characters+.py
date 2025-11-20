class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        n = len(bits)
        
        while i <= n:
            if bits[i] == 0:
                i = i + 1
                if i == n:
                    return True
            else:
                i = i + 2
                if i == n:
                    return False
                




test = Solution()

result = test.isOneBitCharacter([1, 0, 0])
print(result)  # Expected: True
result = test.isOneBitCharacter([1, 1, 1, 0])
print(result)  # Expected: False
class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        leftmax = 0
        rightmax = 0
        res = 0
        # Loop until the two pointers meet
        while left <= right:
            # Process the side with the smaller height
            if arr[left] <= arr[right]:

                # Update leftmax or add trapped water
                if arr[left] >= leftmax:
                    leftmax = arr[left]  # update max if current is higher
                else:
                    res += (leftmax - arr[left])  # trapped water at this position
                left += 1
            else:
                # Update rightmax or add trapped water
                if arr[right] >= rightmax:
                    rightmax = arr[right]
                else:
                    res += (rightmax - arr[right])


                right -= 1
        return res
arr = [0,1,0,2,1,0,1,3,2,1,2,1]

sol = Solution()
# Call the function and print result
result = sol.maxWater(arr)
print("Total Trapped Rainwater:", result)

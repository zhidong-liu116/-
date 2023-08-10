'''py
lass Solution:
    solution 1: 左闭，右闭区间
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # 封闭区间"[]",封闭区间，我们需要“<=”
        while(left <= right):
            middle = (left + right) // 2 # 也可以写成 len(nums - 1),因为是中间值嘛
            if nums[middle] > target:
                right = middle - 1 # 更新右区间，并且是middle - 1，因为既然middle已经大于了 target，那就表明这不是我们想要的值
            elif nums[middle] < target:
                left = middle + 1 # 更新右区间，并且是middle + 1, 思路和上面一样
            else:
                return middle
        return -1
    
    # solution 2: 左闭，右开区间
    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) # 如果是右开，那么就是意味着<,而不是<=，所以这里要写len(nums)
    #     while(left < right): #这里的循环也一样，left < right，不能是包含=
    #         middle = (left + right) // 2 # 也可以写成 len(nums - 1),因为是中间值嘛
    #         if nums[middle] > target:
    #             right = middle # 更新右区间，因为不包含右区间
    #         elif nums[middle] < target:
    #             left = middle + 1 # 更新右区间，并且是middle + 1, 思路和上面一样
    #         else:
    #             return middle
    #     return -1
'''

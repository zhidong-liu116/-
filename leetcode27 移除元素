class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        0 #快慢指针，fast，slow pointer，一开始都从0开始，fast找新数组需要的元素，然后赋值给slow指针
        slow = 0
        for i in range(len(nums)): #这里的i就是快指针
            if nums[i] != val: # 当快指针指向的元素不等于val的时候，把这个值赋给slow pointer
                nums[slow] = nums[i] # 赋值操作
                slow += 1
        return slow

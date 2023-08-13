### 思路就是，快指用来遍历数组，找我们需要添加到新数组里的元素，而慢指针是新数组所对应的下表
### eg,当元素3是我们新数组不需要的时候，当我们的快指针指向这里，就直接跳过，然后i慢指针不变，当我们跳过元素3的时候，在更新
### 记住，赋值操作是快指针赋值给慢指针！！！

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        0 #快慢指针，fast，slow pointer，一开始都从0开始，fast找新数组需要的元素，然后赋值给slow指针
        slow = 0
        for i in range(len(nums)): #这里的i就是快指针
            if nums[i] != val: # 当快指针指向的元素不等于val的时候，把这个值赋给slow pointer
                nums[slow] = nums[i] # 赋值操作
                slow += 1 # 记住，这里的if判断过了之后再加1，因为这样才证明这里的值不是val
        return slow

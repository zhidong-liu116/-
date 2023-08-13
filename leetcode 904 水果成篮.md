### 这也是一道滑动窗口的题目，但是需要配合map，Counter()来使用，这里的Counter()是和dict差不多的，dict的子类（Counter 类是一个字典的子类，不限制键和值）
### 思路和其他的最大滑动窗口问题差不多，一个basket里最多能装两种水果，看在一个list里，在只包含两种水果的情况下最大能装多少水果
### while(len(cnt) > 2):
                y = fruits[i] # 这里指慢指针找到的水果，也就是要删除的水果名字（从头开始）
                cnt[y] -= 1
                if cnt[y] == 0:
                    cnt.pop(y)
### 这里的代码就是关键，快指针j还是用来遍历list，然后添加水果，在第二个循环这里开始判断水果数量是否超过2，超过二了就开始减，而且记住，这是一个字典，包含key value的一个pair
### 如果这里的对应value删完了，同样也需要把key删掉，换到代码这里来，就是"cnt.pop(y)"

```py
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        cnt = Counter()
        res = 0
        while(j < len(fruits)):
            cnt[fruits[j]] += 1 # 这里指快指针找到的水果
            j += 1
            while(len(cnt) > 2):
                y = fruits[i] # 这里指慢指针找到的水果，也就是要删除的水果名字（从头开始）
                cnt[y] -= 1
                if cnt[y] == 0:
                    cnt.pop(y)
                i += 1
            res = max(res, j - i)
        return res

```

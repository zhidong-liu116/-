## 反转链表，这里的主要思路就是，创建两个指针，一个为curr，记录头节点，一个为pre，记录之前的节点，用于反转

### 1, 创建两个变量，curr，pre，分别用于记录head节点，之前的节点，然后初始化，curr初始化为head（因为是第一位），pre初始化为None（因为一开始的pre没有，指向为空）
### 2， 在while循环里，后继指针对应的值记录下里，为curr.next，然后，先改变curr.next的指针指向（意味着现在的pre不是空的了），然后再改pre的赋值，因为完成更改之后，需要
### 更新pre节点和curr节点，并且同时把两个node往后移。这里记住，先更改pre指针，再改curr，避免null ptr*。while循环在这里的作用就是重复整个过程，直至头节点为空的时候，返回pre节点


```py
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        pre = None
        while(curr != None):
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        return pre
```

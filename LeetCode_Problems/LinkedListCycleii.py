# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# with 0(n) space complexity
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
        lookup = set()
        while cur:
            if cur in lookup: return cur
            lookup.add(cur)
            cur=cur.next
        return None 

# with O(1) time complexity

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return 
        slow, fast = head, head 
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: break 
        if not fast.next or not fast.next.next:return 

        slow2 = head 
        while slow.next:
            if slow == slow2:return slow 
            slow = slow.next
            slow2 = slow2.next
        return 


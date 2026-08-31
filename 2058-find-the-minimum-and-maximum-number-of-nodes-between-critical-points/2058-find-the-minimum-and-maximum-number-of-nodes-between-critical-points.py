# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1,-1]
        prev=head
        curr=head.next
        ahead=head.next.next
        i=1
        d=[]
        while ahead:
            if prev.val>curr.val<ahead.val or prev.val<curr.val>ahead.val:
                d.append(i)
            i+=1
            prev=prev.next
            curr=curr.next
            ahead=ahead.next
        if len(d)<2:
            return [-1,-1]
        
        m=d[-1]-d[0]
        n=10**5
        for j in range(1, len(d)):
            n=min(n,d[j]-d[j-1])
        return [n,m]
        
        

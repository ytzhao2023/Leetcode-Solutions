import Solution1 as sl1

list_1 = [9, 9, 9, 9, 9, 9, 9]
list_2 = [9, 9, 9, 9]

head = sl1.ListNode(list_1[0])
body = head
for i in range(1, len(list_1)):
    temp = sl1.ListNode(list_1[i])
    body.next = temp
    body = body.next
l1 = head

body = None
for i in range(len(list_2), 0, -1):
    temp = sl1.ListNode(list_2[i - 1], body)
    body = temp
l2 = body


solution = sl1.Solution()
ans = solution.addTwoNumbers(l1, l2)
while ans.next:
    print(ans.val)
    ans = ans.next
print(ans.val)

# sl.Solution().addTwoNumbers(l1, l2)
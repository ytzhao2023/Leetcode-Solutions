import Solution2 as sl2

list_1 = [9, 9, 9, 9, 9, 9, 9, 9, 9]
list_2 = [9, 9, 9, 9]

head = sl2.ListNode(list_1[0])
body = head
for i in range(1, len(list_1)):
    temp = sl2.ListNode(list_1[i])
    body.next = temp
    body = body.next
l1 = head

head = sl2.ListNode(list_2[0])
body = head
for i in range(1, len(list_2)):
    temp = sl2.ListNode(list_2[i])
    body.next = temp
    body = body.next
l2 = head


solution = sl2.Solution()
ans = solution.addTwoNumbers(l1, l2)
while ans.next:
    print(ans.val)
    ans = ans.next
print(ans.val)

# sl.Solution().addTwoNumbers(l1, l2)
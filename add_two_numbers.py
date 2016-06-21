import sys

def reversed(l_list):
        count = 1
        while l_list != None:
            temp_node = ListNode(l_list.val)
            if count == 1:
                temp_node.next = None
                count -= 1
            else:
                temp_node.next = reversed_list
            reversed_list = temp_node
            l_list = l_list.next
        return reversed_list

def addTwoNumbers(l1, l2):
    carry = 0
    count = 1
    while l1 != None or l2 != None:
        if l1 != None and l2 != None:
            curr_val = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
        elif l1 == None:
            curr_val = l2.val + carry
            l2 = l2.next
        elif l2 == None:
            curr_val = l1.val + carry
            l1 = l1.next
        carry = curr_val / 10
        curr_val = curr_val % 10
        ans_list = ListNode(curr_val)
        if count == 1:
            ans_list.next = None
            count -= 1
        else:
            ans_list.next = my_ans
        my_ans = ans_list
    if carry:
        temp_node = ListNode(carry)
        temp_node.next = my_ans
        my_ans = temp_node
    reverse = reversed(my_ans)
    return reverse

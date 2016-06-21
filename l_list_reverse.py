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

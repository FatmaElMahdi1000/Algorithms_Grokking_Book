"""Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1

we need to traverse every element in the singly linked, use reverse, I can work on a copy 
explanation of reversing: 

"""
class ListNode(object):
    def __init__(self, val=0, next=None): 
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self):
        self.head = ListNode()  # dummy head

    def append(self, data):
        new_node = ListNode(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def Length(self):
        cur_node = self.head.next
        list_length = 0
        while cur_node is not None:
            list_length += 1
            cur_node = cur_node.next
        return list_length

    def display(self):
        elements = []
        cur_node = self.head.next  # skip dummy head
        while cur_node is not None:
            elements.append(cur_node.val)
            cur_node = cur_node.next
        print(elements)

    def get(self, index):
        if index >= self.Length():
            print("ERROR: Index is out of range!")
            return None
        cur_node = self.head.next
        cur_index = 0
        while cur_node is not None:
            if cur_index == index:
                return cur_node.val
            cur_node = cur_node.next
            cur_index += 1

    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev  # new head of reversed list

# Instantiate the list
List_data = Solution()
List_data.append(1)
List_data.append(3)
List_data.append(5)
List_data.append(6)
List_data.append(3)

# Display original list
print("Original list:")
List_data.display()

# Reverse the list using reverseList()
new_head = List_data.reverseList(List_data.head.next)  # pass first actual node

# Update internal head pointer to new reversed list
List_data.head.next = new_head

# Display reversed list
print("Reversed list:")
List_data.display()


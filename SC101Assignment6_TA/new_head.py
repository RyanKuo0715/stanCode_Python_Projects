"""
File: new_head.py
Name: Ryan Kuo
------------------------
reorder a linked list with nodes whose value smaller than a certain integer moved backward
and whose value equal or larger move forward
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    dummy_s, dummy_b = ListNode(), ListNode()
    cur, cur_s, cur_b = head, dummy_s, dummy_b
    while cur:
        if cur.val < x:
            cur_s.next = ListNode(cur.val)  # or cur_s.next = cur
            cur_s = cur_s.next
        else:
            cur_b.next = ListNode(cur.val)  # or cur_b.next = cur
            cur_b = cur_b.next
        cur = cur.next
    cur_s.next = dummy_b.next
    # if cur_b.next is not None:
    #     cur_b.next = None
    return dummy_s.next


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1, 8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()

# 定义单链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ----------------------任务1：迭代反转单链表----------------------
def reverse_list(head: ListNode) -> ListNode:
    """
    迭代法反转单链表
    :param head: 原链表头节点
    :return: 反转后的链表头节点
    """
    prev = None
    curr = head
    while curr is not None:
        # 保存下一个节点
        next_temp = curr.next
        # 反转当前节点指向
        curr.next = prev
        # prev和curr向后移动
        prev = curr
        curr = next_temp
    return prev


# ----------------------任务2：合并两个非递减有序单链表----------------------
def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    合并两个非递减有序单链表，合并后依然保持有序
    :param list1: 链表1头节点
    :param list2: 链表2头节点
    :return: 合并后新链表头节点
    """
    # 哑节点，方便操作
    dummy = ListNode()
    cur = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    # 把剩下的直接接上
    if list1 is not None:
        cur.next = list1
    else:
        cur.next = list2
    return dummy.next


# ----------------------任务3：检测链表是否有环（快慢指针）----------------------
def has_cycle(head: ListNode) -> bool:
    """
    判断单链表是否存在环，快慢指针法
    :param head: 链表头节点
    :return: True有环 / False无环
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next        # 慢指针走1步
        fast = fast.next.next   # 快指针走2步
        if slow == fast:
            return True
    return False


# ===================== 辅助工具函数：方便打印链表（测试用）=====================
def print_linked_list(head: ListNode):
    """打印链表的值"""
    res = []
    cur = head
    while cur:
        res.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(res))


# ===================== 测试代码 =====================
if __name__ == "__main__":
    # ===== 测试1：反转链表 =====
    print("=====任务1 迭代反转单链表测试=====")
    # 构建链表：1 -> 2 -> 3 -> 4 ->5
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print("原链表：", end="")
    print_linked_list(n1)
    reversed_head = reverse_list(n1)
    print("反转后：", end="")
    print_linked_list(reversed_head)

    # ===== 测试2：合并两个有序链表 =====
    print("\n=====任务2 合并两个非递减链表测试=====")
    # list1: 1->3->5
    l1_1 = ListNode(1)
    l1_2 = ListNode(3)
    l1_3 = ListNode(5)
    l1_1.next = l1_2
    l1_2.next = l1_3
    # list2:2->4->6
    l2_1 = ListNode(2)
    l2_2 = ListNode(4)
    l2_3 = ListNode(6)
    l2_1.next = l2_2
    l2_2.next = l2_3
    print("链表1：", end="")
    print_linked_list(l1_1)
    print("链表2：", end="")
    print_linked_list(l2_1)
    merged = merge_two_lists(l1_1, l2_1)
    print("合并结果：", end="")
    print_linked_list(merged)

    # ===== 测试3：检测链表环 =====
    print("\n=====任务3 链表环检测测试=====")
    # 无环链表
    a1 = ListNode(10)
    a2 = ListNode(20)
    a3 = ListNode(30)
    a1.next = a2
    a2.next = a3
    print(f"无环链表检测结果：{has_cycle(a1)}")
    # 构造有环链表：1->2->3->2
    b1 = ListNode(1)
    b2 = ListNode(2)
    b3 = ListNode(3)
    b1.next = b2
    b2.next = b3
    b3.next = b2  # 环！3指向2
    print(f"有环链表检测结果：{has_cycle(b1)}")

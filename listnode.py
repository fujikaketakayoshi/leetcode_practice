class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 値が1のノードを作成
node1 = ListNode(1)

# 値が2のノードを作成
node2 = ListNode(2)

# 値が3のノードを作成
node3 = ListNode(3)

node1.next = node2
#node2.next = node3

# 先頭のノードを変数に保持
current = node1

# currentがNoneになるまでループを続ける
while current:
    # 現在のノードのval（値）を出力
    print(current.val)
    # 次のノードに進む
    current = current.next

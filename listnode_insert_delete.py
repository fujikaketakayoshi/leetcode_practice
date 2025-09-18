# 単方向リストのノード定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Pythonリスト → ListNode に変換
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

# ListNode → Pythonリスト に変換（確認用）
def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

#挿入（例: 値 99 を「3の後」に挿入）
head = build_linked_list([1,2,3,4,5])

current = head
while current and current.val != 3:  # 3を探す
    current = current.next

if current:  # 見つかったら挿入
    new_node = ListNode(99, current.next)
    current.next = new_node

print(to_list(head))  # [1, 2, 3, 99, 4, 5]


#削除（例: 値 3 を削除）
head = build_linked_list([1,2,3,4,5])

dummy = ListNode(0, head)
current = dummy
while current.next and current.next.val != 3:  # 3を探す
    current = current.next

if current.next:  # 見つかったら削除
    current.next = current.next.next

head = dummy.next
print(to_list(head))  # [1, 2, 4, 5]


#先頭に挿入（例: 値 99 を先頭に追加）
head = build_linked_list([1,2,3,4,5])

new_node = ListNode(99, head)
head = new_node

print(to_list(head))  # [99, 1, 2, 3, 4, 5]


#末尾に挿入（例: 値 99 を末尾に追加）
head = build_linked_list([1,2,3,4,5])
current = head
while current.next:  # 末尾まで進む
    current = current.next
current.next = ListNode(99)  # 末尾に追加
print(to_list(head))  # [1, 2, 3, 4, 5, 99]

#末尾を削除（例: 末尾の値を削除）
head = build_linked_list([1,2,3,4,5])
dummy = ListNode(0, head)
current = dummy
while current.next and current.next.next:  # 末尾の一つ前まで進
    current = current.next
if current.next:  # 末尾が存在すれば削除
    current.next = None
head = dummy.next
print(to_list(head))  # [1, 2, 3, 4]

#先頭を削除（例: 先頭の値を削除）
head = build_linked_list([1,2,3,4,5])
head = head.next  # 先頭を削除
print(to_list(head))  # [2, 3, 4, 5]
# 空リストに挿入（例: 空リストに値 1 を追加）
head = None
new_node = ListNode(1)
head = new_node
print(to_list(head))  # [1]
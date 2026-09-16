from collections import deque
class Node:
    __slots__ = ['key', 'left', 'right', 'height']

    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, n):
        return n.height if n else 0

    def _balance(self, n):
        return self._height(n.left) - self._height(n.right) if n else 0

    def _update_h(self, n):
        if n:
            n.height = 1 + max(self._height(n.left), self._height(n.right))

    def _rotate_right(self, y):
        x, T2 = y.left, y.left.right
        x.right, y.left = y, T2
        self._update_h(y)
        self._update_h(x)
        return x

    def _rotate_left(self, x):
        y, T2 = x.right, x.right.left
        y.left, x.right = x, T2
        self._update_h(x)
        self._update_h(y)
        return y

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        else:
            print(f"Число {key} уже есть в дереве.")
            return node

        self._update_h(node)
        balance = self._balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def print_tree(self):
        if not self.root:
            print("Дерево пусто.\n")
            return

        print("\nAVL Дерево ")

        def in_order(n):
            if n:
                in_order(n.left)
                print(f"{n.key}")
                in_order(n.right)

        print("Сортировка по порядку: ")
        in_order(self.root)
        print()

        print("\nСтруктура по уровням:")
        q = deque([(self.root, 0)])
        while q:
            n, lvl = q.popleft()
            if n:
                b = self._balance(n)
                print(f"  Уровень {lvl}: Значение {n.key} : Балансировка: {b}")
                q.append((n.left, lvl + 1))
                q.append((n.right, lvl + 1))
        print()

if __name__ == "__main__":
    tree = AVLTree()
    print("AVL-Дерево")
    print("Введите число или 'exit' или 'stop' для выхода.")
    while True:
        val = input().strip()
        if val.lower() in ('exit', 'stop'):
            break

        try:
            f_val = float(val)
            if f_val.is_integer():
                int_val = int(f_val)
                tree.insert(int_val)
                tree.print_tree()
            else:

                print("Ошибка: Для ввода нужны целые числа.")

        except ValueError:
            print("Ошибка: Введите число.")
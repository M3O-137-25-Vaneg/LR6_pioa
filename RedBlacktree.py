from collections import deque

class RedBlackNode:
    __slots__ = ['value', 'color', 'parent', 'left', 'right']

    def __init__(self, value=None, color="red", parent=None, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL = RedBlackNode(color="black")
        self.root = self.NIL

    def insert(self, value):
        if self._search(value):
            print(f" Значение {value} уже существует в дереве")
            return

        new_node = RedBlackNode(value=value, color="red", left=self.NIL, right=self.NIL)

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "black"
            return

        self.fix_insert(new_node)

    def _search(self, value):
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def in_order_traversal(self, node):
        if node != self.NIL:
            self.in_order_traversal(node.left)
            print(f"{node.value}({node.color[0]})", end=" ")
            self.in_order_traversal(node.right)

    def level_order_traversal(self):
        if self.root == self.NIL:
            print(" Дерево пустое.")
            return
        queue = deque([(self.root, 0)])
        while queue:
            node, level = queue.popleft()
            if node != self.NIL:
                color_name = "Красный" if node.color == "red" else "Черный"
                print(f"  [Уровень {level}] Значение: {node.value}, Цвет: {color_name}")
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

    def print_tree_info(self):
        print("\n-----Состояние дерева ------")
        print("Сортированный порядок (In-Order):")
        self.in_order_traversal(self.root)
        print("\n\nСтруктура по уровням:")
        self.level_order_traversal()


def main():
    rb_tree = RedBlackTree()
    print(" Красно-Черное Дерево")
    print("Введите число для добавления в дерево.")
    print("Введите stop или exit для выхода.\n")

    while True:
        user_input = input("Введите значение: ").strip()
        if user_input.lower() in ['stop', 'exit']:
            break
        try:
            value = float(user_input)
            if value.is_integer():
                value = int(value)

            rb_tree.insert(value)
            rb_tree.print_tree_info()
        except ValueError:
            print("Ошибка: введите корректное число.\n")
if __name__ == "__main__":
    main()
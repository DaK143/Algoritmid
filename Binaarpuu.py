class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if current.key == key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, current):
        result = []
        if current:
            result += self._inorder(current.left)
            result.append(current.key)
            result += self._inorder(current.right)
        return result

# Näide kasutamisest
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [50, 30, 70, 20, 40, 60, 80]

    for el in elements:
        tree.insert(el)

    print("Inorder läbimine:", tree.inorder())
    print("Otsing 40:", tree.search(40))
    print("Otsing 90:", tree.search(90))

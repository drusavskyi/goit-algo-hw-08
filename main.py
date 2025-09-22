import heapq
from typing import Optional, List

# --- Класи для Завдання 1 та 2 ---
class Node:
    """Клас для представлення вузла дерева."""
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class BinarySearchTree:
    """Клас для представлення двійкового дерева пошуку."""
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        """Вставка нового елемента в дерево."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node: Node, key: int) -> None:
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    # Завдання 1: Найменше значення
    def find_min(self) -> Optional[int]:
        """Знаходить найменше значення у двійковому дереві пошуку."""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    # Завдання 2: Сума всіх значень
    def find_sum(self) -> int:
        """Знаходить суму всіх значень у двійковому дереві."""
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return node.key + self._sum_recursive(node.left) + self._sum_recursive(node.right)

# --- Функція для Завдання 3 ---
def min_cost_to_connect_cables(cables: List[int]) -> int:
    """
    Обчислює мінімальні витрати на з'єднання кабелів.
    Використовує min-heap.
    """
    if not cables:
        return 0
    if len(cables) == 1:
        return 0

    h = list(cables)  # копія, щоб не змінювати вихідний список
    heapq.heapify(h)
    total_cost = 0
    
    while len(h) > 1:
        cable1 = heapq.heappop(h)
        cable2 = heapq.heappop(h)
        cost = cable1 + cable2
        total_cost += cost
        heapq.heappush(h, cost)
        
    return total_cost

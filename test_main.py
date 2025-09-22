# test_main.py
from main import BinarySearchTree, min_cost_to_connect_cables

def run_tests():
    """
    Запускає автотести для перевірки функцій.
    """
    print("--- Запуск автотестів ---")
    
    # Тест для Завдання 1: find_min
    bst_test = BinarySearchTree()
    test_elements = [50, 30, 70, 20, 40, 60, 80, 25, 75]
    for el in test_elements:
        bst_test.insert(el)
    
    min_value = bst_test.find_min()
    assert min_value == 20, f"Тест find_min не пройшов: очікується 20, отримано {min_value}"
    print("✅ Тест для find_min пройшов успішно.")

    # Тест для Завдання 2: find_sum
    total_sum = bst_test.find_sum()
    assert total_sum == 450, f"Тест find_sum не пройшов: очікується 450, отримано {total_sum}"
    print("✅ Тест для find_sum пройшов успішно.")

    # Тест для Завдання 3: min_cost_to_connect_cables
    cables_test = [4, 3, 2, 6]
    cost = min_cost_to_connect_cables(cables_test)
    assert cost == 29, f"Тест min_cost_to_connect_cables не пройшов: очікується 29, отримано {cost}"
    print("✅ Тест для min_cost_to_connect_cables пройшов успішно.")
    
    # Додатковий тест для Завдання 3
    cables_test_2 = [1, 2, 3]
    cost_2 = min_cost_to_connect_cables(cables_test_2)
    assert cost_2 == 9, f"Додатковий тест не пройшов: очікується 9, отримано {cost_2}"
    print("✅ Додатковий тест пройшов успішно.")
    
    # Edge cases
    assert min_cost_to_connect_cables([]) == 0, "Порожній список кабелів повинен давати 0"
    assert min_cost_to_connect_cables([5]) == 0, "Один кабель повинен давати 0"
    print("✅ Edge cases для min_cost_to_connect_cables пройшли успішно.")

    bst_empty = BinarySearchTree()
    assert bst_empty.find_min() is None, "Порожнє дерево повинно повертати None"
    assert bst_empty.find_sum() == 0, "Сума порожнього дерева повинна дорівнювати 0"
    print("✅ Edge cases для дерева пройшли успішно.")
    
    print("--- Усі тести успішно пройшли! ---")

if __name__ == "__main__":
    run_tests()

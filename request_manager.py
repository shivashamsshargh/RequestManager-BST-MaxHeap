class BSTNode:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority
        self.left = None
        self.right = None


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertHeap(self, id, priority):
        self.heap.append((priority, id))
        self._heapify_up(len(self.heap) - 1)

    def deleteMaxHeap(self):
        if self.isEmptyHeap():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.maxHeapify(0)
        return max_item

    def processHighestPriorityRequest(self, bst_root):
        if self.isEmptyHeap():
            print("MaxHeap is empty.")
            return bst_root
        priority, id = self.deleteMaxHeap()
        node = searchRequest(bst_root, id)
        if node:
            print(f"Processed request with ID {id}, Name {node.name} and Priority {priority}")
        else:
            print(f"Processed request with ID {id} and Priority {priority}")
        bst_root = deleteRequest(bst_root, id)
        return bst_root

    def printMaxHeap(self):
        print("MaxHeap:", self.heap)

    def maxHeapify(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.maxHeapify(largest)

    def increasePriority(self, id, newPriority):
        found = False
        for i in range(len(self.heap)):
            if self.heap[i][1] == id:
                self.heap[i] = (newPriority, id)
                self._heapify_up(i)
                self.maxHeapify(i)
                found = True
                break
        if not found:
            print("ID not found in MaxHeap.")

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def isEmptyHeap(self):
        return len(self.heap) == 0

    def sizeMaxHeap(self):
        return len(self.heap)


def insertRequest(root, id, name, priority):
    if root is None:
        return BSTNode(id, name, priority)
    elif id < root.id:
        root.left = insertRequest(root.left, id, name, priority)
    elif id > root.id:
        root.right = insertRequest(root.right, id, name, priority)
    else:
        print("Duplicate ID not allowed in BST.")
    return root


def searchRequest(root, id):
    if root is None or root.id == id:
        return root
    elif id < root.id:
        return searchRequest(root.left, id)
    else:
        return searchRequest(root.right, id)


def deleteRequest(root, id):
    if root is None:
        return root
    if id < root.id:
        root.left = deleteRequest(root.left, id)
    elif id > root.id:
        root.right = deleteRequest(root.right, id)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = findMinValueNode(root.right)
        root.id = temp.id
        root.name = temp.name
        root.priority = temp.priority
        root.right = deleteRequest(root.right, temp.id)
    return root


def findMinValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def printBST(root):
    if root:
        printBST(root.left)
        print(f"ID: {root.id}, Name: {root.name}, Priority: {root.priority}")
        printBST(root.right)


def isEmptyBST(root):
    return root is None


def sizeBST(root):
    if root is None:
        return 0
    return 1 + sizeBST(root.left) + sizeBST(root.right)


def get_unique_id_input(bst_root):
    while True:
        try:
            id = int(input("Enter unique ID: "))
            if searchRequest(bst_root, id):
                print("ID already exists. Try again.")
            else:
                return id
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_id_input():
    try:
        return int(input("Enter ID: "))
    except ValueError:
        print("Invalid ID.")
        return None


def main():
    bst_root = None
    max_heap = MaxHeap()

    while True:
        print("\n1. Add Request")
        print("2. Delete Request")
        print("3. Search Request")
        print("4. Print BST (Inorder)")
        print("5. Print MaxHeap")
        print("6. Process Highest Priority Request")
        print("7. Increase Priority")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = get_unique_id_input(bst_root)
            name = input("Enter name: ")
            try:
                priority = int(input("Enter priority: "))
            except ValueError:
                print("Invalid priority. Must be an integer.")
                continue
            bst_root = insertRequest(bst_root, id, name, priority)
            max_heap.insertHeap(id, priority)

        elif choice == '2':
            id = get_id_input()
            if id is None:
                continue
            if searchRequest(bst_root, id) is None:
                print("ID not found in BST.")
                continue
            bst_root = deleteRequest(bst_root, id)
            max_heap.heap = [item for item in max_heap.heap if item[1] != id]
            for i in range(len(max_heap.heap)//2, -1, -1):
                max_heap.maxHeapify(i)

        elif choice == '3':
            id = get_id_input()
            if id is None:
                continue
            result = searchRequest(bst_root, id)
            if result:
                print(f"Found - ID: {result.id}, Name: {result.name}, Priority: {result.priority}")
            else:
                print("Request not found.")

        elif choice == '4':
            print("BST (Inorder Traversal):")
            printBST(bst_root)

        elif choice == '5':
            max_heap.printMaxHeap()

        elif choice == '6':
            bst_root = max_heap.processHighestPriorityRequest(bst_root)

        elif choice == '7':
            id = get_id_input()
            if id is None:
                continue
            try:
                new_priority = int(input("Enter new priority: "))
            except ValueError:
                print("Invalid priority.")
                continue
            max_heap.increasePriority(id, new_priority)
            node = searchRequest(bst_root, id)
            if node:
                node.priority = new_priority

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select from the menu.")


if __name__ == "__main__":
    main()

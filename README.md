# 📋 Request Manager with BST & MaxHeap

A command-line based **Request Management System** built with Python that utilizes a **Binary Search Tree (BST)** for storing requests and a **MaxHeap** for prioritizing them. Designed for performance, clarity, and modularity — perfect for academic projects or learning data structures in practice.


---


## 👩‍💻 Developer and Course Project

**Developer:** Shiva Shams Shargh

**Course Project:** This project is part of the **Algorithm Design** course by **Dr. Bagheri**.



---

## 🚀 Features

- 📌 **Add Requests**  
  Add new requests with a unique ID, name, and priority.

- 🔍 **Search Requests**  
  Quickly search for any request by ID using BST.

- 🗑️ **Delete Requests**  
  Remove requests from both the BST and the MaxHeap.

- ⚡ **Process Highest Priority Request**  
  Process and remove the most important request using MaxHeap logic.

- 🔁 **Increase Priority**  
  Dynamically update a request's priority and re-balance the heap.

- 🌳 **Print BST (Inorder Traversal)**  
  View all requests sorted by their ID.

- 📈 **View MaxHeap**  
  Get a raw view of the internal MaxHeap structure.

- ✅ **Input Validation**  
  Ensures unique IDs and safe user inputs.

---

## 🛠️ Data Structures Used

### 🔹 Binary Search Tree (BST)
- Stores: `ID`, `Name`, `Priority`
- Enables: Efficient insertion, search, deletion
- Sorted output via **inorder traversal**

### 🔸 MaxHeap
- Stores: `Priority`, `ID`
- Enables: Fast access to the highest-priority request
- Maintains heap structure automatically after insert/update

---

## 📦 How to Run

```bash
python3 request_manager.py

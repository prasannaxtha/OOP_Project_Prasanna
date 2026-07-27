# 🛒 Supermarket Billing System

## 📌 Project Description

The Supermarket Billing System is a Python console-based application developed using Object-Oriented Programming (OOP) principles. It allows users to manage products, add items to a shopping cart, and generate bills with automatic discount and VAT calculations.

This project demonstrates the practical implementation of OOP concepts such as abstraction, inheritance, encapsulation, and polymorphism while also using JSON for persistent data storage.

---

## 🎯 Objectives

- Implement Object-Oriented Programming concepts in Python.
- Perform product management operations.
- Generate bills automatically.
- Store product data permanently using JSON files.
- Handle invalid user inputs using exception handling.

---

## ✨ Features

- Add new products
- View available products
- Add products to the shopping cart
- Generate bills automatically
- Apply discounts and VAT calculations
- Save product information in a JSON file
- Handle exceptions for invalid inputs

---

## 🧠 OOP Concepts Used

### 1. Abstraction
An abstract `Item` class is used to define a common structure for items.

### 2. Inheritance
The `Product` class inherits from the `Item` class.

### 3. Encapsulation
Product attributes are kept private using double underscores (`__`).

### 4. Polymorphism
The `display()` method is implemented differently in the `Product` class.

---

## 📂 Project Structure

```
Supermarket-Billing-System/
│
├── main.py
├── supermarket.py
├── product.py
├── item.py
├── products.json
```

---

## ⚙️ Technologies Used

- Python
- JSON
- Object-Oriented Programming (OOP)

---

## 🚀 How to Run the Project

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Run the following command:

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Add Product
2. View Products
3. Add To Cart
4. Generate Bill
5. Exit
```

---

## 💳 Billing System

- Orders above **Rs. 5000** receive a **10% discount**.
- After discount calculation, **13% VAT** is added.
- The final bill displays subtotal, discount, VAT, and total amount.

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

- Classes and Objects
- Inheritance
- Abstraction
- Encapsulation
- Polymorphism
- File Handling
- JSON Data Storage
- Exception Handling
- Modular Programming

---

## 👨‍💻 Developed By

**Name:** **Prasanna Shrestha**

**Course:** **Object Oriented Programming**

**Semester:** **Second**

**Submitted To:** **Dr Ashish Gautam**

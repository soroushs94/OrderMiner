## **OrderMiner: A Multi-Dimensional Work Order Classification Tool**

🚀 **OrderMiner** is a PyQt5-based desktop application designed to enhance work order data analysis through a **multi-dimensional classification system**. Unlike traditional classifiers that assign work orders to a single predefined category (e.g., *mechanical* vs. *lighting*), OrderMiner allows users to **filter across multiple dimensions** simultaneously, such as work centers, actions, issues, and systems.

This capability provides a **more nuanced and customizable approach** to querying work order records, making it easier to analyze large datasets dynamically. The interactive interface enables users to:

- **Filter work orders dynamically** based on taxonomy-defined categories.
- **Select key performance indicators (KPIs)** and generate automated reports.
- **Modify filters and regenerate reports**, allowing for an iterative and interactive analysis process.

OrderMiner is an intuitive tool for organizations looking to streamline their work order management and improve operational efficiency through **structured data classification and analysis**.

🔗 **For more details, refer to the official publication:**  
[📄 Read the Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4783740)

---

## **📦 Features**

- **Multi-Dimensional Filtering** – Query work orders across multiple categories like work centers, actions, issues, and systems.
- **Dynamic Taxonomy-Based Categorization** – Assign work orders to relevant categories based on customizable taxonomies.
- **KPI Selection & Reporting** – Generate automated reports based on selected key performance indicators.
- **Interactive Filtering** – Modify filters dynamically and regenerate reports for iterative data analysis.
---

## 🚀 Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/OrderMiner.git
cd OrderMiner
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
```

- On **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---

## 🎮 Usage

### Run the Application

```sh
python -m src.main
```

This command launches the PyQt5 application.

---

## 📂 Project Structure

```
/OrderMiner
│── /src
│   │── /ui
│   │   │── UI.py
│   │   │── ui_functions.py
│   │── /modules
│   │   │── Taxonomy.py
│   │   │── dialog.py
│   │   │── work_order_categorizer.py
│   │── main.py
│── /data
│   │── 2yrDataLabour.csv
│   │── 2yrWO_cleaned_2_buildings.csv
│── README.md
│── requirements.txt
```

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added a new feature"`).
4. Push to your branch (`git push origin feature-branch`).
5. Create a Pull Request.

---

## 📬 Contact

For questions or collaboration opportunities, feel free to reach out to soroushs96@gmail.com.

---


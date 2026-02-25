# 💰 Personal Finance Tracker

A full-stack **Personal Finance Tracking and Analytics System** built using **FastAPI**, **Streamlit**, and **MySQL**.  
The application allows users to manage daily expenses and visualize spending insights through category-wise and monthly analytics.

---

## 🚀 Features

### ✅ Expense Management
- Add daily expenses
- Update existing expenses
- Delete and replace expenses by date
- Category-based expense recording

### 📊 Category Analytics
- View expense breakdown by category
- Percentage contribution per category
- Date range-based filtering

### 📅 Monthly Analytics
- Select **Year**
- Select **one or multiple months**
- View monthly expense trends
- Interactive bar charts
- Tabular summary view

### 🔐 Backend Validation
- Pydantic models for request validation
- Structured API responses
- Error handling with proper HTTP status codes

---

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: MySQL
- **Data Processing**: Pandas
- **Testing**: Pytest

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Personal-Finance-Tracker.git
cd Personal-Finance-Tracker

````
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```
### 3️⃣ Configure Database

Create a MySQL database

Link database credentials in backend/db_helper.py

**Example:**

```python
host="localhost"
user="root"
password="yourpassword"
database="expense_manager"
```

### 4️⃣ Run FastAPI Backend

```bash
uvicorn backend.server:app --reload --port 9000
```

### 5️⃣ Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

### 🔄 API Endpoints
| Method | Endpoint            | Description                        |
| ------ | ------------------- | ---------------------------------- |
| GET    | `/expenses/{date}`  | Fetch expenses for a specific date |
| POST   | `/expenses/{date}`  | Add or update expenses             |
| POST   | `/analytics/`       | Category-wise analytics            |
| POST   | `/monthly_summary/` | Monthly filtered summary           |






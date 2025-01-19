# Flask SQLAlchemy

Flask-based ORM applications that demonstrates how to manage an app databases using SQLAlchemy ORM. It supports operations such as creating a database, adding initial data, and querying stored records using Flask CLI commands.

---

## **Installation and Setup**

### **1. Clone the Repository:**
```bash
# Clone this repository
git clone https://github.com/your-repository/flask-book-management.git
cd flask-book-management
```

### **2. Create a Virtual Environment (Optional):**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate   # On Windows
```

### **3. Install Dependencies:**
```bash
pip install Flask Flask-SQLAlchemy
```

### **4. Save the Code:**
- Ensure the application code is saved as `app.py`.

---

## **Running the Application**

### **1. Initialize the Database:**
```bash
export FLASK_APP=app_bookstore.py

flask initdb
```

### **2. Populate Initial Data:**
```bash
flask bootstrap
```

### **3. Query the Database:**
```bash
flask query
```

---

## **Technologies Used**
- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (for data storage)
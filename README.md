````markdown
# 🎓 Group Project – Flask + SQLite + Frontend

A collaborative project using **Python (Flask)** for the backend, **SQLite** for the database, and **HTML/CSS/JavaScript** for the frontend.

---

## 📦 Requirements
- Python 3.8+  
- Git  
- (Optional but recommended) Virtual environment support  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <REPO_URL>
cd group-project
````

---

### 2. Create and Activate Virtual Environment

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell)**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Initialize the Database

Run once to create the SQLite database (`instance/app.db`):

```bash
python run.py
```

---

### 5. Run the Application

**Option A: Using Flask CLI**

```bash
flask run
```

**Option B: Using Python**

```bash
python run.py
```

The app will now be running at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔄 Keeping Dependencies Updated

When new Python packages are added, update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 👥 Collaboration Workflow

### Pull the latest changes before starting work

```bash
git pull origin main
```

### After making changes

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### Optional: Working with branches

```bash
git checkout -b feature-branch
git push origin feature-branch
```

---

## 📂 Project Structure (Overview)

```
group-project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── base.html
│       └── index.html
│
├── instance/
│   └── app.db
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Contributing

1. Fork or clone this repo.
2. Create a branch for your changes.
3. Submit a Pull Request for review.
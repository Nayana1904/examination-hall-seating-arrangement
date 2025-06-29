# 🪑 Exam Seating Arrangement System

A web-based application to generate subject-wise and branch-wise seating arrangements for examinations. Admins can input or upload student data, and the system will 
auto-distribute students across rooms to minimize duplication and cheating risk.

---

## 🚀 Features

- 📝 Manual and CSV upload for student data
- 🧠 Auto-arranged seating by branch and subject
- 📄 Dashboard with room-wise seat visualization
- 📤 Export or print-ready format (optional)
- 🔐 Secure login (Flask sessions)

---

## 🛠️ Tech Stack

| Component   | Technology       |
|------------|------------------|
| Backend    | Python (Flask)   |
| Frontend   | HTML, CSS        |
| Database   | None or MongoDB (optional) |
| UI Styling | CSS (RGB gradients) |
| Hosting    | Local or Render/Vercel |

---

## 📂 File Structure
project-folder/
├── app.py
├── templates/
│ ├── login.html
│ ├── dashboard.html
│ └── frontpage.html
├── static/
│ └── style.css
├── students.csv (optional)
└── README.md

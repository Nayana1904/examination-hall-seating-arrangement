from flask import Flask, render_template, request, redirect, url_for, session
from collections import defaultdict
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load users
with open('users.json') as f:
    users = json.load(f)

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and users[uname] == pwd:
            session['user'] = uname
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = {}
    if request.method == 'POST':
        data = request.form.get('students')
        rooms = {"Room A": (3, 3), "Room B": (2, 3)}
        students = []
        for line in data.strip().split('\n'):
            parts = line.strip().split(',')
            if len(parts) == 4:
                roll, name, branch, subject = map(str.strip, parts)
                students.append({"roll": roll, "name": name, "branch": branch, "subject": subject})

        grouped = defaultdict(list)
        for student in students:
            key = f"{student['branch']}_{student['subject']}"
            grouped[key].append(student)

        mixed_students = []
        group_keys = list(grouped.keys())
        i = 0
        while any(grouped.values()):
            key = group_keys[i % len(group_keys)]
            if grouped[key]:
                mixed_students.append(grouped[key].pop(0))
            i += 1

        seating = defaultdict(list)
        student_index = 0
        for room, (rows, cols) in rooms.items():
            for r in range(rows):
                row = []
                for c in range(cols):
                    if student_index < len(mixed_students):
                        s = mixed_students[student_index]
                        row.append(f"{s['roll']} ({s['branch']}-{s['subject']})")
                        student_index += 1
                    else:
                        row.append("Empty")
                seating[room].append(row)
        result = seating

    return render_template('dashboard.html', result=result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('front'))

if __name__ == '__main__':
    app.run(debug=True)

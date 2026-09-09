from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def login_page():
    if 'user_id' in session:
        return redirect(url_for('instruction'))
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll = request.form['roll']
    email = request.form['email']
    password = request.form['password']

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, roll, email, password) VALUES (?, ?, ?, ?)",
                       (name, roll, email, password))
        conn.commit()
        flash("Registration successful! Please login.", "success")
    except sqlite3.IntegrityError:
        flash("Email already exists. Try another.", "error")
    finally:
        conn.close()

    return redirect(url_for('login_page'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        session['user_id'] = user['id']
        session['name'] = user['name']
        session['roll'] = user['roll']
        session['email'] = user['email']
        return redirect(url_for('instruction'))
    else:
        flash("Invalid email or password. Please try again.", "error")
        return redirect(url_for('login_page'))

@app.route('/instruction')
def instruction():
    if 'user_id' not in session:
        flash("Please login first.", "error")
        return redirect(url_for('login_page'))
    return render_template('instruction.html')

# Keep only this quiz route, remove the duplicate one
@app.route('/quiz')
def quiz():
    if 'user_id' not in session:
        flash("Please login first to take the quiz.", "error")
        return redirect(url_for('login_page'))

    questions = [
        {
            "text": "Q1. Which of the following is a primary key?",
            "options": [
                "A key that can take NULL values",
                "A key that uniquely identifies each record in a table",
                "A key used to connect two tables",
                "A key used for sorting"
            ],
            "correct": "A key that uniquely identifies each record in a table"
        },
        {
            "text": "Q2. In a relational database, rows are also called:",
            "options": ["Tuples", "Attributes", "Schemas", "Relations"],
            "correct": "Tuples"
        },
        {
            "text": "Q3. Which SQL command is used to remove all records but not the table?",
            "options": ["DROP", "DELETE", "TRUNCATE", "REMOVE"],
            "correct": "TRUNCATE"
        },
        {
            "text": "Q4. What is the output of the following code? <br><br>x = [1, 2, 3]<br>print(x[1])",
            "options": ["1", "2", "3", "Error"],
            "correct": "2"
        },
        {
            "text": "Q5. Which of the following is a mutable data type in Python?",
            "options": ["Tuple", "String", "List", "Integer"],
            "correct": "List"
        },
        {
            "text": "Q6. What is the correct file extension for Python files?",
            "options": [".py", ".pyt", ".pt", ".p"],
            "correct": ".py"
        },
        {
            "text": "Q7. Which of the following is a linear data structure?",
            "options": ["Graph", "Tree", "Array", "Binary Tree"],
            "correct": "Array"
        },
        {
            "text": "Q8. In a stack, insertion and deletion are performed at:",
            "options": ["Front", "Rear", "Both ends", "Top"],
            "correct": "Top"
        },
        {
            "text": "Q9. The time complexity of binary search in a sorted array is:",
            "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
            "correct": "O(log n)"
        },
        {
            "text": "Q10. A queue follows which principle?",
            "options": ["LIFO (Last In First Out)", "FIFO (First In First Out)", "FILO (First In Last Out)", "Random order"],
            "correct": "FIFO (First In First Out)"
        }
    ]

    return render_template('quiz.html', questions=questions)

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    if 'user_id' not in session:
        flash("Please login first.", "error")
        return redirect(url_for('login_page'))

    correct_answers = {
        "q0": "A key that uniquely identifies each record in a table",
        "q1": "Tuples",
        "q2": "TRUNCATE",
        "q3": "2",
        "q4": "List",
        "q5": ".py",
        "q6": "Array",
        "q7": "Top",
        "q8": "O(log n)",
        "q9": "FIFO (First In First Out)"
    }

    score = 0
    total = len(correct_answers)

    for qkey, correct in correct_answers.items():
        selected = request.form.get(qkey)
        if selected == correct:
            score += 1

    return render_template('result.html', 
                           score=score, 
                           total=total,
                           name=session.get('name'), 
                           email=session.get('email'), 
                           roll=session.get('roll'))

@app.route('/result')
def result():
    if 'user_id' not in session:
        flash("Please login first.", "error")
        return redirect(url_for('login_page'))
    # Optionally, you can retrieve score from session or pass via redirect
    return render_template('result.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)

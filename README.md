online Quiz Portal

A simple and interactive web-based Quiz Application developed using **Python, Flask, HTML, CSS, and SQLite**. The application provides a user-friendly interface where users can log in, read quiz instructions, attempt questions, and view their final results.

Features

* User Login System
* Quiz Instructions Page
* Interactive Quiz Interface
* Automatic Result Calculation
* Result Display
* SQLite Database for User Data
* Responsive and Simple UI
* Separate HTML templates and CSS styling

Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **SQLite**
* **Jinja2 Templates**

Project Structure

```text
Project/
│
├── index.py              # Main Flask application
├── init_db.py            # Database initialization
├── users.db              # SQLite database
├── sjcem.png             # Project image/logo
│
├── templates/
│   ├── login.html
│   ├── instruction.html
│   ├── quiz.html
│   └── result.html
│
├── static/
│   ├── style.css
│   ├── instruction.css
│   ├── quiz.css
│   └── result.css
│
└── .vscode/
```

How to Run

1. Clone this repository.
2. Install the required Python dependencies.
3. Initialize the database.
4. Run the Flask application.
5. Open the application in your browser.

```bash
python init_db.py
python index.py
```

Then open the local URL provided by Flask in your browser.

Objective

The main objective of this project is to develop a simple and interactive online quiz platform that demonstrates the use of **Python Flask for web development, HTML/CSS for frontend design, and SQLite for database management**.

Future Scope

* Admin dashboard for managing quizzes
* Multiple quiz categories
* Timer-based quizzes
* User performance analytics
* Leaderboard system
* Question randomization
* User registration and authentication
* Deployment on cloud platforms

Project

This project was developed as an academic/project-based application to demonstrate practical implementation of **Python, Web Development, and Database Management** concepts.

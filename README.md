🚀 Project Overview
This project is a Flask-based web application for managing posts with dynamic database and table management functionalities. Users can create, edit, delete, and view posts.

---

 🛠️ Setup Instructions

 Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- PostgreSQL (or any SQL database)

 Installation Steps
1. Clone the Repository:
   bash
   git clone <repository_url>
   cd <project_folder>
   

2. Create and Activate a Virtual Environment:
   bash
   python -m venv venv
   source venv/bin/activate   On Windows: venv\Scripts\activate
   

3. Install Required Packages:
   bash
   pip install -r requirements.txt
   

4. Set Up Environment Variables:
   Create a .env file in the root directory and add the following:
   bash
   FLASK_APP=app.py
   FLASK_DEBUG=True
   

---

 🗄️ Database Configuration

 Using PostgreSQL
1. Install PostgreSQL:  
   [PostgreSQL Installation Guide](https://www.postgresql.org/download/)

2. Create a Database:
   sql
   CREATE DATABASE your_database_name;
   

3. Configure Database in config.py:
   python
   class Config:
       SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/your_database_name'
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   

4. Migrate the Database:
   bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   

---

 📂 Project Structure

project_folder/
│
├── app.py                  Main Flask application
├── config.py               Configuration file
├── models.py               Database models
├── templates/              HTML templates
│   ├── index.html
│   ├── edit_table.html
│   └── databases.html
│
├── static/                 CSS, JavaScript files
│   └── style.css
│
├── migrations/             Database migrations
├── requirements.txt        Python dependencies
└── README.md               Project documentation


---

 🌐 Routes and Functionality

1. Home Page (/):
   - Displays all posts in a table format.
   
2. Add Post (/add):
   - Handles form submission to create new posts.

3. Edit Post (/edit_table/<id>):
   - Retrieves and updates a specific post.

4. Delete Post (/delete_table/<id>):
   - Deletes a specified post.

5. Database Management Page (/database_page):
   - Interface to manage database tables dynamically.

---

 🛠️ Development Procedures

1. Creating a New Post:
   - Navigate to /database_page.
   - Fill in the required fields and submit the form.

2. Editing an Existing Post:
   - Click the Edit button in the post table.
   - Update the fields and save changes.

3. Deleting a Post:
   - Click the Delete button next to the relevant post.

4. Adding Database Migrations:
   bash
   flask db migrate -m "Your message here"
   flask db upgrade
   

5. Testing the Application:
   - Use tools like Postman to test CRUD operations.
   - Verify responses and status codes.

---

 ▶️ Running the Project
1. Start the Flask Application:
   bash
   flask run
   

2. Access the Web App:
   Open your browser and navigate to:
   
   http://127.0.0.1:5000/
  

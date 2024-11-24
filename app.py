from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import datetime

# App initialization
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Added category field
    tags = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publication_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserPost {self.title}>'

# Routes
@app.route('/')
def index():
    posts = UserPost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def newtable():
    title = request.form['title']
    content = request.form['content']
    category = request.form['category']
    tags = request.form['tags']
    author = request.form['author']
    publication_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    
    new_post = UserPost(
        title=title,
        content=content,
        category=category,
        tags=tags,
        author=author,
        publication_date=publication_date
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_table/<int:id>')
def delete_table(id):
    table_to_delete = UserPost.query.get_or_404(id)
    db.session.delete(table_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/database_page')
def database_page():
    return render_template('databases.html')

@app.route('/edit_table/<int:id>', methods=['GET', 'POST'])
def edit_table(id):
    post = UserPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.category = request.form['category']
        post.tags = request.form['tags']
        post.author = request.form['author']
        post.publication_date = datetime.strptime(request.form['publication_date'], '%Y-%m-%d')
        
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f"There was an issue updating the post: {e}"
    return render_template('edit_table.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)

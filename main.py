from flask import Flask, render_template, url_for, request, flash, redirect, Markup
from operator import itemgetter
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content_preview = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


@app.route('/')
@app.route('/home/')
def index():
	posts = Post.query.order_by(Post.date_posted).all()
	return render_template('index.html', title="Test", posts=posts)


@app.route('/new_post/', methods=['GET', 'POST'])
def new_post():
	if request.method == 'POST':
		post_title = request.form['title']
		post_content = Markup(request.form['content'])
		post_preview = Markup(request.form['content_preview'])
		post_author = request.form['author']
		newpost = Post(title=post_title, content=post_content, author=post_author, content_preview=post_preview) 
		try:
			db.session.add(newpost)
			db.session.commit()
			return redirect('/')
		except Exception as e:
			raise e
	else:
		return render_template('new_post.html')

@app.route('/p/<int:post_id>/')
def p(post_id):
	current_post = Post.query.get(post_id)
	return render_template('post.html', post=current_post)
	


if __name__=='__main__':
	app.run(debug=True)
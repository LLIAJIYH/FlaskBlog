from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		'author': "Bayram Tagiev",
		'nickname': "LLIAJIYH",
		'title': "My first post",
		'content': "Yay, now we have our first post"
	},
	{
		'author': "Artur Adgiev",
		'nickname': "LLIAJIYH",
		'title': "My second post",
		'content': "Yay, now we have our second post"
	},
	{
		'author': "Aram Vagifov",
		'nickname': "LLIAJIYH",
		'title': "My third post",
		'content': "Yay, now we have our third post and we will congratule me for this work"
	}]

@app.route('/')
def index():
	return render_template('index.html', title="Test", posts=posts)

if __name__=='__main__':
	app.run(debug=True)
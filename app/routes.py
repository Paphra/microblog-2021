from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {
		'username': 'Epaphradito',
	}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Suzan'},
			'body': 'The Marvel Studio is so Cool!'
		}
	]

	return render_template('index.html', title="Home", user=user, posts=posts)
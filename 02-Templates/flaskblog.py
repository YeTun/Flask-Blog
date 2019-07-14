# July 14, 2019
# Jinja2

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ye Tun Aung',
        'title': 'Blog Post 1',
        'content': 'JavaScript is pretty cool!',
        'date_posted': 'July 14, 2019'
    },
    {
        'author': 'Thura Ye Tun',
        'title': 'Blog Post 2',
        'content': 'So tired from all that learning!',
        'date_posted': 'July 14, 2019'
    },
    {
        'author': 'Maythansin Ye Tun',
        'title': 'Blog Post 2',
        'content': 'Scratch is so cool!',
        'date_posted': 'July 14, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

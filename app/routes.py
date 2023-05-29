from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'pysdr.org'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'flask.palletsprojects.com'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'wireguard.com'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'certbot.eff.org'
        },
    ]
    return render_template('index.html', title='cyberdeck.ch', posts=posts)

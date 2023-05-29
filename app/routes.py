from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='cyberdeck.ch')

@app.route('/hardware')
def software():
    posts = [
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'PlutoSDR'
        },
         {
            'subject': {'tag': 'cyberdeck'},
            'body': 'GPD MicroPC'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'Raspberry Pi'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'RTL-SDR'
        },
    ]
    return render_template('hardware.html', title='cyberdeck.ch', posts=posts)

@app.route('/software')
def software():
    posts = [
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'pysdr.org'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'gnuradio.org'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'ubuntu-mate.org'
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
    return render_template('software.html', title='cyberdeck.ch', posts=posts)

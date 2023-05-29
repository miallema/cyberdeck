from app import app

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'Check out pysdr.org'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'Check out blog.miguelgrinberg.com'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'Check out wireguard.com'
        },
        {
            'subject': {'tag': 'cyberdeck'},
            'body': 'Check out certbot.eff.org'
        },
    ]
    return render_template('index.html', title='cyberdeck.ch', posts=posts)

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="cyberdeck.ch")


@app.route("/goal")
def goal():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "Amateur radio license"},
        {"subject": {"tag": "cyberdeck"}, "body": "Send bits from PlutoSDR to RTL-SDR"},
        {"subject": {"tag": "cyberdeck"}, "body": "Write transmitted bytes to memory"},
        {"subject": {"tag": "cyberdeck"}, "body": "TCP/IP networking"},
        {"subject": {"tag": "cyberdeck"}, "body": "LTE"},
        {"subject": {"tag": "cyberdeck"}, "body": "Satellite reception"},
        {"subject": {"tag": "cyberdeck"}, "body": "Explore turbo and LDPC codes"},
    ]
    return render_template("goal.html", title="cyberdeck.ch", posts=posts)


@app.route("/personal")
def personal():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "nts.live"},
        {"subject": {"tag": "cyberdeck"}, "body": "Alastair Reynolds"},
    ]
    return render_template("personal.html", title="cyberdeck.ch", posts=posts)


@app.route("/hardware")
def hardware():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "PlutoSDR"},
        {"subject": {"tag": "cyberdeck"}, "body": "GPD MicroPC"},
        {"subject": {"tag": "cyberdeck"}, "body": "Raspberry Pi"},
        {"subject": {"tag": "cyberdeck"}, "body": "RTL-SDR"},
    ]
    return render_template("hardware.html", title="cyberdeck.ch", posts=posts)


@app.route("/software")
def software():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "pysdr.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "gnuradio.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "ubuntu-mate.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "flask.palletsprojects.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "wireguard.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "certbot.eff.org"},
    ]
    return render_template("software.html", title="cyberdeck.ch", posts=posts)

from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="cyberdeck.ch")


@app.route("/goal")
def goal():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "Deploy and test a software radio receiver on PlutoSDR following the textbook 'software receiver design' by Sethares et al. but implementing it in python using pysdr.org."},
        {"subject": {"tag": "cyberdeck"}, "body": "Build tranceiver using GNU Radio."},
        {"subject": {"tag": "cyberdeck"}, "body": "Interact with LTE network."},
    ]
    return render_template("goal.html", title="cyberdeck.ch", posts=posts)


@app.route("/personal")
def personal():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "nts.live"},
        {"subject": {"tag": "cyberdeck"}, "body": "interzone.press"},
        {"subject": {"tag": "cyberdeck"}, "body": "monde-diplomatique.fr"},
    ]
    return render_template("personal.html", title="cyberdeck.ch", posts=posts)


@app.route("/hardware")
def hardware():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "PlutoSDR"},
        {"subject": {"tag": "cyberdeck"}, "body": "GPD MicroPC"},
        {"subject": {"tag": "cyberdeck"}, "body": "Raspberry Pi"},
        {"subject": {"tag": "cyberdeck"}, "body": "RTL-SDR"},
        {"subject": {"tag": "cyberdeck"}, "body": "Swisscom Internet-Box 3"},
    ]
    return render_template("hardware.html", title="cyberdeck.ch", posts=posts)


@app.route("/software")
def software():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "gnuradio.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "ubuntu-mate.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "flask.palletsprojects.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "wireguard.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "certbot.eff.org"},
        {"subject": {"tag": "cyberdeck"}, "body": "pi-hole.net"},
    ]
    return render_template("software.html", title="cyberdeck.ch", posts=posts)


@app.route("/services")
def services():
    posts = [
        {"subject": {"tag": "cyberdeck"}, "body": "proton.me"},
        {"subject": {"tag": "cyberdeck"}, "body": "infomaniak.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "cloudflare.com"},
        {"subject": {"tag": "cyberdeck"}, "body": "swisscom.ch"},
    ]
    return render_template("services.html", title="cyberdeck.ch", posts=posts)


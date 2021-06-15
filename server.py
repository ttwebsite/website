import requests
import datetime
from datetime import datetime
from flask import Flask, redirect, render_template
from flask.helpers import url_for

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("home.html")

# Server information
@app.route("/serverinformation")
def lite():
    return render_template("si_home.html")

# Server information: LITE
@app.route("/serverinformation/lite")
def si_lite():
    headers_request = {'User-Agent': 'Quinns Website'}
    userlist_request = requests.get('https://servers-frontend.fivem.net/api/servers/single/dgpvx3', headers=headers_request).json()
    tcount = str(userlist_request['Data']['clients']) + "/" + str(userlist_request['Data']['vars']['sv_maxClients'])
    uptime = userlist_request['Data']['vars']['Uptime']
    dateandtime = datetime.utcnow()
    currenttimed = dateandtime.strftime("%a %d %b %Y - %H:%M:%S")
    players = ""
    players = []
    for i in userlist_request['Data']['players']:
        players.append(f"{i['name']} ({i['ping']}ms)")
    players = '<br>'.join(players)
    return render_template("si_lite.html", tcount=tcount, uptime=uptime, players=players, currenttimed=currenttimed)

# About the creator
@app.route("/aboutthecreator")
def atc():
    return render_template("atc_h.html")

# If page does NOT exist!
@app.route("/<name>")
def user(name):
    return render_template("nonexistent.html", content=name)

# Rick Roll :heh:
@app.route("/rickroll")
def rickroll():
    return render_template("rickroll.html")

if __name__ == "__main__":
    app.run() 
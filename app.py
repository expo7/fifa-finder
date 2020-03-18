from flask import Flask,request,redirect,url_for,render_template
from form import PlayerForm
from flask_bootstrap import Bootstrap
from utils import get_player_attributes

app = Flask(__name__)
Bootstrap(app)
app.secret_key="pass"

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method=='POST'):
        return redirect(url_for('player', name=request.form["player"]))
    return render_template('home.html')

@app.route('/<name>')
def player(name):
    attributes = get_player_attributes(playername=name)
    return render_template('player.html', attributes=attributes)

if __name__=="__main__":
    app.run(debug=True)
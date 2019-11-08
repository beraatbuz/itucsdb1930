from flask import Flask,render_template,request,redirect,url_for,flash,abort,session
from flask_login import LoginManager,login_user,current_user,login_required,logout_user
from user import get_user
from wtforms import Form, BooleanField, StringField, validators,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from passlib.hash import pbkdf2_sha256 as hasher
import forms
lm = LoginManager()

@lm.user_loader
def load_user(user_id):
    return get_user(user_id)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisisSecret'
app.config.from_object("settings")
@app.route("/")
def home_page():
     logout_user()
     return render_template("home.html")

@app.route("/dashboard")
@login_required
def dashboard_page():
     if not current_user.is_admin:
        abort(401)
     return render_template("dashboard.html")
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

@app.route("/login",methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.is_submitted(): 
        username = form.data["username"]
        user = get_user(username)
        if user is not None: 
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("You have logged in.")#
                next_page = request.args.get("next", url_for("dashboard_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
        #abort(401)
    return render_template("login.html", form=form)
@app.route("/")
def logout_page():
    print("1")
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))
lm.init_app(app)
lm.login_view = "login_page"

@app.route("/add_team", methods=['GET','POST'])
@login_required
def team_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_team.html')

    elif request.method == 'POST':
        team_name = str(request.form["team_name"])
        NickName = str(request.form["team_name"])
        ShortName = str(request.form["team_name"])
        FoundationDate = str(request.form["team_name"])
        Capacity =  str(request.form["team_name"])
        ManagerID =  str(request.form["team_name"])
        obje = forms.FootballStats()
        obje.Team_add(team_name,NickName,ShortName,FoundationDate,Capacity,ManagerID)
        flash("You have added.")
        return render_template("add_team.html")

@app.route("/team", methods=['GET','POST'])
def teams_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Team()
        print(cursor)
        return render_template("teams.html",cursor=cursor)
    else:
        obje = forms.FootballStats()
        form_team_keys = request.form.getlist("ID")
        for form_team_key in range(len(form_team_keys)):
            obje.Team_delete(int(form_team_key))
        flash("You have deleted.")
        return redirect(url_for("teams_page"))

@app.route("/stadium", methods=['GET','POST'])
def stadium_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Stadium()
        print(cursor)
        return render_template("stadium.html",cursor=cursor)

@app.route("/assist", methods=['GET','POST'])
def assist_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Assist()
        print(cursor)
        return render_template("assist.html",cursor=cursor)

@app.route("/statistic", methods=['GET','POST'])
def statistic_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Statistic()
        print(cursor)
        return render_template("statistic.html",cursor=cursor)
    

@app.route("/add_player", methods=['GET','POST'])
@login_required
def player_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_player.html')

    elif request.method == 'POST':
        PlayerName = str(request.form["PlayerName"])
        PlayerAge = str(request.form["PlayerAge"])
        PlayerNationalty = str(request.form["PlayerNationalty"])
        PlayerHeight = str(request.form["PlayerHeight"])
        PlaceOfBirth = str(request.form["PlaceOfBirth"])
        TeamID = str(request.form["TeamID"])
        obje = forms.FootballStats()
        obje.Player_add(PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID)
        flash("You have added.")
        return render_template("add_player.html")

@app.route("/player", methods=['GET','POST'])
def player_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Player()
        return render_template("players.html",cursor=cursor)
    else:
        obje = forms.FootballStats()
        form_player_keys = request.form.getlist("ID")
        #for form_player_key in form_player_keys:
        obje.Player_delete(form_player_keys)
        flash("You have deleted.")
        return redirect(url_for("player_page"))

@app.route("/add_manager", methods=['GET','POST'])
@login_required
def manager_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_manager.html')

    elif request.method == 'POST':
        Name = str(request.form["Name"])
        Age = str(request.form["Age"])
        Nationalty = str(request.form["Nationalty"])
        Height = str(request.form["Height"])
        PlaceOfBirth = str(request.form["PlaceOfBirth"])
        TeamID = str(request.form["TeamID"])
        obje = forms.FootballStats()
        obje.Manager_add(Name, Age, Nationalty, Height, PlaceOfBirth, TeamID)
        flash("You have added.")
        return render_template("add_manager.html")

@app.route("/manager")
def manager_page():
    obje = forms.FootballStats()
    cursor=obje.Manager()
    return render_template("managers.html",cursor=cursor)   
    
@app.route("/add_goal", methods=['GET','POST'])
@login_required
def goal_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_goal.html')

    elif request.method == 'POST':
        PlayerID = str(request.form["PlayerID"])
        MatchID = str(request.form["MatchID"])
        Minute = str(request.form["Minute"])
        obje = forms.FootballStats()
        obje.Goal_add(PlayerID, MatchID, Minute)
        flash("You have added.")
        return render_template("add_goal.html")

@app.route("/goal")
def goal_page():
    obje = forms.FootballStats()
    cursor=obje.Goal()
    return render_template("goals.html",cursor=cursor)  
if __name__ == "__main__":
    app.run(debug=True)

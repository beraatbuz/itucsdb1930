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

@app.route("/fixture", methods=['GET','POST'])
def fixture_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Fixtures()
        return render_template("fixture.html",cursor=cursor)
    
@app.route("/standing", methods=['GET','POST'])
def standing_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Standings()
        return render_template("standing.html",cursor=cursor)

@app.route("/referee", methods=['GET','POST'])
def referee_page():
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Referee()
        return render_template("referee.html",cursor=cursor)
    
@app.route("/add_team", methods=['GET','POST'])
@login_required
def team_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_team.html')

    elif request.method == 'POST':
        team_name = str(request.form["team_name"])
        NickName = str(request.form["NickName"])
        ShortName = str(request.form["ShortName"])
        FoundationDate = str(request.form["FoundationDate"])
        Capacity =  str(request.form["Capacity"])
        ManagerID =  str(request.form["ManagerID"])
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
        form_team_keys = request.form.getlist("team_keys")
        for team_key in form_team_keys:
            obje.Team_delete(team_key)
        flash("You have deleted.")
        return redirect(url_for("teams_page"))

@app.route("/stadium", methods=['GET','POST'])
def stadium_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Stadium()
        print(cursor)
        return render_template("stadium.html",cursor=cursor)
    else:
        form_stadium_keys = request.form.getlist('stadium_keys')
        for form_stadium_key in form_stadium_keys:
            obje.Stadium_delete(int(form_stadium_key))
        return redirect(url_for("stadium_page"))

@app.route("/add_stadium", methods=['GET','POST'])
def stadium_add_page():
    if request.method == 'GET':
        return render_template('add_stadium.html')
    elif request.method == 'POST':
        Team_ID = str(request.form["Team_ID"])
        Stadiumname = str(request.form["Stadiumname"])
        Capacity = str(request.form["Capacity"])
        Built = str(request.form["Built"])
        PitchSize = str(request.form["PitchSize"])
        Surface = str(request.form["Surface"])
        obje = forms.FootballStats()
        obje.Stadium_add(Team_ID,Stadiumname,int(Capacity),Built,PitchSize,Surface)
        flash("Stadium added")
        return render_template("add_stadium.html")


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
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player()
        print(cursor)
        return render_template("players.html",cursor=cursor)
    else:
        form_player_keys = request.form.getlist("player_keys")
        for form_player_key in form_player_keys:
            obje.Player_delete(int(form_player_key))
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
        obje = forms.FootballStats()
        obje.Manager_add(Name, Age, Nationalty, Height, PlaceOfBirth)
        flash("You have added.")
        return render_template("add_manager.html")

@app.route("/manager", methods=['GET','POST'])
def manager_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager()
        return render_template("managers.html",cursor=cursor)   
    else:
        form_manager_keys = request.form.getlist("manager_keys")
        for form_manager_key in form_manager_keys:
            obje.Manager_delete(int(form_manager_key))
        return redirect(url_for("manager_page"))


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

@app.route("/goal", methods=['GET','POST'])
def goal_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Goal()
        print(cursor)
        return render_template("goals.html",cursor=cursor)
    else:
        form_goal_keys = request.form.getlist("goal_keys")
        for form_goal_key in form_goal_keys:
            obje.Goal_delete(int(form_goal_key))
        return redirect(url_for("goal_page"))

if __name__ == "__main__":
    app.run(debug=True)

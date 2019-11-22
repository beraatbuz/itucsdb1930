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
@login_required
def fixture_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Fixtures(1)
        return render_template("fixture.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        if(process == "week"):
            week = request.form.get('select') 
            cursor=obje.Fixtures(week)
            return render_template("fixture.html",cursor=cursor)

        elif (process == "Delete"):
            form_fixture_keys = request.form.getlist('fixture')
            for form_fixture_key in form_fixture_keys:
                obje.Fixture_delete(int(form_fixture_key))
            return redirect(url_for("fixture_page"))
        else:
            return fixture_update_page(process)
@app.route("/update_fixture", methods=['GET','POST'])
@login_required
def fixture_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("fixture.html")
    elif request.method == 'POST':
        if update is not None:
            HomeTeam = request.form["HomeTeam"]
            AwayTeam = request.form["AwayTeam"]
            HomeScore = request.form["HomeScore"]
            AwayScore =  request.form["AwayScore"]
            Week =  request.form["Week"]
            MatchDate =  request.form["MatchDate"]
            Time =  request.form["Time"]
            obje = forms.FootballStats()
            obje.Fixture_update(update,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time)
            return redirect(url_for("fixture_page"))
        cursor=obje.Fixture_update_info(process)
        return render_template("update_fixture.html",cursor=cursor)

    
    
@app.route("/add_fixture", methods=['GET','POST'])
@login_required
def fixture_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_fixture.html')

    elif request.method == 'POST':
        HomeTeam = request.form["HomeTeam"]
        AwayTeam = request.form["AwayTeam"]
        HomeScore = request.form["HomeScore"]
        AwayScore =  request.form["AwayScore"]
        Week =  request.form["Week"]
        MatchDate =  request.form["MatchDate"]
        Time =  request.form["Time"]
        Status = request.form["Status"]
        obje = forms.FootballStats()
        obje.Fixture_add(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status)
        flash("You have added.")
        return render_template("add_fixture.html")

@app.route("/add_standing", methods=['GET','POST'])
@login_required
def standing_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_standings.html')

    elif request.method == 'POST':
        TeamID = request.form["TeamID"]
        Played = request.form["Played"]
        Won = request.form["Won"]
        Drawn =  request.form["Drawn"]
        Lost =  request.form["Lost"]
        Goals_for =  request.form["Goals_for"]
        Goals_against =  request.form["Goals_against"]
        obje = forms.FootballStats()
        obje.Standing_add(TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against)
        flash("You have added.")
        return render_template("add_standings.html")

@app.route("/add_referee", methods=['GET','POST'])
@login_required
def referee_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_referee.html')

    elif request.method == 'POST':
        RefereeName = request.form["RefereeName"]
        Age = request.form["Age"]
        TotalMatch = request.form["TotalMatch"]
        TotalRedCard =  request.form["TotalRedCard"]
        TotalYellowCard =  request.form["TotalYellowCard"]
        obje = forms.FootballStats()
        obje.Referee_add(RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard)
        flash("You have added.")
        return render_template("add_referee.html")

@app.route("/standing", methods=['GET','POST'])
@login_required
def standing_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Standings()
        return render_template("standing.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        if(process == "Delete"):
            form_standing_keys = request.form.getlist('standing')
            for form_standing_key in form_standing_keys:
                obje.Standing_delete(int(form_standing_key))
            return redirect(url_for("standing_page"))
        else:
            return standing_update_page(process)
@app.route("/update_standing", methods=['GET','POST'])
@login_required
def standing_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("standing.html")
    elif request.method == 'POST':
        if update is not None:
            TeamID = request.form["TeamID"]
            Played = request.form["Played"]
            Won = request.form["Won"]
            Drawn =  request.form["Drawn"]
            Lost =  request.form["Lost"]
            Goals_for =  request.form["Goals_for"]
            Goals_against =  request.form["Goals_against"]
            obje = forms.FootballStats()
            obje.Standing_update(update,TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against)
            return redirect(url_for("standing_page"))
        cursor=obje.Standing_update_info(process)
        return render_template("update_standing.html",cursor=cursor)

@app.route("/referee", methods=['GET','POST'])
@login_required
def referee_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Referee()
        return render_template("referee.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        if(process == "Delete"):
            form_referee_keys = request.form.getlist('referee')
            for form_referee_key in form_referee_keys:
                print(form_referee_key)
                obje.Referee_delete(int(form_referee_key))
            return redirect(url_for("referee_page"))
        else:
            return referee_update_page(process)
@app.route("/update_referee", methods=['GET','POST'])
@login_required
def referee_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("referee.html")
    elif request.method == 'POST':
        if update is not None:
            RefereeName = request.form["RefereeName"]
            Age = request.form["Age"]
            TotalMatch = request.form["TotalMatch"]
            TotalRedCard =  request.form["TotalRedCard"]
            TotalYellowCard =  request.form["TotalYellowCard"]
            obje = forms.FootballStats()
            obje.Referee_update(update,RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard)
            return redirect(url_for("referee_page"))
        cursor=obje.Referee_update_info(process)
        return render_template("update_referee.html",cursor=cursor)
    
@app.route("/add_team", methods=['GET','POST'])
@login_required
def team_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_team.html')

    elif request.method == 'POST':
        Teamname = str(request.form["Teamname"])
        NickName = str(request.form["NickName"])
        ShortName = str(request.form["ShortName"])
        FoundationDate = str(request.form["FoundationDate"])
        Capacity =  str(request.form["Capacity"])
        ManagerID =  str(request.form["ManagerID"])
        obje = forms.FootballStats()
        obje.Team_add(Teamname,NickName,ShortName,FoundationDate,Capacity,ManagerID)
        flash("You have added.")
        return render_template("add_team.html")

@app.route("/team", methods=['GET','POST'])
@login_required
def team_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Team()
        print(cursor)
        return render_template("teams.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_team_keys = request.form.getlist("team_keys")
            for team_key in form_team_keys:
                obje.Team_delete(team_key)
            flash("You have deleted.")
            return redirect(url_for("team_page"))
        else:
            return team_update_page(process)

@app.route("/stadium", methods=['GET','POST'])
@login_required
def stadium_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Stadium()
        print(cursor)
        return render_template("stadium.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_stadium_keys = request.form.getlist('stadium_keys')
            for form_stadium_key in form_stadium_keys:
                obje.Stadium_delete(int(form_stadium_key))
            return redirect(url_for("stadium_page"))
        else:
            return stadium_update_page(process)


@app.route("/add_stadium", methods=['GET','POST'])
@login_required
def stadium_add_page():
    if not current_user.is_admin:
        abort(401)
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

@app.route("/update_stadium", methods=['GET','POST'])
@login_required
def stadium_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("stadium.html")
    elif request.method == 'POST':
        if update is not None:
            Team_ID = str(request.form["Team_ID"])
            Stadiumname = str(request.form["Stadiumname"])
            Capacity = str(request.form["Capacity"])
            Built = str(request.form["Built"])
            PitchSize = str(request.form["PitchSize"])
            Surface = str(request.form["Surface"])
            obje = forms.FootballStats()
            obje.Stadium_update(update,Team_ID,Stadiumname,int(Capacity),Built,PitchSize,Surface)
            return redirect(url_for("stadium_page"))
        cursor=obje.Stadium_update_info(process)
        print(cursor)
        return render_template("update_stadium.html",cursor=cursor)


@app.route("/assist", methods=['GET','POST'])
@login_required
def assist_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == "GET":
        obje = forms.FootballStats()
        cursor=obje.Assist()
        print(cursor)
        return render_template("assist.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_assist_keys = request.form.getlist('assist_keys')
            for form_assist_key in form_assist_keys:
                obje.Assist_delete(int(form_assist_key))
            return redirect(url_for("assist_page"))
        else:
            return assist_update_page(process)

@app.route("/add_assist", methods=['GET','POST'])
@login_required
def assist_add_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_assist.html')
    elif request.method == 'POST':
        PlayerID = str(request.form["PlayerID"])
        MatchID = str(request.form["MatchID"])
        Minute = str(request.form["Minute"])
        LastTouch = str(request.form["LastTouch"])
        Format = str(request.form["Format"])
        GoldenAssist = str(request.form["GoldenAssist"])
        StadiumHA = str(request.form["StadiumHA"])
        obje = forms.FootballStats()
        obje.Assist_add(PlayerID,MatchID,Minute,LastTouch,Format,GoldenAssist,StadiumHA)
        return render_template("add_assist.html")

@app.route("/update_assist", methods=['GET','POST'])
@login_required
def assist_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("assist.html")
    elif request.method == 'POST':
        if update is not None:
            PlayerID = str(request.form["PlayerID"])
            MatchID = str(request.form["MatchID"])
            Minute = str(request.form["Minute"])
            LastTouch = str(request.form["LastTouch"])
            Format = str(request.form["Format"])
            GoldenAssist = str(request.form["GoldenAssist"])
            StadiumHA = str(request.form["StadiumHA"])
            obje = forms.FootballStats()
            obje.Assist_update(update,PlayerID,MatchID,Minute,LastTouch,Format,GoldenAssist,StadiumHA)
            return redirect(url_for("assist_page"))
        cursor=obje.Assist_update_info(process)
        print(cursor)
        return render_template("update_assist.html",cursor=cursor)

@app.route("/statistic", methods=['GET','POST'])
@login_required
def statistic_page():
    if not current_user.is_admin:
        abort(401)
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
        Position = str(request.form["Position"])
        PlayerNationalty = str(request.form["PlayerNationalty"])
        PlayerHeight = str(request.form["PlayerHeight"])
        PlaceOfBirth = str(request.form["PlaceOfBirth"])
        TeamID = str(request.form["TeamID"])
        obje = forms.FootballStats()
        obje.Player_add(PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID)
        flash("You have added.")
        return render_template("add_player.html")

@app.route("/player", methods=['GET','POST'])
@login_required
def player_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player()
        return render_template("players.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_player_keys = request.form.getlist("player_keys")
            for form_player_key in form_player_keys:
                obje.Player_delete(int(form_player_key))
            return redirect(url_for("player_page"))
        else:
            return player_update_page(process)

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
@login_required
def manager_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager()
        return render_template("managers.html",cursor=cursor)   
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_manager_keys = request.form.getlist("manager_keys")
            for form_manager_key in form_manager_keys:
                obje.Manager_delete(int(form_manager_key))
            return redirect(url_for("manager_page"))
        else:
            return manager_update_page(process)

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
@login_required
def goal_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Goal()
        print(cursor)
        return render_template("goals.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if(process == "Delete"):
            form_goal_keys = request.form.getlist("goal_keys")
            for form_goal_key in form_goal_keys:
                obje.Goal_delete(int(form_goal_key))
            return redirect(url_for("goal_page"))
        else:
            return goal_update_page(process)

@app.route("/update_goal", methods=['GET','POST'])
@login_required
def goal_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("goals.html")
    elif request.method == 'POST':
        if update is not None:
            PlayerID = str(request.form["PlayerID"])
            MatchID = str(request.form["MatchID"])
            Minute = str(request.form["Minute"])
            obje = forms.FootballStats()
            obje.Goal_update(update,PlayerID,MatchID,Minute)
            return redirect(url_for("goal_page"))
        cursor=obje.Goal_update_info(process)
        print(cursor)
        return render_template("update_goal.html",cursor=cursor)

@app.route("/update_manager", methods=['GET','POST'])
@login_required
def manager_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("managers.html")
    elif request.method == 'POST':
        if update is not None:
            Name = str(request.form["Name"])
            Age = str(request.form["Age"])
            Nationalty = str(request.form["Nationalty"])
            Height = str(request.form["Height"])
            PlaceOfBirth = str(request.form["PlaceOfBirth"])
            obje = forms.FootballStats()
            obje.Manager_update(update,Name,Age,Nationalty,Height,PlaceOfBirth)
            return redirect(url_for("manager_page"))
        cursor=obje.Manager_update_info(process)
        print(cursor)
        return render_template("update_manager.html",cursor=cursor)

@app.route("/update_player", methods=['GET','POST'])
@login_required
def player_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("players.html")
    elif request.method == 'POST':
        if update is not None:
            PlayerName = str(request.form["PlayerName"])
            PlayerAge = str(request.form["PlayerAge"])
            Position = str(request.form["Position"])
            PlayerNationalty = str(request.form["PlayerNationalty"])
            PlayerHeight = str(request.form["PlayerHeight"])
            PlaceOfBirth = str(request.form["PlaceOfBirth"])
            TeamID = str(request.form["TeamID"])
            obje = forms.FootballStats()
            obje.Player_update(update,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,TeamID)
            return redirect(url_for("player_page"))
        cursor=obje.Player_update_info(process)
        print(cursor)
        return render_template("update_player.html",cursor=cursor)

@app.route("/update_team", methods=['GET','POST'])
@login_required
def team_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("teams.html")
    elif request.method == 'POST':
        if update is not None:
            Teamname = str(request.form["Teamname"])
            NickName = str(request.form["NickName"])
            ShortName = str(request.form["ShortName"])
            FoundationDate = str(request.form["FoundationDate"])
            Capacity = str(request.form["Capacity"])
            ManagerID = str(request.form["ManagerID"])
            obje = forms.FootballStats()
            obje.Team_update(update,Teamname,NickName,ShortName,FoundationDate,Capacity,ManagerID)
            return redirect(url_for("team_page"))
        cursor=obje.Team_update_info(process)
        print(cursor)
        return render_template("update_team.html",cursor=cursor)


@app.route("/player")
@login_required
def players_page(player_key):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player_key(player_key)
        print(cursor)
        return render_template("players.html",cursor=cursor)
app.add_url_rule("/player/<player_key>", view_func=players_page)

@app.route("/teams")
@login_required
def teams_page(team_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Team_key(team_keys)
        print(cursor)
        return render_template("teams.html",cursor=cursor)
app.add_url_rule("/team/<team_keys>", view_func=teams_page) 

@app.route("/goals")
@login_required
def goals_page(goal_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Goal_key(goal_keys)
        print(cursor)
        return render_template("goals.html",cursor=cursor)
app.add_url_rule("/goal/<goal_keys>", view_func=goals_page) 

@app.route("/managers")
@login_required
def managers_page(manager_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager_key(manager_keys)
        print(cursor)
        return render_template("managers.html",cursor=cursor)
app.add_url_rule("/manager/<manager_keys>", view_func=managers_page) 

if __name__ == "__main__":
    app.run(debug=True)

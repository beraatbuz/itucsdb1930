from flask import Flask,render_template,request,redirect,url_for,flash,abort,session
from flask_login import LoginManager,login_user,current_user,login_required,logout_user
from user import get_user
from wtforms import Form, BooleanField, StringField, validators,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from passlib.hash import pbkdf2_sha256 as hasher
import forms
import webbrowser
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
     return redirect(url_for("fixture_user_page"))

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
                flash("You have logged in.")
                next_page = request.args.get("next", url_for("fixture_page"))
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

@app.route("/fixture_user", methods=['GET','POST'])
def fixture_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Fixtures(1)
        return render_template("user-fixture.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        week = request.form.get('select') 
        cursor=obje.Fixtures(week)
        return render_template("user-fixture.html",cursor=cursor)

@app.route("/referee_user", methods=['GET'])
def referee_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Referee()
        return render_template("user-referee.html",cursor=cursor)

@app.route("/standing_user", methods=['GET'])
def standing_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Standings()
        return render_template("user-standing.html",cursor=cursor)

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
        processStart = request.form.get('Start')
        processLive = request.form.get('Live')
        update = request.form.get('Update')
        if (process == "add"):
            return redirect(url_for("fixture_adding_page"))
        elif (processStart):
            return fixture_update_page(processStart)
        elif (processLive):
            return live_match_page(processLive)
        elif (process == "week"):
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
    obje = forms.FootballStats()
    if not current_user.is_admin:
        abort(401)
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
            Status = request.form["Status"]
            Refereeid=request.form["Refereeid"]
            obje.Fixture_update(update,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid)
            return redirect(url_for("fixture_page"))
        cursor=obje.Fixture_update_info(process)
        cursor1=obje.Team()
        cursor2=obje.Referee()
        return render_template("update_fixture.html",cursor=[cursor,cursor1,cursor2])

    
    
@app.route("/add_fixture", methods=['GET','POST'])
@login_required
def fixture_adding_page():
    obje = forms.FootballStats()
    cursor1=obje.Team()
    cursor2=obje.Referee()
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_fixture.html',cursor=[cursor1,cursor2])

    elif request.method == 'POST':
        HomeTeam = request.form["HomeTeam"]
        AwayTeam = request.form["AwayTeam"]
        HomeScore = request.form["HomeScore"]
        AwayScore =  request.form["AwayScore"]
        Week =  request.form["Week"]
        MatchDate =  request.form["MatchDate"]
        Time =  request.form["Time"]
        Status = request.form["Status"]
        Refereeid=request.form["Refereeid"]
        obje = forms.FootballStats()
        obje.Fixture_add(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid)
        flash("You have added.")
        return render_template("add_fixture.html",cursor=[cursor1,cursor2])

@app.route("/add_standing", methods=['GET','POST'])
@login_required
def standing_adding_page():
    obje = forms.FootballStats()
    cursor1=obje.Team()
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        return render_template('add_standings.html',cursor=cursor1)

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
        return render_template("add_standings.html",cursor=cursor1)

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
        if (process == "add"):
            return redirect(url_for("standing_adding_page"))
        elif (process == "Delete"):
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
        cursor1=obje.Team()
        return render_template("update_standing.html",cursor=[cursor,cursor1])

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
        if (process == "add"):
            return redirect(url_for("referee_adding_page"))
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
        obje = forms.FootballStats()
        managerCursor=obje.Manager_user()
        return render_template('add_team.html',cursor=managerCursor)
    elif request.method == 'POST':
        Teamname = str(request.form["Teamname"])
        NickName = str(request.form["NickName"])
        ShortName = str(request.form["ShortName"])
        FoundationDate = str(request.form["FoundationDate"])
        ManagerID =  str(request.form["ManagerID"])
        Location =  str(request.form["Location"])
        obje = forms.FootballStats()
        obje.Team_add(Teamname,NickName,ShortName,FoundationDate,ManagerID,Location)
        flash("You have added.")
        return redirect(url_for("team_adding_page"))

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
        if (process == "add"):
            return redirect(url_for("team_adding_page"))
        elif(process == "Delete"):
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
        elif (process == "add"):
            return redirect(url_for("stadium_add_page"))
        else:
            return stadium_update_page(process)


@app.route("/add_stadium", methods=['GET','POST'])
@login_required
def stadium_add_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        obje = forms.FootballStats()
        teamCursor=obje.Team()
        return render_template('add_stadium.html',cursor=teamCursor)
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
        return redirect(url_for("stadium_add_page"))

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
        teamsCursor = obje.Team()
        print(cursor)
        return render_template("update_stadium.html",cursor=[cursor,teamsCursor])


@app.route("/assist", methods=['GET','POST'])
@login_required
def assist_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":    
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
        elif (process == "add"):
            return redirect(url_for("assist_add_page"))
        else:
            return assist_update_page(process)

@app.route("/add_assist", methods=['GET','POST'])
@login_required
def assist_add_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        obje = forms.FootballStats()
        playerCursor=obje.Player()
        fixtureCursor=obje.Fixtures2()
        return render_template('add_assist.html',cursor=[playerCursor,fixtureCursor])
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
        return redirect(url_for("assist_add_page"))

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
        playerCursor = obje.Player()
        fixtureCursor = obje.Fixtures2()
        print(cursor)
        return render_template("update_assist.html",cursor=[cursor,playerCursor,fixtureCursor])

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
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        if(process == "Delete"):
            form_statistic_keys = request.form.getlist('statistic_keys')
            for form_statistic_key in form_statistic_keys:
                obje.Statistic_delete(int(form_statistic_key))
            return redirect(url_for("statistic_page"))
        elif (process == "add"):
            return redirect(url_for("statistic_add_page"))
        else:
            return statistic_update_page(process)

@app.route("/add_statistic", methods=['GET','POST'])
@login_required
def statistic_add_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    cursor=obje.Referee()
    cursor2=obje.Fixtures2()
    if request.method == 'GET':
        return render_template('add_statistic.html',cursor=[cursor,cursor2])
    elif request.method == 'POST':
        MatchID = str(request.form["MatchID"])
        HPossesion = str(request.form["HPossesion"])
        HCorner = str(request.form["HCorner"])
        HFoul = str(request.form["HFoul"])
        HOffside = str(request.form["HOffside"])
        HShot = str(request.form["HShot"])
        HShotOnTarget = str(request.form["HShotOnTarget"])
        HShotAccuracy = str(request.form["HShotAccuracy"])
        HPassAccuracy = str(request.form["HPassAccuracy"])
        APossesion = str(request.form["APossesion"])
        ACorner = str(request.form["ACorner"])
        AFoul = str(request.form["AFoul"])
        AOffside = str(request.form["AOffside"])
        AShot = str(request.form["AShot"])
        AShotOnTarget = str(request.form["AShotOnTarget"])
        AShotAccuracy = str(request.form["AShotAccuracy"])
        APassAccuracy = str(request.form["APassAccuracy"])
        RefereeID = str(request.form["RefereeID"])
        obje = forms.FootballStats()
        obje.Statistic_add(MatchID, HPossesion,HCorner,HFoul,HOffside,HShot,HShotOnTarget,HShotAccuracy,HPassAccuracy,APossesion,ACorner,AFoul,AOffside,AShot,AShotOnTarget,AShotAccuracy,APassAccuracy,RefereeID)
        return render_template("add_statistic.html",cursor=[cursor,cursor2])

@app.route("/update_statistic", methods=['GET','POST'])
@login_required
def statistic_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    cursorReferee=obje.Referee()
    cursorFixture=obje.Fixtures2()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("statistic.html")
    elif request.method == 'POST':
        if update is not None:
            MatchID = str(request.form["MatchID"])
            HPossesion = str(request.form["HPossesion"])
            HCorner = str(request.form["HCorner"])
            HFoul = str(request.form["HFoul"])
            HOffside = str(request.form["HOffside"])
            HShot = str(request.form["HShot"])
            HShotOnTarget = str(request.form["HShotOnTarget"])
            HShotAccuracy = str(request.form["HShotAccuracy"])
            HPassAccuracy = str(request.form["HPassAccuracy"])
            APossesion = str(request.form["APossesion"])
            ACorner = str(request.form["ACorner"])
            AFoul = str(request.form["AFoul"])
            AOffside = str(request.form["AOffside"])
            AShot = str(request.form["AShot"])
            AShotOnTarget = str(request.form["AShotOnTarget"])
            AShotAccuracy = str(request.form["AShotAccuracy"])
            APassAccuracy = str(request.form["APassAccuracy"])
            RefereeID = str(request.form["RefereeID"])
            obje = forms.FootballStats()
            obje.Statistic_Update(update,MatchID, HPossesion,HCorner,HFoul,HOffside,HShot,HShotOnTarget,HShotAccuracy,HPassAccuracy,APossesion,ACorner,AFoul,AOffside,AShot,AShotOnTarget,AShotAccuracy,APassAccuracy,RefereeID)
            return redirect(url_for("statistic_page"))
        cursor=obje.Statistic_update_info(process)
        print(cursor)
        return render_template("update_statistic.html",cursor=[cursor,cursorReferee,cursorFixture])

@app.route("/add_detail", methods=['GET','POST'])
@login_required
def detail_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        obje = forms.FootballStats()
        fixtureCursor=obje.Fixtures2()
        return render_template('add_detail.html',cursor=fixtureCursor)
    elif request.method == 'POST':
        Detail = str(request.form["Detail"])
        MatchID = str(request.form["MatchID"])
        Minute = str(request.form["Minute"])
        obje = forms.FootballStats()
        obje.Detail_add(MatchID,Detail, Minute)
        flash("You have added.")
        return redirect(url_for("detail_adding_page"))

@app.route("/detail", methods=['GET','POST'])
@login_required
def detail_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Detail()
        print(cursor)
        return render_template("detail.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if (process == "add"):
            return redirect(url_for("detail_adding_page"))
        elif(process == "Delete"):
            form_detail_keys = request.form.getlist("detail_keys")
            for form_detail_key in form_detail_keys:
                obje.Detail_delete(int(form_detail_key))
            return redirect(url_for("detail_page"))
        else:
            return detail_update_page(process)

@app.route("/update_detail", methods=['GET','POST'])
@login_required
def detail_update_page(process):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    update = request.form.get('Update') 
    if request.method == 'GET':
        return render_template("detail.html")
    elif request.method == 'POST':
        if update is not None:
            Detail = str(request.form["Detail"])
            MatchID = str(request.form["MatchID"])
            Minute = str(request.form["Minute"])
            obje = forms.FootballStats()
            obje.Detail_update(update,MatchID,Detail,Minute)
            return redirect(url_for("detail_page"))
        cursor=obje.Detail_update_info(process)
        fixturesCursor = obje.Fixtures2()
        print(cursor)
        return render_template("update_detail.html",cursor=[cursor,fixturesCursor])

@app.route("/add_player", methods=['GET','POST'])
@login_required
def player_adding_page():
    if not current_user.is_admin:
        abort(401)
    if request.method == 'GET':
        obje = forms.FootballStats()
        teamCursor=obje.Team()
        return render_template('add_player.html',cursor=teamCursor)

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
        return redirect(url_for("player_adding_page"))

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
        if (process == "add"):
            return redirect(url_for("player_adding_page"))
        elif(process == "Delete"):
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
        return redirect(url_for("manager_adding_page"))

@app.route("/manager", methods=['GET','POST'])
@login_required
def manager_page():
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager_user()
        return render_template("managers.html",cursor=cursor)   
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if (process == "add"):
            return redirect(url_for("manager_adding_page"))
        elif(process == "Delete"):
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
        obje = forms.FootballStats()
        playerCursor=obje.Player()
        matchCursor=obje.Fixtures2()
        return render_template('add_goal.html',cursor=[playerCursor,matchCursor])

    elif request.method == 'POST':
        PlayerID = str(request.form["PlayerID"])
        MatchID = str(request.form["MatchID"])
        Minute = str(request.form["Minute"])
        obje = forms.FootballStats()
        obje.Goal_add(PlayerID, MatchID, Minute)
        flash("You have added.")
        return redirect(url_for("goal_adding_page"))

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
        if (process == "add"):
            return redirect(url_for("goal_adding_page"))
        elif(process == "Delete"):
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
        playerCursor = obje.Player()
        matchCursor = obje.Fixtures2()
        print(cursor)
        return render_template("update_goal.html",cursor=[cursor,playerCursor,matchCursor])

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
        teamCursor = obje.Team()
        print(cursor)
        return render_template("update_player.html",cursor=[cursor,teamCursor])

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
            ManagerID = str(request.form["ManagerID"])
            Location = str(request.form["Location"])
            obje = forms.FootballStats()
            obje.Team_update(update,Teamname,NickName,ShortName,FoundationDate,ManagerID,Location)
            return redirect(url_for("team_page"))
        cursor=obje.Team_update_info(process)
        managerCursor = obje.Manager_user()
        print(cursor)
        return render_template("update_team.html",cursor=[cursor, managerCursor])


@app.route("/player",methods=['GET','POST'])
@login_required
def players_page(player_key):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player_key(player_key)
        print(cursor)
        return render_template("players.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if (process == "add"):
            return redirect(url_for("player_adding_page"))
        elif(process == "Delete"):
            form_player_keys = request.form.getlist("player_keys")
            for form_player_key in form_player_keys:
                obje.Player_delete(int(form_player_key))
            return redirect(url_for("player_page"))
        else:
            return player_update_page(process)
app.add_url_rule("/player/<player_key>", view_func=players_page,methods=['GET','POST'])

i = 0

@app.route("/teams",methods=['GET','POST'])
@login_required
def teams_page(team_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Team_key(team_keys)
        playerCursor=obje.Player_team_user(team_keys)
        stadiumCursor=obje.Stadium_key(team_keys)
        fixtureCursor=obje.Fixture_team_key(team_keys)
        managerCursor=obje.Manager_team_key(team_keys)
        print(cursor)
        return render_template("teams_player.html",cursor=[cursor,playerCursor,stadiumCursor,fixtureCursor,managerCursor])
    else:
        global i
        process = request.form.get('buttonName')
        processStadium = request.form.get('buttonStadium')
        processMatches = request.form.get('buttonMatch')
        processManager = request.form.get('buttonManager')
        processTeam = request.form.get('buttonTeam')
        processStart = request.form.get('Start')
        processPlayer = request.form.get('buttonPlayer')
        if(processStadium):
            i=1
            return stadium_update_page(processStadium)
        elif (processMatches):
            i=2
            return fixture_update_page(processMatches)
        elif (processPlayer):
            i=3
            return player_update_page(processPlayer)
        elif (processManager):
            i=4
            return manager_update_page(processManager)
        elif (processTeam):
            i=5
            return team_update_page(processTeam)
        elif (processStart):
            i=6
            return fixture_update_page(processStart)
        elif (process == "add"):
            return redirect(url_for("team_adding_page"))
        elif (process == "add_player"):
            return redirect(url_for("player_adding_page"))
        elif (process == "add_stadium"):
            return redirect(url_for("stadium_add_page"))
        elif (process == "add_Match"):
            return redirect(url_for("fixture_adding_page"))
        elif (process == "add_Manager"):
            return redirect(url_for("manager_adding_page"))
        elif(process == "Delete"):
            form_team_keys = request.form.getlist("team_keys")
            for team_key in form_team_keys:
                obje.Team_delete(team_key)
            flash("You have deleted.")
            return redirect(url_for("team_page"))
        elif(process == "Delete_player"):
            form_player_keys = request.form.getlist("player_keys")
            for form_player_key in form_player_keys:
                obje.Player_delete(int(form_player_key))
            return redirect(url_for("team_page"))
        elif(process == "Delete_stadium"):
            form_stadium_keys = request.form.getlist('stadium_keys')
            for form_stadium_key in form_stadium_keys:
                obje.Stadium_delete(int(form_stadium_key))
            return redirect(url_for("team_page"))
        elif(process == "Delete_match"):
            form_fixture_keys = request.form.getlist('fixture')
            for form_fixture_key in form_fixture_keys:
                obje.Fixture_delete(int(form_fixture_key))
            return redirect(url_for("team_page"))
        elif(process == "Delete_manager"):
            form_manager_keys = request.form.getlist("manager_keys")
            for form_manager_key in form_manager_keys:
                obje.Manager_delete(int(form_manager_key))
            return redirect(url_for("team_page"))
        else:
            if(i==1):
                stadium_update_page(processStadium)
            elif(i==2):
                fixture_update_page(processMatches)
            elif(i==3):  
                player_update_page(processPlayer)      
            elif(i==4):
                manager_update_page(processManager)
            elif(i==5):
                team_update_page(processTeam)
            elif(i==6):
                fixture_update_page(processStart)
            cursor=obje.Team_key(team_keys)
            playerCursor=obje.Player_team_user(team_keys)
            stadiumCursor=obje.Stadium_key(team_keys)
            fixtureCursor=obje.Fixture_team_key(team_keys)
            managerCursor=obje.Manager_team_key(team_keys)
            return render_template("teams_player.html",cursor=[cursor,playerCursor,stadiumCursor,fixtureCursor,managerCursor])
app.add_url_rule("/team/<team_keys>", view_func=teams_page,methods=['GET','POST']) 

@app.route("/goals",methods=['GET','POST'])
@login_required
def goals_page(goal_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Goal_key(goal_keys)
        print(cursor)
        return render_template("goals.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if (process == "add"):
            return redirect(url_for("goal_adding_page"))
        elif(process == "Delete"):
            form_goal_keys = request.form.getlist("goal_keys")
            for form_goal_key in form_goal_keys:
                obje.Goal_delete(int(form_goal_key))
            return redirect(url_for("goal_page"))
        else:
            return goal_update_page(process)
app.add_url_rule("/goal/<goal_keys>", view_func=goals_page,methods=['GET','POST']) 

@app.route("/managers", methods=['GET','POST'])
@login_required
def managers_page(manager_keys):
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager_key(manager_keys)
        print(cursor)
        return render_template("managers.html",cursor=cursor)
    else:
        process = request.form.get('buttonName')
        update = request.form.get('Update')
        print(update)
        if (process == "add"):
            return redirect(url_for("manager_adding_page"))
        elif(process == "Delete"):
            form_manager_keys = request.form.getlist("manager_keys")
            for form_manager_key in form_manager_keys:
                obje.Manager_delete(int(form_manager_key))
            return redirect(url_for("manager_page"))
        else:
            return manager_update_page(process)
app.add_url_rule("/manager/<manager_keys>", view_func=managers_page,methods=['GET','POST']) 


@app.route("/top_goal", methods=['GET'])
def top_goal_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Top_goal()
        print(cursor)
        return render_template("user_top_goal.html",cursor=cursor)

@app.route("/teams_user", methods=['GET'])
def team_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Team()
        print(cursor)
        return render_template("user_teams.html",cursor=cursor)

@app.route("/managers_user", methods=['GET'])
def manager_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager_user()
        return render_template("user_managers.html",cursor=cursor)  

@app.route("/players_user", methods=['GET'])
def player_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player()
        return render_template("user_players.html",cursor=cursor)

@app.route("/managers_user")
def managers_user_page(manager_keys):
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Manager_key(manager_keys)
        print(cursor)
        return render_template("user_managers.html",cursor=cursor)
app.add_url_rule("/managers_user/<manager_keys>", view_func=managers_user_page) 


@app.route("/players_user")
def players_user_page(player_key):
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Player_key(player_key)
        print(cursor)
        return render_template("user_players.html",cursor=cursor)
app.add_url_rule("/players_user/<player_key>", view_func=players_user_page)

@app.route("/teams_user")
def teams_user_page(team_keys):
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Team_user_key(team_keys)
        playerCursor=obje.Player_team_user(team_keys)
        stadiumCursor=obje.Stadium_key(team_keys)
        fixtureCursor=obje.Fixture_team_key(team_keys)
        managerCursor=obje.Manager_team_key(team_keys)
        print(cursor)
        return render_template("user_teams_player.html",cursor=[cursor,playerCursor,stadiumCursor,fixtureCursor,managerCursor])
app.add_url_rule("/teams_user/<team_keys>", view_func=teams_user_page) 

@app.route("/referee_user")
def referees_user_page(referee):
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Referee_user_key(referee)
        print(cursor)
        return render_template("user-referee.html",cursor=cursor)
app.add_url_rule("/referee_user/<referee>", view_func=referees_user_page) 

@app.route("/detail_user")
def detail_user_page(detail_key):
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Detail_user(detail_key)
        cursorFixture=obje.Fixture_key(detail_key)
        cursorGoal=obje.Goal_user(detail_key)
        cursorAssist=obje.Assist_user(detail_key)
        cursorStatistic=obje.Statistic_user(detail_key)
        print(cursor)
        return render_template("user_detail.html",cursor=[cursor,cursorFixture,cursorGoal,cursorAssist,cursorStatistic])
app.add_url_rule("/detail_user/<detail_key>", view_func=detail_user_page) 

@app.route("/top_assist", methods=['GET'])
def top_assist_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Top_assist()
        cursorInfo=obje.Assist_information_of_user()
        print(cursor)
        return render_template("user_top_assist.html",cursor=[cursor,cursorInfo])

@app.route("/stadium_user", methods=['GET'])
def stadium_user_page():
    obje = forms.FootballStats()
    if request.method == "GET":
        cursor=obje.Stadium()
        print(cursor)
        return render_template("user_stadium.html",cursor=cursor)
        
@app.route("/live_match", methods=['GET','POST'])
@login_required
def live_match_page(processLive): 
    if not current_user.is_admin:
        abort(401)
    obje = forms.FootballStats()
    cursorFixture = obje.Fixture_key(processLive)
    cursorStanding = obje.Standing_key(processLive)
    cursorPlayer = obje.Player_fixture_team(processLive)
    cursorDetail = obje.Detail_user(processLive)
    cursorGoal = obje.Goal_user(processLive)
    cursorAssist = obje.Assist_user(processLive)
    return render_template("live_match.html", cursor=[cursorFixture,cursorStanding,cursorPlayer,cursorDetail,cursorGoal,cursorAssist])
    


if __name__ == "__main__":
    app.run(debug=True)

###############################################################################3
        #if request.method == "POST":
        #return live_match_page(processLive)
        
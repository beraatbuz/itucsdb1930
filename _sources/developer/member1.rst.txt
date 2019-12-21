Parts Implemented by Ahmet YILMAZ
================================

Database Design
---------------

**explain the database design of your project**

   .. figure:: erDiagram.png
         :scale: 50 %
         :alt: E/R Diagram for Assist, Statistic, Stadium


Code
----

**explain the technical structure of your code**

**to include a code listing, use the following example**:

   .. code-block:: python

      def Assist(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Assist.id,Player.playername,Assist.minute,home.teamname as HomeTeam, away.teamname as AwayTeam,Assist.lasttouch,Assist.format,Assist.goldenassist,Assist.stadiumha, Player.id, HomeTeam,Awayteam,MatchID FROM Assist, Player,Teams as home, Teams as away, Fixtures where Assist.playerid = Player.id and Assist.matchid = fixtures.id and home.id=fixtures.hometeam and away.id=fixtures.awayteam ORDER BY fixtures.ID"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This code get all assist from db by joining Teams and Fixtures tables. To show the assist is done in which match we have to join with fixtures table and teams table for team’s name

   .. code-block:: python

      def Assist_add(self, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Assist(PlayerId,MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([PlayerId, MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA]))

   This method adds new assist

   .. code-block:: python

      def Assist_delete(self, AssistId):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Delete From Assist Where ID = %s; """
               cursor.execute(statement,([AssistId]))

   This method deletes the asistst according to id value.

   .. code-block:: python

      def Assist_update(self, AssistId, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Assist Set PlayerID=%s, MatchID=%s, Minute=%s, LastTouch=%s, Format=%s,GoldenAssist=%s,StadiumHA=%s Where ID=%s;"""
               cursor.execute(statement,([PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA, AssistId]))

   This query updates the assist that exists before

   .. code-block:: python

      def Assist_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Assist where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

   To get information of asisst that will be updated and show in the .html page, we use this method.

   .. code-block:: python

      def Assist_user(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Assist.id,Player.playername,Teams.Teamname, Assist.minute,Assist.lasttouch,Assist.format,Assist.goldenassist,Assist.stadiumha, Player.id, Player.teamid FROM Assist, Player,Teams,Fixtures where Assist.playerid = Player.id and Assist.matchid = fixtures.id and fixtures.id=%s and Teams.id=Player.Teamid ORDER BY minute"""
               cursor.execute(statement,[Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   To show assists information on the user side, we use this query.

   .. code-block:: python

      def Stadium(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Stadium.id, Teamname, StadiumName, capacity,built,pitchsize,surface,team_id FROM Stadium,teams Where Teams.id=team_id ORDER BY Teamname"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This code get all stadium information from db by joining Teams table to show team’s name.

   .. code-block:: python
	
      def Stadium_add(self, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Stadium(Team_ID,Stadiumname,Capacity,Built,PitchSize,Surface) VALUES(%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface]))

   This method adds new stadium for teams.

   .. code-block:: python
	
      def Stadium_delete(self,StadiumId):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Delete From Stadium Where ID = %s;"""
               cursor.execute(statement,([StadiumId]))

   This method deletes the stadium according to id value.

   .. code-block:: python

      def Stadium_update(self, StadiumId, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Stadium Set Team_ID=%s, Stadiumname=%s, Capacity=%s, Built=%s, PitchSize=%s, Surface=%s Where ID=%s;"""
               cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface, StadiumId]))

   This query updates the stadium that exists before

   .. code-block:: python

      def Stadium_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Stadium where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

   To get information of stadium that will be updated and show in the .html page, we use this method.

   .. code-block:: python

      def Stadium_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Stadium.id, Teamname, StadiumName, capacity,built,pitchsize,surface,team_id FROM Stadium,teams Where Teams.id=team_id and team_id=%s ORDER BY Teamname"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   To show stadium information on the user side, we use this query.

   .. code-block:: python

      def Statistic(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select statistic.ID, matchid, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeName FROM Statistic,Referee where "RefereeID"=Referee.ID ORDER BY MatchID"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This code get all statistic from db by joining Referee table to show referee’s name.

   .. code-block:: python
	
      def Statistic_add(self, MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Statistic(MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, "RefereeID") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID]))

   This method adds new statistic for the match
   
   .. code-block:: python
      
      def Statistic_delete(self, StatisticId):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Delete From Statistic Where ID = %s; """
               cursor.execute(statement,([StatisticId]))

   This method deletes the statistic according to id value.

   .. code-block:: python

      def Statistic_Update(self, StatisticId, MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Statistic Set MatchID=%s, HPossesion=%s, HCorner=%s, HFoul=%s, HOffside=%s, HShot=%s, HShotOnTarget=%s, HShotAccuracy=%s, HPassAccuracy=%s, APossesion=%s, ACorner=%s, AFoul=%s, AOffside=%s, AShot=%s, AShotOnTarget=%s, AShotAccuracy=%s, APassAccuracy=%s, "RefereeID"=%s Where ID=%s;"""
               cursor.execute(statement,([MatchID, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeID,StatisticId]))
	
   This query updates the statistic that exists before

   .. code-block:: python
      
      def Statistic_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select * FROM Statistic where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

   To get information of statistic that will be updated and show in the .html page, we use this method.

   .. code-block:: python

      def Statistic_user(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select statistic.ID, matchid, HPossesion, HCorner, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, APossesion, ACorner, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, RefereeName, Statistic."RefereeID" FROM Statistic, Referee  Where matchid=%s and Statistic."RefereeID"=Referee.id ORDER BY MatchID"""
               cursor.execute(statement,[Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   To show statistic information on the user side, we use this query.

   .. code-block:: python

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

   In this method, if we enter the stadium page with get method, we list information of stadiums. If it is post, we investigate the button value. If the value is add we go to stadium add page, if it is delete, we call stadium delete method. In the other possibility we go to stadium update page by calling stadium information method that gets the information of stadium that will be updated. 

   .. code-block:: python

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

   if our method is post, we get the form information and we add new stadium.

   .. code-block:: python

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

   if our method is post, we update the stadium according the id value received as a parameter.

   .. code-block:: python

      @app.route("/stadium_user", methods=['GET'])
      def stadium_user_page():
         obje = forms.FootballStats()
         if request.method == "GET":
            cursor=obje.Stadium()
            print(cursor)
            return render_template("user_stadium.html",cursor=cursor)

   To send information of stadiums to user, we use this method

   .. code-block:: python

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

   In this method, if we enter the assist page with get method, we list information of assists.  If it is post, we investigate the button value. If the value is add we go to assists add page, if it is delete, we call assist delete method. In the other possibility we go to assist update page by calling assist information method that gets the information of assists that will be updated.

   .. code-block:: python

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

   if our method is post, we get the form information and we add new assist.

   .. code-block:: python

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

   if our method is post, we update the assist according the id value received as a parameter.

   .. code-block:: python
      @app.route("/top_assist", methods=['GET'])
      def top_assist_page():
      obje = forms.FootballStats()
      if request.method == "GET":
         cursor=obje.Top_assist()
         cursorInfo=obje.Assist_information_of_user()
         print(cursor)
         return render_template("user_top_assist.html",cursor=[cursor,cursorInfo])

   To send information of top player’s assists, we use this method.

   .. code-block:: python

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

   In this method, if we enter the statistic page with get method, we list information of statistic.  If it is post, we investigate the button value. If the value is add we go to stastistic add page, if it is delete, we call statistc delete method. In the other possibility we go to statistic update page by calling statistic information method that gets the information of statistic that will be updated.

   .. code-block:: python

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

   if our method is post, we get the form information and we add new statistic.

   .. code-block:: python

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

   if our method is post, we update the statistic according the id value received as a parameter.

Parts Implemented by Muhammed Enes Tırnakçı
================================

Database Design
---------------

   .. figure:: erDiagramEnes.png
         :scale: 50 %
         :alt: E/R Diagram for Teams, Player, Manager, Goal Table 


Code
----

   .. code-block:: python

      """

      CREATE TABLE IF NOT EXISTS  Teams
      (
               ID SERIAL PRIMARY KEY,
               Teamname VARCHAR(30) NOT NULL,
               NickName VARCHAR(30),
               ShortName VARCHAR(30) NOT NULL,
               FoundationDate VARCHAR(30),	
               ManagerID INTEGER REFERENCES Manager (ID) ON DELETE cascade,
               Location VARCHAR(50)
      )
      """,
      """

      CREATE TABLE IF NOT EXISTS  Player
      (
               ID SERIAL PRIMARY KEY,
               PlayerName VARCHAR(30) NOT NULL,
               PlayerAge INTEGER NOT NULL,
               Position VARCHAR(30),
               PlayerNationalty VARCHAR(30) NOT NULL,
               PlayerHeight INTEGER NOT NULL,
               PlaceOfBirth VARCHAR(30) NOT NULL,
               TeamID INTEGER NOT NULL REFERENCES Teams (ID) ON DELETE cascade
      )
      """,
      """

      CREATE TABLE IF NOT EXISTS  Manager
      (
               ID SERIAL PRIMARY KEY,
               Name VARCHAR(30) NOT NULL,
               Age INTEGER NOT NULL,
               Nationalty VARCHAR(30) NOT NULL,
               Height INTEGER NOT NULL,
               PlaceOfBirth VARCHAR(30) NOT NULL,
               teamid integer REFERENCES teams (ID) ON DELETE cascade
      )
      """,
      """ 

      CREATE TABLE IF NOT EXISTS  Goal
      (
         ID serial,
         PlayerID integer NOT NULL REFERENCES Player (ID) ON DELETE cascade,
         MatchID integer NOT NULL REFERENCES Fixtures (ID) ON DELETE cascade,
                              Minute INTEGER NOT NULL,
         PRIMARY KEY (ID)
      ) 
      """,

   These methods create tables.

   .. code-block:: python

      def Team_add(self, TeamName, NickName, ShortName, FoundationDate, ManagerID,Location):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Teams(TeamName, NickName, ShortName, FoundationDate,  ManagerID,Location) VALUES(%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, ManagerID,Location]))

   This method adds new team.

 
   .. code-block:: python

      def Team_update(self, TeamID, TeamName, NickName, ShortName, FoundationDate, ManagerID,Location):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Teams Set Teamname=%s, NickName=%s, ShortName=%s, FoundationDate=%s, ManagerID=%s,Location=%s  Where ID=%s;"""
               cursor.execute(statement,([TeamName, NickName, ShortName, FoundationDate, ManagerID, Location, TeamID]))

   This method updates teams.
    
   .. code-block:: python

      def Team_delete(self, TeamID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ DELETE FROM Teams WHERE ID = %s;"""
               cursor.execute(statement,[TeamID])		

   This method deletes teams.
    
   .. code-block:: python

      def Goal_add(self, PlayerID, MatchID, Minute):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Goal(PlayerID, MatchID, Minute) VALUES(%s,%s,%s);"""
               cursor.execute(statement,([PlayerID, MatchID,Minute]))

   This method adds new goal.
    
   .. code-block:: python

      def Goal_update(self, GoalID, PlayerID, MatchID, Minute):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Goal Set PlayerID=%s, MatchID=%s, Minute=%s Where ID=%s;"""
               cursor.execute(statement,([PlayerID, MatchID, Minute, GoalID]))

   This method updates goals.
    
   .. code-block:: python

      def Goal_delete(self, GoalID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ DELETE FROM Goal WHERE ID = %s;"""
               cursor.execute(statement,[GoalID])	

   This method deletes goals.
    
   .. code-block:: python

      def Player_add(self, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """
                                 INSERT INTO Player(PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID]))

   This method adds new player.
    
   .. code-block:: python

      def Player_delete(self, PlayerID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ DELETE FROM Player WHERE ID = %s;"""
               cursor.execute(statement,[PlayerID])

   This method deletes players.
    
   .. code-block:: python

      def Player_update(self, PlayerID, PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Player Set PlayerName=%s, PlayerAge=%s, Position=%s, PlayerNationalty=%s, PlayerHeight=%s, PlaceOfBirth=%s, TeamID=%s Where ID=%s;"""
               cursor.execute(statement,([PlayerName, PlayerAge, Position, PlayerNationalty, PlayerHeight, PlaceOfBirth, TeamID, PlayerID]))

   This method updates players.
    
   .. code-block:: python

      def Manager_add(self, Name, Age, Nationalty, Height, PlaceOfBirth):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """INSERT INTO Manager(Name, Age, Nationalty, Height, PlaceOfBirth) VALUES(%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth]))

   This method adds new manager.
    
   .. code-block:: python

      def Manager_update(self, ManagerID, Name, Age, Nationalty, Height, PlaceOfBirth):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Manager Set Name=%s, Age=%s, Nationalty=%s, Height=%s, PlaceOfBirth=%s Where ID=%s;"""
               cursor.execute(statement,([Name, Age, Nationalty, Height, PlaceOfBirth, ManagerID]))

   This method updates managers.
    
   .. code-block:: python

      def Manager_delete(self, ManagerID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ DELETE FROM Manager WHERE ID = %s;"""
               cursor.execute(statement,[ManagerID])

   This method deletes managers.
    
   .. code-block:: python

      def Team(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=Teams.ID and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

      def Player(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,TeamID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID ORDER BY PlayerName,Teamname ASC;"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list
      
      def Goal(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Goal.ID, PlayerName, MatchID,Minute FROM Goal,Fixtures,Player WHERE Goal.ID=Goal.ID and Player.ID=PlayerID and MatchID=Fixtures.ID ORDER BY PlayerID,MatchID ASC;"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

      def Manager(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Manager.id, Name, Age,Nationalty,height,placeofbirth, Teamname,Teams.id FROM Manager,teams Where ManagerID=manager.id ORDER BY Name"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   These methods are used for getting all teams, players, goals, and managers by join operation.
    
   .. code-block:: python

      def Goal_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Goal where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list
      
      def Manager_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Manager where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

      def Team_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Teams where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

      def Player_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Player where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

   These methods are used for getting information of goals, managers, players, teams that will be updated and show in the .html page.
    
   .. code-block:: python

      def Player_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=%s and Teams.ID=TeamID ORDER BY Teamname ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list
      
      def Team_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=%s and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list
      
      def Goal_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Goal.ID, PlayerName, MatchID,Minute FROM Goal,Fixtures,Player WHERE Goal.ID=%s and Player.ID=PlayerID and MatchID=Fixtures.ID ORDER BY PlayerID,MatchID ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list
      
      def Manager_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname from manager left join teams on manager.id = teams.managerid where manager.id=%s Order By Name"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method are used for accessing indivual tuple by its primal key.
    
   .. code-block:: python
	
      def Top_goal(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID, PlayerName, count(PlayerID),Position,Teamname,Player.TeamID FROM Goal,Player,Teams WHERE Goal.ID=Goal.ID and Player.ID=PlayerID and Player.TeamID=Teams.ID Group BY PlayerName,player.id,Teams.Teamname ORDER BY count(PlayerID) DESC;"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used to show top goal players in user mode by countig each player how many goal that they have.
    
   .. code-block:: python

      def Manager_user(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname, teams.id from manager left join teams on manager.id = teams.managerid where manager.id=manager.id Order By Name"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used for showing all managers with their teams by joining Teams and Manager table in user mode.
    
   .. code-block:: python

      def Team_user_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Teams.ID,Teamname,NickName,ShortName,FoundationDate,Name,Location, ManagerID FROM Teams,Manager WHERE Teams.ID=%s and Manager.ID=ManagerID ORDER BY Teamname ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used for accessing one single team by their primal key, and to show its manager, I used joined Manager table and Teams table.
    
   .. code-block:: python

      def Player_team_user(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID and Teams.ID=%s  ORDER BY Teamname ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method gets all informations about all player in one team, and that one team will be accessed by user using key accessing.
    
   .. code-block:: python

      def Player_team(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID,PlayerName,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth,Teamname,Teams.ID FROM Player,Teams WHERE Player.ID=Player.ID and Teams.ID=TeamID and Teams.ID=%s  ORDER BY Teamname ASC;"""
               cursor.execute(statement, [Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method gets all informations about all player in one team, and that one team will be accessed by developer using key accessing.
    
   .. code-block:: python

      def Goal_user(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select distinct Goal.ID, PlayerName, Teamname,  Goal.Minute, Fixtures.id, Goal.MatchID,PlayerID,teams.id FROM Goal,Fixtures,Player,MatchDetails,Teams 
                           WHERE Goal.ID=Goal.id and Player.ID=PlayerID 
                           and Goal.MatchID=Fixtures.ID and Player.TeamID=Teams.id and fixtures.id=%s
                           ORDER BY Goal.Minute ASC;"""
               cursor.execute(statement,[Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method shows goal in user live match page.
    
   .. code-block:: python

      def Player_fixture_team(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Player.ID,PlayerName,Teamname,PlayerAge,Position,PlayerNationalty,PlayerHeight,PlaceOfBirth, Fixtures.HomeTeam, Fixtures.ID,Player.TeamID  From Player, Fixtures, Teams Where ((Teams.ID=Fixtures.HomeTeam and Player.TeamID=Fixtures.HomeTeam) 
               or (Teams.ID=Fixtures.AwayTeam and Player.TeamID=Fixtures.AwayTeam))
               and Fixtures.ID=%s Order By Teamname"""
               cursor.execute(statement,[Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used for showing each teams' players in live match page.
    
   .. code-block:: python

      def Fixture_team_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select distinct Fixtures.ID,T1.Teamname ,T2.Teamname,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName,HomeTeam,AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee 
               WHERE (( T1.ID=HomeTeam AND T2.ID=AwayTeam and Fixtures.Hometeam=T1.ID and HomeTeam=T1.ID) )  
               AND Refereeid=Referee.id  and (T1.ID=%s or T2.ID=%s)  ORDER BY MatchDate,Time"""
               cursor.execute(statement,[Key,Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used for when accessing a team by key access in order to show teams' played or unplayed matches.
    
   .. code-block:: python

      def Manager_team_key(self,Key):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """SELECT manager.id, manager.name, manager.age, manager.nationalty, manager.height, manager.placeofbirth, teams.teamname, Teams.ID from manager left join teams on manager.id = teams.managerid 
               where manager.id=manager.id and Teams.ManagerID=Manager.ID and Teams.ID=%s Order By Name"""
               cursor.execute(statement,[Key])
               cursor_list=cursor.fetchall()
               return cursor_list

   This method used for when accessing a team by key access in order to show teams' managers.
    
   .. code-block:: python

      @app.route("/add_team", methods=['GET','POST'])
      @login_required
      def team_adding_page():
         if not current_user.is_admin:
            abort(401)
         if request.method == 'GET':
            obje = forms.FootballStats()
            managerCursor=obje.Manager()
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

   In this method, if our method is post, we get the form information and we add new team.

   .. code-block:: python

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
   

   In this method, if we enter the team page with get method, we list information of teams. If it is post, we investigate the button value. If the value is add we go to team adding page, if it is delete, we call team delete method. In the other possibility we go to team update page by calling team information method that gets the information of team that will be updated. 

   .. code-block:: python
      
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
   
   If our method is post, we get the form information and we add new player.

   .. code-block:: python
      
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
   
   In this method, if we enter the player page with get method, we list information of players. If it is post, we investigate the button value. If the value is add we go to player adding page, if it is delete, we call player delete method. In the other possibility we go to player update page by calling player information method that gets the information of player that will be updated. 

   .. code-block:: python
      
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

   If our method is post, we get the form information and we add new manager.

   .. code-block:: python
      
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

   In this method, if we enter the manager page with get method, we list information of managers. If it is post, we investigate the button value. If the value is add we go to manager adding page, if it is delete, we call manager delete method. In the other possibility we go to manager update page by calling manager information method that gets the information of manager that will be updated. 

   .. code-block:: python
      
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

   If our method is post, we get the form information and we add new goal.

   .. code-block:: python
      
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
   
   In this method, if we enter the goal page with get method, we list information of goals. If it is post, we investigate the button value. If the value is add we go to goal adding page, if it is delete, we call goal delete method. In the other possibility we go to goal update page by calling goal information method that gets the information of goal that will be updated. 

   .. code-block:: python
     
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
            managerCursor = obje.Manager()
            print(cursor)
            return render_template("update_team.html",cursor=[cursor, managerCursor])
   
   If our method is post, we update the team, player, goal or manager according the id value received as a parameter.

   .. code-block:: python
      
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
   
   This method creates a page for single team with its players, stadium, manager, fixture informations by using key access when form is GET. When form is post, since all of the team, players, stadium, manager, fixture buttons which are delete, add, update are directed to the its right function.

   .. code-block:: python
      
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

   In this method is used for creating pages for single tuples by using key access. In POST form Delete, add, update are same as methods that do not have key access. 

   .. code-block:: python
      
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
   
   These methods are used for creating user players, managers, teams, and top goal pages.

   .. code-block:: python
      
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
   
   These methods are used for creating user players, managers, teams, and top goal pages. These function perform key access, and teams_user_page not only show teams' informations but also shows that team's manager, stadium, players, and played or unplayed matches.

   .. code-block:: python
      
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

   This method creates a live match page in order to control matches by developer. Cursor used for showing details, players, current fixture state, etc. to show current state of match to developer. 
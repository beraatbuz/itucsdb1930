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

    If our method is post, we get the form information and we add new team.
  
Developer Guide
===============

Database Design
---------------

**explain the database design of your project**

**include the E/R diagram(s)**

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

      def Stadium(self):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """Select Stadium.id, Teamname, StadiumName, capacity,built,pitchsize,surface,team_id FROM Stadium,teams Where Teams.id=team_id ORDER BY Teamname"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

   This code get all statistic from db by joining Referee table to show referee’s name.

   .. code-block:: python
	
      def Stadium_add(self, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Stadium(Team_ID,Stadiumname,Capacity,Built,PitchSize,Surface) VALUES(%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface]))

   This method adds new statistic for the match

   .. code-block:: python
	
      def Stadium_delete(self,StadiumId):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Delete From Stadium Where ID = %s;"""
               cursor.execute(statement,([StadiumId]))

   This method deletes the statistic according to id value.

   .. code-block:: python

      def Stadium_update(self, StadiumId, TeamId, StadiumName, Capacity, Built, PitchSize, Surface):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Stadium Set Team_ID=%s, Stadiumname=%s, Capacity=%s, Built=%s, PitchSize=%s, Surface=%s Where ID=%s;"""
               cursor.execute(statement,([TeamId, StadiumName, Capacity, Built, PitchSize, Surface, StadiumId]))

   This query updates the statistic that exists before

   .. code-block:: python

      def Stadium_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Stadium where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

   To get information of statistic that will be updated and show in the .html page, we use this method.

.. toctree:

   Muhammed Enes Tırnakçı
   Beraat Buz 
   Ahmet Yılmaz

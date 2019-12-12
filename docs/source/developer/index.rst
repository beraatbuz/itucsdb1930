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
               statement = """Select Assist.id,Player.playername,Assist.minute,home.teamname as HomeTeam, away.teamname as AwayTeam,Assist.lasttouch,Assist.format,Assist.goldenassist,Assist.stadiumha, Player.id, HomeTeam,Awayteam,MatchID FROM Assist, Player,Teams as home, Teams as away, Fixtures 
               where Assist.playerid = Player.id and Assist.matchid = fixtures.id
               and home.id=fixtures.hometeam
               and away.id=fixtures.awayteam ORDER BY fixtures.ID"""
               cursor.execute(statement)
               cursor_list=cursor.fetchall()
               return cursor_list

	.. code-block:: python		
      def Assist_add(self, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ INSERT INTO Assist(PlayerId,MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA) VALUES(%s,%s,%s,%s,%s,%s,%s);"""
               cursor.execute(statement,([PlayerId, MatchId,Minute,LastTouch,Format,GoldenAssist,StadiumHA]))

   .. code-block:: python
      def Assist_delete(self, AssistId):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Delete From Assist Where ID = %s; """
               cursor.execute(statement,([AssistId]))

   .. code-block:: python

      def Assist_update(self, AssistId, PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement="""Update Assist Set PlayerID=%s, MatchID=%s, Minute=%s, LastTouch=%s, Format=%s,GoldenAssist=%s,StadiumHA=%s Where ID=%s;"""
               cursor.execute(statement,([PlayerId, MatchId, Minute, LastTouch, Format, GoldenAssist, StadiumHA, AssistId]))

   .. code-block:: python
      def Assist_update_info(self, ID):
         with dbapi.connect(url) as connection:
            with connection.cursor() as cursor:
               statement = """ Select * From Assist where ID = %s;"""
               cursor.execute(statement,([ID]))
               cursor_list=cursor.fetchall()
               return cursor_list

.. toctree:

   Muhammed Enes Tırnakçı
   Beraat Buz 
   Ahmet Yılmaz

import psycopg2 as dbapi
import os

url = "postgres://ydsnhphm:afmHtP2dhNoOfJQA7f_aX7YaaF9GMKWP@salt.db.elephantsql.com:5432/ydsnhphm"

class FootballStats:

	def Team_add(self, TeamName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Teams(Teamname) VALUES(%s);"""
				cursor.execute(statement,([TeamName]))
				
	def Stadium_add(self, TeamId, StadiumName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Stadium(Team_ID,Stadiumname) VALUES(%s,%s);"""
				cursor.execute(statement,([TeamId, StadiumName]))
	
	def Assist_add(self, PlayerId, MatchId, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Assist(PlayerId,MatchId,Minute) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId,Minute]))
	
	def Admins_add(self, UserName, UserPassword):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO ADMINS(UserName,UserPassword) VALUES(%s,%s);"""
				cursor.execute(statement,([UserName, UserPassword]))
	
	def Goal_add(self, PlayerId, MatchId, Minute):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Goal(PlayerId, MatchId, Minute) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId,Minute]))
	
	def Statistic_add(self, MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Statistic(MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName]))

	def Referee_add(self, RefereeName, TotalMatch, TotalRedCard, TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Referee(RefereeName, TotalMatch, TotalRedCard, TotalYellowCard) VALUES(%s,%s,%s,%s);"""
				cursor.execute(statement,([RefereeName, TotalMatch, TotalRedCard, TotalYellowCard]))

	def Player_add(self, PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """
                                INSERT INTO Player(PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID]))

	def Manager_add(self, Name, Age, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Manager(Name, Age, TeamID) VALUES(%s,%s,%s);"""
				cursor.execute(statement,([Name, Age, TeamID]))			

	def Fixtures_add(self, HomeTeam, AwayTeam, Week, StadiumID, RefereeID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Fixtures(HomeTeam, AwayTeam, Week, StadiumID, RefereeID) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([HomeTeam, AwayTeam, Week, StadiumID, RefereeID]))

	def Standings_add(self, TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Standings(TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points]))

	def Team(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Teams ORDER BY Teamname"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				#cursor_tuple=()
				#cursor_list=list(cursor_tuple)
				#for id,Teamname in cursor:
					#cursor_list.append(Teamname)
					#print('%(tt)s: %(nm)s' % {'tt': id, 'nm': Teamname})
				return cursor_list

	def Player(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Player ORDER BY PlayerName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Goal(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Goal ORDER BY PlayerID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Stadium(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Stadium ORDER BY Stadiumname"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Assist(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Assist ORDER BY PlayerID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Statistic(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Statistic ORDER BY MatchID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Standings(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Standings ORDER BY TeamID"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list
	
	def Fixtures(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Fixtures ORDER BY Week"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Referee(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Referee ORDER BY RefereeName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Manager(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Manager ORDER BY Name"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

	def Player_delete(self, Name):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ DELETE FROM PLAYER WHERE PlayerName = Name """
				cursor.execute(statement)	
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
	
	def Assist_add(self, PlayerId, MatchId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Assist(PlayerId,MatchId) VALUES(%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId]))
	
	def Admins_add(self, UserName, UserPassword):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO ADMINS(UserName,UserPassword) VALUES(%s,%s);"""
				cursor.execute(statement,([UserName, UserPassword]))
	
	def Goal_add(self, PlayerId, MatchId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Goal(UserName,UserPassword) VALUES(%s,%s);"""
				cursor.execute(statement,([PlayerId, MatchId]))
	
	def Statistic_add(self, MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Statistic(MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([MatchID, HScore, HPossesion, HCorner, HInjure, HFoul, HOffside, HShot, HShotOnTarget, HShotAccuracy, HPassAccuracy, AScore, APossesion, ACorner, AInjure, AFoul, AOffside, AShot, AShotOnTarget, AShotAccuracy, APassAccuracy, Referee_UserName]))

	def Referee_add(self, RefereeName, TotalMatch, TotalRedCard, TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Referee(RefereeName, TotalMatch, TotalRedCard, TotalYellowCard) VALUES(%s,%s,%s,%s);"""
				cursor.execute(statement, ([RefereeName, TotalMatch, TotalRedCard, TotalYellowCard]))

	def Player_add(self, PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Player(PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement, ([PlayerName, PlayerAge, PlayerNationalty, PlayerHeight, TeamID]))

	def Manager_add(self, Name, Age, TeamID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Player(Name, Age, TeamID) VALUES(%s,%s,%s);"""
				cursor.execute(statement, ([Name, Age, TeamID]))			

	def Fixtures_add(self, HomeTeam, AwayTeam, Week, StadiumID, RefereeID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Fixtures(HomeTeam, AwayTeam, Week, StadiumID, RefereeID) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement, ([HomeTeam, AwayTeam, Week, StadiumID, RefereeID]))

	def Standings_add(self, TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """INSERT INTO Standings(TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement, ([TeamID, Played, Won, Drawn, Lost, Goals_for, Goals_against, Goals_difference, Points]))

	def Team(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Teams ORDER BY Teamname"""
				cursor.execute(statement)
				cursor_tuple=()
				cursor_list=list(cursor_tuple)
				for id,Teamname in cursor:
					cursor_list.append(Teamname)
					#print('%(tt)s: %(nm)s' % {'tt': id, 'nm': Teamname})
				return cursor_list

	def Player(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Teams ORDER BY PlayerName"""
				cursor.execute(statement)
				cursor_tuple=()
				cursor_list=list(cursor_tuple)
				for id,PlayerName in cursor:
					cursor_list.append(PlayerName)
					#print('%(tt)s: %(nm)s' % {'tt': id, 'nm': PlayerName})
				return cursor_list
 

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
	
	def Matches_add(self, HomeTeam, AwayTeam):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Matches(HomeTeam,AwayTeam) VALUES(%s,%s);"""
				cursor.execute(statement,([HomeTeam, AwayTeam]))
				
	
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


 

import psycopg2 as dbapi
import os

url = "postgres://ydsnhphm:afmHtP2dhNoOfJQA7f_aX7YaaF9GMKWP@salt.db.elephantsql.com:5432/ydsnhphm"

class FootballStats:

	def Team_add(self, TeamName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO  Teams(Teamname) VALUES(%s);"""
				cursor.execute(statement,([TeamName]))
				
	def Stadium_add(self, TeamId, StadiumName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO  Stadium(Team_ID,Stadiumname) VALUES(%s,%s);"""
				cursor.execute(statement,(TeamId, StadiumName))

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


 

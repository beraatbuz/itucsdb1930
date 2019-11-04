import psycopg2 as dbapi
import os

url = "postgres://ydsnhphm:afmHtP2dhNoOfJQA7f_aX7YaaF9GMKWP@salt.db.elephantsql.com:5432/ydsnhphm"

class FootballStats:
	
	def Team_add(self, TeamName):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO  Teams(Teamname) VALUES(%s)"""
				cursor.execute(statement,(TeamName))
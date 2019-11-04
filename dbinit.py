import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [

			""" 
			CREATE TABLE Matches
			(
				ID serial,
				HomeTeam integer NOT NULL,
				AwayTeam integer NOT NULL,
				PRIMARY KEY (ID)
			)
			""",
			
			"""CREATE TABLE Assist
			(
				ID serial NOT NULL,
				PlayerID integer,
				MatchID integer,
				PRIMARY KEY (ID),
				FOREIGN KEY PlayerID REFERENCES Player (ID),
				FOREIGN KEY MatchID REFERENCES Matches (ID)
			)""",
			
			""" 
			CREATE TABLE public."ADMINS"
			(
				UserName VARCHAR(10) NOT NULL,
				ID serial ,
				"UserPassword" VARCHAR(16) NOT NULL,
				PRIMARY KEY (ID)
			)
			""",
			
			""" 
			CREATE TABLE Goal
			(
				ID serial,
				PlayerID integer,
				MatchID integer,
				PRIMARY KEY (ID),
				FOREIGN KEY PlayerID REFERENCES Player (ID),
				FOREIGN KEY MatchID REFERENCES Matches (ID)
			) 
			""",
			
			
			"""
			CREATE TABLE Statistic
			(
				ID serial,
				MatchID integer NOT NULL,
				HScore integer DEFAULT 0,
				HPossesion integer DEFAULT 0,
				HCorner integer DEFAULT 0,
				HInjure integer DEFAULT 0,
				HFoul integer DEFAULT 0,
				HOffside integer DEFAULT 0,
				HShot integer DEFAULT 0,
				HShotOnTarget integer DEFAULT 0,
				HShotAccuracy integer DEFAULT 0,
				HPassAccuracy integer DEFAULT 0,
				AScore integer DEFAULT 0,
				APossesion integer DEFAULT 0,
				ACorner integer DEFAULT 0,
				AInjure integer DEFAULT 0,
				AFoul integer DEFAULT 0,
				AOffside integer DEFAULT 0,
				AShot integer DEFAULT 0,
				AShotOnTarget integer DEFAULT 0,
				AShotAccuracy integer DEFAULT 0,
				APassAccuracy integer DEFAULT 0,
				Referee UserName VARCHAR(30),
				PRIMARY KEY (ID)
				FOREIGN KEY MatchID REFERENCES Matches (ID)
			)
			"""
			
			
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)

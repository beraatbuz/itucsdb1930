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
				PRIMARY KEY (ID),
				FOREIGN KEY HomeTeam,AwayTeam REFERENCES Teams (ID)
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
			""",
                        
                        """
                        CREATE TABLE Teams
                        (
                                ID SERIAL PRIMARY KEY,
                                Teamname VARCHAR(30) NOT NULL
                        )
                        """,
                        
                        """
                        CREATE TABLE Stadium
                        (
                                ID SERIAL PRIMARY KEY,
                                TeamID INTEGER NOT NULL,
                                Stadiumname VARCHAR(30) NOT NULL,
                                FOREIGN KEY TeamID REFERENCES Teams (ID)
                        )
                        """,

                        """
                        CREATE TABLE Refree
                        (
                                ID SERIAL PRIMARY KEY,
                                name VARCHAR(30),
                                matches INTEGER,
                                Redcard INTEGER,
                                Yellowcard INTEGER
                        )
                        """,
                        """
                        CREATE TABLE Standings
                        (
                                ID SERIAL PRIMARY KEY,
                                TeamID INTEGER NOT NULL,
                                Played INTEGER NOT NULL,
                                Won INTEGER NOT NULL,
                                Drawn INTEGER NOT NULL,
                                Lost INTEGER NOT NULL,
                                Goals_for INTEGER NOT NULL,
                                Goals_against INTEGER NOT NULL,
                                Goals_difference INTEGER NOT NULL,
                                Point INTEGER NOT NULL,
                                FOREIGN KEY TeamID REFERENCES Teams (ID)
                        )
                        """,

                         """
                        CREATE TABLE Fixtures
                        (
                                ID SERIAL PRIMARY KEY,
                                Hometeam INTEGER NOT NULL,
                                Awayteam INTEGER NOT NULL,
                                Week INTEGER NOT NULL,
                                StadiumID INTEGER,
                                RefreeID INTEGER,
                                FOREIGN KEY Hometeam,Awayteam REFERENCES Teams (ID),
                                FOREIGN KEY StadiumID REFERENCES Stadium (ID),
                                FOREIGN KEY RefreeID REFERENCES Refree (ID)
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

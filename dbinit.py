import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
                        """
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS Teamname VARCHAR(30) NOT NULL;
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS NickName VARCHAR(30);
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS ShortName VARCHAR(30) NOT NULL;
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS FoundationDate VARCHAR(30);
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS Capacity INTEGER NOT NULL;
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS ManagerID INTEGER REFERENCES Manager (ID);
                        ALTER TABLE Teams ADD COLUMN IF NOT EXISTS Location VARCHAR(50);

                        CREATE TABLE IF NOT EXISTS  Teams
                        (
                                ID SERIAL PRIMARY KEY,
                                Teamname VARCHAR(30) NOT NULL,
                                NickName VARCHAR(30),
                                ShortName VARCHAR(30) NOT NULL,
                                FoundationDate VARCHAR(30),	
                                ManagerID INTEGER REFERENCES Manager (ID),
                                Location VARCHAR(50)
                        )
                        """,
                        
                        """
                        ALTER TABLE Stadium ADD COLUMN IF NOT EXISTS Capacity INTEGER NOT NULL;
                        ALTER TABLE Stadium ADD COLUMN IF NOT EXISTS Built INTEGER NOT NULL;
                        ALTER TABLE Stadium ADD COLUMN IF NOT EXISTS PitchSize VARCHAR(10) NOT NULL;
                        ALTER TABLE Stadium ADD COLUMN IF NOT EXISTS Surface VARCHAR(10) NOT NULL;

                        CREATE TABLE IF NOT EXISTS  Stadium
                        (
                                ID SERIAL PRIMARY KEY,
                                Team_ID INTEGER NOT NULL REFERENCES Teams (ID),
                                Stadiumname VARCHAR(30) NOT NULL,
                                Capacity INTEGER NOT NULL,
                                Built INTEGER NOT NULL,
                                PitchSize VARCHAR(10) NOT NULL,
                                Surface VARCHAR(10) NOT NULL
                        )
                        """,

                        

                        """
                        ALTER TABLE Referee ADD COLUMN IF NOT EXISTS Age INTEGER;
                        ALTER TABLE Referee ADD COLUMN IF NOT EXISTS RefereeName VARCHAR(30);
                        ALTER TABLE Referee ADD COLUMN IF NOT EXISTS TotalMatch INTEGER;
                        ALTER TABLE Referee ADD COLUMN IF NOT EXISTS TotalRedCard INTEGER;
                        ALTER TABLE Referee ADD COLUMN IF NOT EXISTS TotalYellowCard INTEGER;                                
                        CREATE TABLE IF NOT EXISTS  Referees
                        (
                                ID SERIAL PRIMARY KEY,
                                RefereeName VARCHAR(30),
                                Age INTEGER,
                                TotalMatch INTEGER,
                                TotalRedCard INTEGER,
                                TotalYellowCard INTEGER
                        )
                        """,
                        """
                        CREATE TABLE IF NOT EXISTS  Standings
                        (
                                ID SERIAL PRIMARY KEY,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID),
                                Played INTEGER NOT NULL,
                                Won INTEGER NOT NULL,
                                Drawn INTEGER NOT NULL,
                                Lost INTEGER NOT NULL,
                                Goals_for INTEGER NOT NULL,
                                Goals_against INTEGER NOT NULL,
                                Goals_difference INTEGER NOT NULL,
                                Points INTEGER NOT NULL
                        )
                        """,

                         """
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS MatchDate VARCHAR(30);
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS Refereeid INTEGER;
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS Status VARCHAR(30) NOT NULL;
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS Time VARCHAR(30);
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS  HomeScore VARCHAR(2) DEFAULT '-';
                        ALTER TABLE Fixtures ADD COLUMN IF NOT EXISTS AwayScore VARCHAR(2) DEFAULT '-';
                        ALTER TABLE Fixtures DROP COLUMN IF EXISTS StadiumID;
                        ALTER TABLE Fixtures DROP COLUMN IF EXISTS HomeTScore;
                        ALTER TABLE Fixtures DROP COLUMN IF EXISTS AwayTScore;
                        
                        CREATE TABLE IF NOT EXISTS  Fixtures
                        (
                                ID SERIAL PRIMARY KEY,
                                HomeTeam INTEGER NOT NULL REFERENCES Teams (ID),
                                AwayTeam INTEGER NOT NULL REFERENCES Teams (ID),
                                Refereeid INTEGER REFERENCES Referee (ID),
                                HomeScore VARCHAR(2) DEFAULT '-',
                                AwayScore VARCHAR(2) DEFAULT '-',
                                Week INTEGER NOT NULL,
                                MatchDate VARCHAR(30),
                                Time VARCHAR(30),
                                Status VARCHAR(10) NOT NULL
                        )
                        """,
                        """
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerAge INTEGER;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerNationalty VARCHAR(30) NOT NULL;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlayerHeight INTEGER NOT NULL;
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS Position VARCHAR(30);
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS TeamID INTEGER NOT NULL REFERENCES Teams (ID);
                        ALTER TABLE Player ADD COLUMN IF NOT EXISTS PlaceOfBirth VARCHAR(30) NOT NULL;
                                
                        CREATE TABLE IF NOT EXISTS  Player
                        (
                                ID SERIAL PRIMARY KEY,
                                PlayerName VARCHAR(30) NOT NULL,
                                PlayerAge INTEGER NOT NULL,
                                Position VARCHAR(30),
                                PlayerNationalty VARCHAR(30) NOT NULL,
                                PlayerHeight INTEGER NOT NULL,
                                PlaceOfBirth VARCHAR(30) NOT NULL,
                                TeamID INTEGER NOT NULL REFERENCES Teams (ID)
                        )
                        """,
			
			"""
                        ALTER TABLE Assist ADD COLUMN IF NOT EXISTS Minute INTEGER NOT NULL;

                        CREATE TABLE IF NOT EXISTS  Assist
			(
				ID serial NOT NULL,
				PlayerID integer REFERENCES Player (ID),
				MatchID integer  REFERENCES Fixtures (ID),
                                Minute INTEGER NOT NULL,
                                LastTouch VARCHAR(10) NOT NULL,
                                Format VARCHAR(15) NOT NULL,
                                GoldenAssist VARCHAR(3) NOT NULL,
                                StadiumHA VARCHAR(5) NOT NULL,
				PRIMARY KEY (ID)
			)""",
			
			""" 
			CREATE TABLE IF NOT EXISTS ADMINS
			(
				UserName VARCHAR(10) NOT NULL,
				ID serial ,
				UserPassword VARCHAR(16) NOT NULL,
				PRIMARY KEY (ID)
			)
			""",
			
			""" 
                        ALTER TABLE Goal ADD COLUMN IF NOT EXISTS Minute INTEGER NOT NULL;
                        ALTER TABLE Goal ADD COLUMN IF NOT EXISTS MatchID integer NOT NULL REFERENCES Fixtures (ID);
                        ALTER TABLE Goal ADD COLUMN IF NOT EXISTS PlayerID integer NOT NULL REFERENCES Player (ID);

			CREATE TABLE IF NOT EXISTS  Goal
			(
				ID serial,
				PlayerID integer NOT NULL REFERENCES Player (ID),
				MatchID integer NOT NULL REFERENCES Fixtures (ID),
                                Minute INTEGER NOT NULL,
				PRIMARY KEY (ID)
			) 
			""",
			
			
			"""
			CREATE TABLE IF NOT EXISTS  Statistic
			(
				ID serial,
				MatchID integer NOT NULL  REFERENCES Fixtures (ID),
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
				Referee_UserName VARCHAR(30),
				PRIMARY KEY (ID)
			)
			""",

                        """
                        ALTER TABLE Manager ADD COLUMN IF NOT EXISTS Name VARCHAR(30) NOT NULL;
                        ALTER TABLE Manager ADD COLUMN IF NOT EXISTS Age INTEGER NOT NULL;
                        ALTER TABLE Manager ADD COLUMN IF NOT EXISTS Nationalty VARCHAR(30) NOT NULL;
                        ALTER TABLE Manager ADD COLUMN IF NOT EXISTS Height INTEGER NOT NULL;
                        ALTER TABLE Manager ADD COLUMN IF NOT EXISTS PlaceOfBirth VARCHAR(30) NOT NULL;
                        
                        CREATE TABLE IF NOT EXISTS  Manager
                        (
                                ID SERIAL PRIMARY KEY,
                                Name VARCHAR(30) NOT NULL,
                                Age INTEGER NOT NULL,
                                Nationalty VARCHAR(30) NOT NULL,
                                Height INTEGER NOT NULL,
                                PlaceOfBirth VARCHAR(30) NOT NULL
                        
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
    url = os.getenv("url")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)

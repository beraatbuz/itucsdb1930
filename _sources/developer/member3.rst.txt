Parts Implemented by Beraat Buz
================================

Database Design
---------------

**explain the database design of your project**

   .. figure:: er.png
         :scale: 50 %
         :alt: E/R Diagram 


Code
----

**explain the technical structure of your code**

**to include a code listing, use the following example**:

   .. code-block:: python

        lm = LoginManager()

		@lm.user_loader
		def load_user(user_id):
			return get_user(user_id)

		app = Flask(__name__)
		app.config['SECRET_KEY'] = 'ThisisSecret'
		app.config.from_object("settings")
		@app.route("/")
		def home_page():
			 logout_user()
			 return redirect(url_for("fixture_user_page"))
		class LoginForm(FlaskForm):
			username = StringField("Username", validators=[DataRequired()])
			password = PasswordField("Password", validators=[DataRequired()])

		@app.route("/login",methods=['GET', 'POST'])
		def login_page():
			form = LoginForm()
			if form.is_submitted(): 
				username = form.data["username"]
				user = get_user(username)
				if user is not None: 
					password = form.data["password"]
					if hasher.verify(password, user.password):
						login_user(user)
						flash("You have logged in.")
						next_page = request.args.get("next", url_for("fixture_page"))
						return redirect(next_page)
				flash("Invalid credentials.")
				#abort(401)
			return render_template("login.html", form=form)

   This code is required for login and login page. ınput validation is done. Hasher is used to hide the password.

   .. code-block:: python

		@app.route("/fixture_user", methods=['GET','POST'])
		def fixture_user_page():
			obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Fixtures(1)
				return render_template("user-fixture.html",cursor=cursor)
			else:
				process = request.form.get('buttonName')
				week = request.form.get('select') 
				cursor=obje.Fixtures(week)
				return render_template("user-fixture.html",cursor=cursor)

   This code is required for fixture page at user side.

   .. code-block:: python

      def Fixtures(self,week):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName, HomeTeam, AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee WHERE Week = %s AND T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id ORDER BY MatchDate,Time;"""
				cursor.execute(statement,([week]))
				cursor_list=cursor.fetchall()
				return cursor_list

   This code is required for fixture page at user side for week selection and table creation. The cursor is used in HTML file.

   .. code-block:: python

      @app.route("/referee_user", methods=['GET'])
	  def referee_user_page():
		 obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Referee()
				return render_template("user-referee.html",cursor=cursor)

   This code is required for referee page at user side.

   .. code-block:: python

      def Referee(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select * FROM Referee ORDER BY RefereeName"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

   This code is required for referee page at user side for table creation. The cursor is used in HTML file.

   .. code-block:: python

      @app.route("/standing_user", methods=['GET'])
		def standing_user_page():
			obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Standings()
				return render_template("user-standing.html",cursor=cursor)

   This code is required for standing table page at user side.

   .. code-block:: python

      def Standings(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Standings.ID,TeamName,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points, Teams.id FROM Standings,Teams WHERE Teams.ID=TeamID ORDER BY Points DESC,Goals_difference DESC,TeamName;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

   This code is required for standing page at user side for table creation. The cursor is used in HTML file.

   .. code-block:: python
	
        @app.route("/fixture", methods=['GET','POST'])
		@login_required
		def fixture_page():
			if not current_user.is_admin:
				abort(401)
			obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Fixtures(1)
				return render_template("fixture.html",cursor=cursor)
			else:
				process = request.form.get('buttonName')
				processStart = request.form.get('Start')
				processLive = request.form.get('Live')
				update = request.form.get('Update')
				if (process == "add"):
					return redirect(url_for("fixture_adding_page"))
				elif (processStart):
					return fixture_update_page(processStart)
				elif (processLive):
					return live_match_page(processLive)
				elif (process == "week"):
					week = request.form.get('select') 
					cursor=obje.Fixtures(week)
					return render_template("fixture.html",cursor=cursor)

				elif (process == "Delete"):
					form_fixture_keys = request.form.getlist('fixture')
					for form_fixture_key in form_fixture_keys:
						obje.Fixture_delete(int(form_fixture_key))
					return redirect(url_for("fixture_page"))
				else:
					return fixture_update_page(process)

   This code is required for fixture page at administrator side for table creation. Firstly, using GET method creates table for week 1. Then, by clicking desired button operates add, delete, update or starting match operations.

   .. code-block:: python
	
        @app.route("/add_fixture", methods=['GET','POST'])
		@login_required
		def fixture_adding_page():
			obje = forms.FootballStats()
			cursor1=obje.Team()
			cursor2=obje.Referee()
			if not current_user.is_admin:
				abort(401)
			if request.method == 'GET':
				return render_template('add_fixture.html',cursor=[cursor1,cursor2])

			elif request.method == 'POST':
				HomeTeam = request.form["HomeTeam"]
				AwayTeam = request.form["AwayTeam"]
				HomeScore = request.form["HomeScore"]
				AwayScore =  request.form["AwayScore"]
				Week =  request.form["Week"]
				MatchDate =  request.form["MatchDate"]
				Time =  request.form["Time"]
				Status = request.form["Status"]
				Refereeid=request.form["Refereeid"]
				obje = forms.FootballStats()
				obje.Fixture_add(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid)
				flash("You have added.")
				return render_template("add_fixture.html",cursor=[cursor1,cursor2])

   This code is required for fixture adding page at administrator side. Two cursors are used to post input by using selection.

   .. code-block:: python

      def Fixture_add(self, HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Fixtures(HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid]))

   This code is required for fixture adding page at administrator side. This query provides insertion to Fixtures Table.

   .. code-block:: python

		@app.route("/update_fixture", methods=['GET','POST'])
		@login_required
		def fixture_update_page(process):
			obje = forms.FootballStats()
			if not current_user.is_admin:
				abort(401)
			update = request.form.get('Update') 
			if request.method == 'GET':
				return render_template("fixture.html")
			elif request.method == 'POST':
				if update is not None:
					HomeTeam = request.form["HomeTeam"]
					AwayTeam = request.form["AwayTeam"]
					HomeScore = request.form["HomeScore"]
					AwayScore =  request.form["AwayScore"]
					Week =  request.form["Week"]
					MatchDate =  request.form["MatchDate"]
					Time =  request.form["Time"]
					Status = request.form["Status"]
					Refereeid=request.form["Refereeid"]
					obje.Fixture_update(update,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid)
					return redirect(url_for("fixture_page"))
				cursor=obje.Fixture_update_info(process)
				cursor1=obje.Team()
				cursor2=obje.Referee()
				return render_template("update_fixture.html",cursor=[cursor,cursor1,cursor2])

   This code is required for fixture update page at administrator side. Two cursors are used to post input by using selection, one cursor is used to select the row from database we want to update.

   .. code-block:: python

      def Fixture_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Fixtures where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

   To select the row from database we want to update.

   .. code-block:: python

      def Fixture_update(self, FixtureID,HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Fixtures Set HomeTeam=%s, AwayTeam=%s, HomeScore=%s, AwayScore=%s, Week=%s,MatchDate=%s,Time=%s,Status=%s,Refereeid=%s Where ID=%s;"""
				cursor.execute(statement,([HomeTeam,AwayTeam,HomeScore,AwayScore,Week,MatchDate,Time,Status,Refereeid,FixtureID]))

   To update database.

   .. code-block:: python
	
      def Fixture_delete(self,FixtureId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Fixtures Where ID = %s;"""
				cursor.execute(statement,([FixtureId]))

   To delete checked rows.
   
   .. code-block:: python
      
		@app.route("/standing", methods=['GET','POST'])
		@login_required
		def standing_page():
			if not current_user.is_admin:
				abort(401)
			obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Standings()
				return render_template("standing.html",cursor=cursor)
			else:
				process = request.form.get('buttonName')
				update = request.form.get('Update')
				if (process == "add"):
					return redirect(url_for("standing_adding_page"))
				elif (process == "Delete"):
					form_standing_keys = request.form.getlist('standing')
					for form_standing_key in form_standing_keys:
						obje.Standing_delete(int(form_standing_key))
					return redirect(url_for("standing_page"))
				else:
            return standing_update_page(process)

   This code is required for standing page at administrator side for table creation. By clicking desired button operates add, delete or update operations.

   .. code-block:: python
		@app.route("/add_standing", methods=['GET','POST'])
		@login_required
		def standing_adding_page():
			obje = forms.FootballStats()
			cursor1=obje.Team()
			if not current_user.is_admin:
				abort(401)
			if request.method == 'GET':
				return render_template('add_standings.html',cursor=cursor1)

			elif request.method == 'POST':
				TeamID = request.form["TeamID"]
				Played = request.form["Played"]
				Won = request.form["Won"]
				Drawn =  request.form["Drawn"]
				Lost =  request.form["Lost"]
				Goals_for =  request.form["Goals_for"]
				Goals_against =  request.form["Goals_against"]
				obje = forms.FootballStats()
				obje.Standing_add(TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against)
				flash("You have added.")
				return render_template("add_standings.html",cursor=cursor1)
      
   This code is required for standing row adding page at administrator side. The cursor is used to post input by using selection.

   .. code-block:: python
      
      def Standing_add(self, TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Standings(TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,Goals_difference,Points) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn))]))
	

   This query provides insertion to Standings Table.

   .. code-block:: python

        @app.route("/update_standing", methods=['GET','POST'])
		@login_required
		def standing_update_page(process):
			if not current_user.is_admin:
				abort(401)
			obje = forms.FootballStats()
			update = request.form.get('Update') 
			if request.method == 'GET':
				return render_template("standing.html")
			elif request.method == 'POST':
				if update is not None:
					TeamID = request.form["TeamID"]
					Played = request.form["Played"]
					Won = request.form["Won"]
					Drawn =  request.form["Drawn"]
					Lost =  request.form["Lost"]
					Goals_for =  request.form["Goals_for"]
					Goals_against =  request.form["Goals_against"]
					obje = forms.FootballStats()
					obje.Standing_update(update,TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against)
					return redirect(url_for("standing_page"))
				cursor=obje.Standing_update_info(process)
				cursor1=obje.Team()
				return render_template("update_standing.html",cursor=[cursor,cursor1])

   This code is required for standing update page at administrator side. One cursor is used to post input by using selection, one cursor is used to select the row from database we want to update.

   .. code-block:: python

      def Standing_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Standings where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

   To select the row of standing table we want to update.

   .. code-block:: python

      def Standing_update(self, StandingId,TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Standings Set TeamID=%s, Played=%s, Won=%s, Drawn=%s, Lost=%s,Goals_for=%s,Goals_against=%s,Goals_difference=%s,Points=%s Where ID=%s;"""
				cursor.execute(statement,([TeamID,Played,Won,Drawn,Lost,Goals_for,Goals_against,(int(Goals_for)-int(Goals_against)),(3*int(Won)+int(Drawn)),StandingId]))

   This querry updates the row of standings table we have selected.

   .. code-block:: python

      def Standing_delete(self,StandingId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Standings Where ID = %s;"""
				cursor.execute(statement,([StandingId]))

   This querry deletes the row of standings table we have checked.

   .. code-block:: python

        @app.route("/referee", methods=['GET','POST'])
		@login_required
		def referee_page():
			if not current_user.is_admin:
				abort(401)
			obje = forms.FootballStats()
			if request.method == "GET":
				cursor=obje.Referee()
				return render_template("referee.html",cursor=cursor)
			else:
				process = request.form.get('buttonName')
				update = request.form.get('Update')
				if (process == "add"):
					return redirect(url_for("referee_adding_page"))
				if(process == "Delete"):
					form_referee_keys = request.form.getlist('referee')
					for form_referee_key in form_referee_keys:
						print(form_referee_key)
						obje.Referee_delete(int(form_referee_key))
					return redirect(url_for("referee_page"))
				else:
					return referee_update_page(process)

   This code is required for referee page at administrator side for table creation. By clicking desired button operates add, delete or update operations.

   .. code-block:: python

		@app.route("/add_referee", methods=['GET','POST'])
		@login_required
		def referee_adding_page():
			if not current_user.is_admin:
				abort(401)
			if request.method == 'GET':
				return render_template('add_referee.html')

			elif request.method == 'POST':
				RefereeName = request.form["RefereeName"]
				Age = request.form["Age"]
				TotalMatch = request.form["TotalMatch"]
				TotalRedCard =  request.form["TotalRedCard"]
				TotalYellowCard =  request.form["TotalYellowCard"]
				obje = forms.FootballStats()
				obje.Referee_add(RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard)
				flash("You have added.")
				return render_template("add_referee.html")

   This code is required for referee adding page at administrator side.

   .. code-block:: python

      def Referee_add(self, RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ INSERT INTO Referee(RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard) VALUES(%s,%s,%s,%s,%s);"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard]))

   This querry is needed for adding new referee to referee table.

   .. code-block:: python

		@app.route("/update_referee", methods=['GET','POST'])
		@login_required
		def referee_update_page(process):
			if not current_user.is_admin:
				abort(401)
			obje = forms.FootballStats()
			update = request.form.get('Update') 
			if request.method == 'GET':
				return render_template("referee.html")
			elif request.method == 'POST':
				if update is not None:
					RefereeName = request.form["RefereeName"]
					Age = request.form["Age"]
					TotalMatch = request.form["TotalMatch"]
					TotalRedCard =  request.form["TotalRedCard"]
					TotalYellowCard =  request.form["TotalYellowCard"]
					obje = forms.FootballStats()
					obje.Referee_update(update,RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard)
					return redirect(url_for("referee_page"))
				cursor=obje.Referee_update_info(process)
				return render_template("update_referee.html",cursor=cursor)

   This code is required for referee update page at administrator side. The cursor is used to select the row from database we want to update.

   .. code-block:: python
      def Referee_update_info(self, ID):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """ Select * From Referee where ID = %s;"""
				cursor.execute(statement,([ID]))
				cursor_list=cursor.fetchall()
				return cursor_list

   To select the row of referee table we want to update.

   .. code-block:: python

      def Referee_update(self, RefereeID,RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Update Referee Set RefereeName=%s, Age=%s, TotalMatch=%s, TotalRedCard=%s, TotalYellowCard=%s Where ID=%s;"""
				cursor.execute(statement,([RefereeName,Age,TotalMatch,TotalRedCard,TotalYellowCard,RefereeID]))
      
   This querry updates the row of referee table we have selected.	
   
   .. code-block:: python

      def Referee_delete(self,RefereeId):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement="""Delete From Referee Where ID = %s;"""
				cursor.execute(statement,([RefereeId]))

   This querry deletes the row of referee table we have checked.

   .. code-block:: python

      def Fixture_key(self,Key):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName,HomeTeam,AwayTeam,Refereeid FROM Fixtures,Teams AS T1,Teams AS T2,Referee 
				WHERE T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id and Fixtures.id=%s ORDER BY MatchDate,Time;"""
				cursor.execute(statement, [Key])
				cursor_list=cursor.fetchall()
				return cursor_list
	  def Fixtures2(self):
		with dbapi.connect(url) as connection:
			with connection.cursor() as cursor:
				statement = """Select Fixtures.ID,T1.TeamName ,T2.TeamName,Week,MatchDate,Time,HomeScore,AwayScore,Status,RefereeName FROM Fixtures,Teams AS T1,Teams AS T2,Referee WHERE T1.ID=HomeTeam AND T2.ID=AwayTeam AND Refereeid=Referee.id ORDER BY MatchDate,Time;"""
				cursor.execute(statement)
				cursor_list=cursor.fetchall()
				return cursor_list

   These codes is needed other tables which is references to fixture table.


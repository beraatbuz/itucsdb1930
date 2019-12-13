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

   This code is required for login and login page. ınput validation is done. Hasher is used to hide the password

   

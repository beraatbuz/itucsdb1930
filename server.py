from flask import Flask,render_template,request,redirect,url_for,flash,abort,session
from flask_login import LoginManager,login_user,current_user,login_required,logout_user
from user import get_user
from wtforms import Form, BooleanField, StringField, validators,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from passlib.hash import pbkdf2_sha256 as hasher
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
     return render_template("home.html")

@app.route("/dashboard")
@login_required
def dashboard_page():
     if not current_user.is_admin:
        abort(401)
     return render_template("dashboard.html")
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
                next_page = request.args.get("next", url_for("dashboard_page"))
                return redirect(next_page)
        flash("Invalid credentials.")
        #abort(401)
    return render_template("login.html", form=form)
@app.route("/")
def logout_page():
    print("1")
    logout_user()
    flash("You have logged out.")
    return redirect(url_for("home_page"))
lm.init_app(app)
lm.login_view = "login_page"

if __name__ == "__main__":
    app.run(debug=True)

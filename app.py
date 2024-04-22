from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required

from models import Group, User, session
from secure.local import DATABASE_ENGINE, DEBUG_MODE, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_ENGINE
app.config['secret_key'] = SECRET_KEY

# login_manager.setup_app(app)
# login_manager.user_loader(User)
# login_manager.request_loader(User)


# Home route
@app.route('/')
def index():
    context = {}
    return render_template('home/index.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    print(request)
    return render_template('auth/register.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = session.query(User).filter_by(username=username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password'
    return render_template('auth/login.html')


# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    return 'You are logged in.'

if __name__ == '__main__':
    
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    app.run(debug=DEBUG_MODE)
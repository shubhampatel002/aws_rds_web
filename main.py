app = Flask(__name__)

# Group of user-related routes
@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/user/<string:username>')
def user_profile(username):
    return "Welcome " + username

# Group of admin-related routes
@app.route('/admin')
def admin_dashboard():
    return 'Admin dashboard'

@app.route('/admin/settings')
def admin_settings():
    return 'Admin settings page'

if __name__ == '__main__':
    app.run(debug=True)

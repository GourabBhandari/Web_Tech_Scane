from flask import Flask, request, render_template, redirect, url_for, session, flash
import builtwith
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory database for storing user information
users = {}

# Mapping of technologies to their images
tech_images = {
    'LiteSpeed': '/static/images/litespeed.png',
    'Underscore.js': '/static/images/underscore.png',
    'jQuery': '/static/images/jquery.png',
    'WooCommerce': '/static/images/woocommerce.png',
    'WordPress': '/static/images/wordpress.png',
    'PHP': '/static/images/php.png',
    'Apache': 'static/images/apache.png',
    'Nginx': 'static/images/nginx.png',
    'Python': 'static/images/python.png',
    'Ruby': 'static/images/ruby.png',
    'JavaScript': 'static/images/javascript.png',
    'AngularJS': 'static/images/angularjs.png',
    'React': 'static/images/react.png',
    'Vue.js': 'static/images/vue.png',
    'Drupal': 'static/images/drupal.png',
    'Joomla': 'static/images/joomla.png',
    'Magento': 'static/images/magento.png',
    'Shopify': 'static/images/shopify.png',
    'MySQL': 'static/images/mysql.png',
    'PostgreSQL': 'static/images/postgresql.png',
    'MongoDB': 'static/images/mongodb.png',
    'Express': '/static/images/express.png',
    'node.js': '/static/images/nodejs.png',
    'Google Font API': '/static/images/googlefontapi.png',
    'Google Tag Manager': '/static/images/googletagmanager.png',
    'OWL Carousel': '/static/images/owlcarousel.png',
    'Cloudflare': '/static/images/cloudflare.png',
    'Javascript Infovis Toolkit': '/static/images/javascriptinfovis.png',
    'Prototype': '/static/images/prototype.png',
    'RequireJS': '/static/images/requirejs.png',
    'Django': '/static/images/django.png',
    'Flask': '/static/images/flask.png',
    'Ruby on Rails': '/static/images/rubyonrails.png',
    'Spring Boot': '/static/images/springboot.png',
    'ASP.NET': '/static/images/aspnet.png',
    'Bootstrap': '/static/images/bootstrap.png',
    'Foundation': '/static/images/foundation.png',
    'Tailwind CSS': '/static/images/tailwindcss.png',
    'Sass': '/static/images/sass.png',
    'Less': '/static/images/less.png',
    'Gatsby': '/static/images/gatsby.png',
    'Next.js': '/static/images/nextjs.png',
    'Docker': '/static/images/docker.png',
    'Kubernetes': '/static/images/kubernetes.png',
    'AWS': '/static/images/aws.png',
    'Azure': '/static/images/azure.png',
    'Google Cloud': '/static/images/googlecloud.png',
    'Firebase': '/static/images/firebase.png',
    'GraphQL': '/static/images/graphql.png',
    'REST API': '/static/images/restapi.png',
    'GraphQL API': '/static/images/graphqlapi.png',
    'Socket.IO': '/static/images/socketio.png',
    'WebSockets': '/static/images/websockets.png',
    'OAuth': '/static/images/oauth.png',
    'JWT': '/static/images/jwt.png',
    'OAuth2': '/static/images/oauth2.png',
    'CI/CD': '/static/images/cicd.png',
    'Jenkins': '/static/images/jenkins.png',
    'CircleCI': '/static/images/circleci.png',
    'Travis CI': '/static/images/travisci.png',
    'GitLab CI/CD': '/static/images/gitlab.png',
    'GitHub Actions': '/static/images/githubactions.png'

    # Add more mappings as needed
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = {'password': generate_password_hash(password)}
            flash('Registration successful, please log in')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    result = None
    if request.method == 'POST':
        url = request.form['url']
        website = builtwith.parse(url)
        result = {key: ", ".join(value) for key, value in website.items()}
    return render_template('index.html', result=result, tech_images=tech_images)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

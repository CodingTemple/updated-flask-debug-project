from flask import Flask

from config import Config

# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import for Flask Mail
from flask_mail import Mail, Message

# Create flask app variable
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

mail = Mail(app)



from may_blog import routes,models
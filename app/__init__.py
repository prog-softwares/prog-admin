from flask.app import Flask
from flask_admin import Admin
from flask_migrate import Migrate

from app.views.admin import UserView
from app.config import configure_app
from app.models import User, db

app = Flask(__name__)

configure_app(app)

db.init_app(app)

Migrate(app,db)


admin = Admin(app, name='Prog Admin', template_mode='bootstrap3')
admin.add_view(UserView(User, db.session, name='Gestão de usuários', category="Configuração"))
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import wvar_db, wvar_login_manager

class wvar_User(UserMixin, wvar_db.Model):
    __tablename__ = 'wvar_users'
    id = wvar_db.Column(wvar_db.Integer, primary_key=True)
    username = wvar_db.Column(wvar_db.String(64), unique=True, index=True)
    email = wvar_db.Column(wvar_db.String(120), unique=True, index=True)
    password_hash = wvar_db.Column(wvar_db.String(128))
    created_at = wvar_db.Column(wvar_db.DateTime, default=datetime.utcnow)
    
    def wfun_set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def wfun_check_password(self, password):
        return check_password_hash(self.password_hash, password)

@wvar_login_manager.user_loader
def wfun_load_user(user_id):
    return wvar_User.query.get(int(user_id)) 
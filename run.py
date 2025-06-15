import os
from app import wfun_create_app, wvar_db
from app.models import wvar_User

app = wfun_create_app(os.getenv('wvar_ENV', 'development'))

@app.shell_context_processor
def wfun_make_shell_context():
    return dict(db=wvar_db, User=wvar_User)

if __name__ == '__main__':
    with app.app_context():
        wvar_db.create_all()
    app.run(host='0.0.0.0', port=5000) 
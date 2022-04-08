from .credentials import POSTGRES

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test_app.db"
SQLALCHEMY_DATABASE_URL = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

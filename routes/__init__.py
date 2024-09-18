from flask import session, redirect, url_for
from routes.home import home_page
from routes.accounts import accounts_page
from routes.movements import movements_page
from routes.operations import operations_page
#from routes.dashboard import dashboard_page
#from routes.configurations import configurations_page
#from routes.plans import plans_page
from routes.login import login_page
from routes.register import register_page

def init_routes(app):
    # Rotas protegidas por login
    app.add_url_rule('/home', 'home', login_required(home_page))
    app.add_url_rule('/accounts', 'accounts', login_required(accounts_page))
    app.add_url_rule('/movements', 'movements', login_required(movements_page))
    app.add_url_rule('/operacoes', 'operations', login_required(operations_page))
    #app.add_url_rule('/dashboard', 'dashboard', login_required(dashboard_page))
    #app.add_url_rule('/plans', 'plans', login_required(plans_page))
    #app.add_url_rule('/configurations', 'configurations', login_required(configurations_page))

    # Rotas de login e registro
    app.add_url_rule('/', 'login', login_page, methods=['GET', 'POST'])
    app.add_url_rule('/login', 'login_post', login_page, methods=['POST'])  # Verifique esta linha
    app.add_url_rule('/register', 'register', register_page, methods=['GET', 'POST'])

def login_required(f):
    """Decorator que verifica se o usuário está logado."""
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

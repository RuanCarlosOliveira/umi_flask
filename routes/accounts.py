from flask import render_template, session
from database.models import session as db_session, Account


def accounts_page():
    user_id = session.get('user_id')

    # Buscar contas pertencentes ao usuário logado
    accounts = db_session.query(Account).filter_by(user_id=user_id).all()

    return render_template('accounts.html', accounts=accounts)

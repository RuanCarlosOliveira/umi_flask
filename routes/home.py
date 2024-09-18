from flask import render_template, session
from database.models import session as db_session, User

def home_page():
    # Obter o ID do usuário logado a partir da sessão
    user_id = session.get('user_id')

    # Buscar os dados do usuário logado
    user = db_session.query(User).filter_by(id=user_id).first()

    return render_template('home.html', user=user)

from flask import render_template, session
from database.models import session as db_session, Movement


def movements_page():
    user_id = session.get('user_id')

    # Buscar as movimentações do usuário logado
    movements = db_session.query(Movement).filter_by(user_id=user_id).all()

    return render_template('movements.html', movements=movements)

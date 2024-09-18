from flask import render_template, session
from database.models import session as db_session, Operation  # Certifique-se de ter um modelo Operation

def operations_page():
    user_id = session.get('user_id')

    # Buscar as operações do usuário logado
    operations = db_session.query(Operation).filter_by(user_id=user_id).all()

    return render_template('operations.html', operations=operations)

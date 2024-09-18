from flask import render_template, request, jsonify, session
from database.models import session as db_session, User
from werkzeug.security import check_password_hash

def login_page():
    if request.method == 'GET':
        return render_template('login.html', script_name='login.js')

    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Verificar se o usuário existe
        user = db_session.query(User).filter_by(username=username).first()

        if user and check_password_hash(user.password, password):  # Comparando o hash da senha
            session['user_id'] = user.id  # Salvar a sessão do usuário
            return jsonify(success=True)
        else:
            return jsonify(success=False)

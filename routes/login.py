from flask import render_template, request, jsonify, session
from database.models import session as db_session, User
from werkzeug.security import check_password_hash

def login_page():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        print(f"Tentando login para o usuário: {username}")

        # Verificar se o usuário existe
        user = db_session.query(User).filter_by(username=username).first()

        if user:
            print(f"Usuário encontrado: {user.username}")
            print(f"Senha fornecida: {password}")
            print(f"Senha armazenada (hash): {user.password}")

        # Verificar se a senha corresponde ao hash armazenado
        if user and check_password_hash(user.password, password):
            print("Senha correta. Autenticação bem-sucedida.")
            session['user_id'] = user.id
            return jsonify(success=True), 200
        else:
            print("Falha na autenticação. Senha incorreta.")
            return jsonify(success=False), 401  # Retornar 401 Unauthorized para falha no login

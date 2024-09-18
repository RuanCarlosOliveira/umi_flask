from flask import render_template, request, jsonify
from database.models import session as db_session, User
from werkzeug.security import generate_password_hash

def register_page():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        data = request.get_json()

        # Verificar se os campos username e password foram fornecidos
        if not data or 'username' not in data or 'password' not in data:
            print("Dados incompletos.")
            return jsonify(success=False, message="Dados incompletos"), 400

        username = data.get('username')
        password = data.get('password')

        print(f"Recebendo solicitação de registro para: {username}")

        # Verificar se o usuário já existe
        existing_user = db_session.query(User).filter_by(username=username).first()
        if existing_user:
            print(f"Usuário {username} já existe")
            return jsonify(success=False, message="Usuário já existe"), 409

        # Criar novo usuário com senha hash
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db_session.add(new_user)
        print(f"Tentando registrar o usuário {username} no banco de dados...")

        # Tente realizar o commit e capture erros se ocorrerem
        try:
            db_session.commit()
            print(f"Usuário {username} registrado com sucesso")
            return jsonify(success=True), 201
        except Exception as e:
            db_session.rollback()  # Reverter transação no caso de erro
            print(f"Erro ao registrar o usuário: {e}")
            return jsonify(success=False, message="Erro ao registrar o usuário"), 500

        # Verificar se o usuário foi realmente inserido
        user_in_db = db_session.query(User).filter_by(username=username).first()
        if user_in_db:
            print(f"Usuário {username} encontrado no banco após commit.")
        else:
            print(f"Usuário {username} NÃO foi encontrado no banco após commit.")

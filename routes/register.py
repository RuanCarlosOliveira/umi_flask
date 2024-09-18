from flask import render_template, request, jsonify
from database.models import session as db_session, User
from werkzeug.security import generate_password_hash

def register_page():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Verificar se o usuário já existe
        existing_user = db_session.query(User).filter_by(username=username).first()
        if existing_user:
            return jsonify(success=False, message="Usuário já existe")

        # Criar novo usuário com senha hash
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db_session.add(new_user)
        db_session.commit()

        return jsonify(success=True)


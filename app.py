import os, sqlite3
from flask import Flask, render_template, request

# APLICAÇÃO FLASK
app = Flask(__name__)

# APLICAÇÃO SQLITE
n = 0
while n == 0:    
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE CADASTRO (USER_NAME TEXT, USER_EMAIL TEXT, USER_ADDRESS TEXT)')
    conn.close()
    n += 1

# CONTROLLERS
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']

    if nome and email and endereco:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO CADASTRO (USER_NAME, USER_EMAIL, USER_ADDRESS) VALUES (?, ?, ?)', (nome, email, endereco))
        conn.commit()
        return render_template('index.html')

@app.route('/lista', methods=['POST', 'GET'])
def listar():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT USER_NAME, USER_EMAIL, USER_ADDRESS FROM CADASTRO')
    data = cursor.fetchall()
    conn.commit()
    return render_template('lista.html', datas=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='localhost', port=port, debug=True)

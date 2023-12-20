import random
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.json.get('usuario')
        senha = request.json.get('senha')
        # Lógica de login aqui (substitua pelo seu código real)
        if usuario == 'teste' and senha == '123':
            cookie = "seu_cookie"  # Substitua pelo cookie real
            return jsonify({'cookie': cookie})
        else:
            return jsonify({'erro': 'Credenciais inválidas'}), 401  # 401 significa não autorizado
    return render_template('login.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

# ... (código anterior)

@app.route('/consultar', methods=['POST'])
def consultar_cpf():
    cpf = request.json.get('cpf')
    cookie = request.headers.get('Cookie')

    # Lógica de consulta aqui (substitua pelo seu código real)
    # Neste exemplo, vou gerar um valor aleatório entre 1000 e 5000
    valor_aleatorio = random.randint(1000, 5000)

    # Mensagem de crédito pré-aprovado
    mensagem = f"Você tem um crédito pré-aprovado de: R$ {valor_aleatorio}"

    return jsonify({'cpf': cpf, 'valor_aleatorio': valor_aleatorio, 'mensagem': mensagem})


if __name__ == '__main__':
    app.run(debug=True)

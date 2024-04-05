from flask import Flask, render_template, request
from datetime import datetime
# Cria a instância do Flask no App
app = Flask(__name__)

# Banco em memória
banco = []

# Rota de teste
@app.route('/')
def ola():
    banco.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "hora":datetime.now(),
    "metodo": request.method
    })
    return render_template('index.html')

# Rota de logs
@app.route('/info')
def logs():
    return render_template('logs.html')

# Rota que retorna os acessos
@app.route('/dash', methods=['GET'])
def retorna_acessos():
    return render_template('item-log.html', itens=banco)

@app.route('/ping', methods=['GET'])
def ping():
    banco.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "hora":datetime.now(),
    "metodo": request.method
    })
    return {"resposta": "pong",}

@app.route('/echo', methods=['POST'])
def echo():
    banco.append({
    "endereco":request.environ['REMOTE_ADDR'],
    "hora":datetime.now(),
    "metodo": request.method
    })
    return {"resposta": request.json}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
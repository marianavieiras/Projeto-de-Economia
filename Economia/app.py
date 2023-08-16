from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Defina as rotas para os conceitos e tipos de custos de produção em JSON
@app.route('/conceitos')
def conceitos():
    conceitos_data = {
        'conceito1': '...',
        'conceito2': '...',
        # Adicione mais conceitos aqui
    }
    return jsonify(conceitos_data)

@app.route('/tipos')
def tipos():
    tipos_data = {
        'tipo1': '...',
        'tipo2': '...',
        # Adicione mais tipos aqui
    }
    return jsonify(tipos_data) 

# Adicione outras rotas e endpoints conforme necessário

if __name__ == '__main__':
    app.run(debug=True)

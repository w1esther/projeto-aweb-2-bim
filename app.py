from flask import Flask, render_template, request

app = Flask(__name__)

gabarito = {
    'goldbach' : 'c',
    'reimann' : 'c',
    'gemeos' : 'c',
    'desafios' : 'c'
}

@app.route('/')
def index():
    return render_template('index.html')

# teste

@app.route('/goldbach')
def goldbach():
    return render_template('goldbach.html')

@app.route('/primos')
def primos():
    return render_template('primos.html')

@app.route('/reimann')
def reimann():
    return render_template('reimann.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

@app.route('/twinprimes')
def twinprimes():
    return render_template('twinprimes.html')

# teste

@app.route('/corrigir', methods=['POST'])
def corrigir():
    respostas_usuario = {}

    for perguntas in gabarito:
        respostas_usuario[perguntas] = request.form.get(perguntas)
    
    resultado = {}
    acertos = 0

    for pergunta, resposta in respostas_usuario.items():
        correta = gabarito[pergunta]
        acertou = (resposta == correta)
        resultado[pergunta] = {
            'resposta_usuario': resposta,
            'correta': correta,
            'acertou': acertou
        }

        if acertou:
            acertos += 1
        
    return render_template('resultado.html', resultado=resultado, total=acertos)
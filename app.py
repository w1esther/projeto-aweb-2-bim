from flask import Flask, render_template, request

app = Flask(__name__)

gabarito = {
    'goldbach' : 'c',
    'reimann' : 'c',
    'gemeos' : 'c',
    'desafios' : 'c'
}

@app.route('/')
def teste():
    return render_template('index.html')

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
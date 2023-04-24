from flask import Flask, request, jsonify , render_template

app = Flask(__name__)

@app.route('/',) 
def main():   
  return 'Bem-Vindo';

@app.route('/nota',) 
def note():   
    situacao = None
    media = None

    nota1 = request.args.get('nota1')
    nota2 = request.args.get('nota2')

    if nota1 and nota2:
      nota1 = float(nota1)
      nota2 = float(nota2)

    media = (nota1 + nota2) / 2
    if media >= 7:
      situacao = 'Aprovado'
    elif media >= 4:
      situacao = 'DP'
    else:
      situacao = 'Reprovado'

    return render_template('index.html', media=media,
                                         resultado=situacao)


if __name__ == '__main__':
  app.run(debug=True)

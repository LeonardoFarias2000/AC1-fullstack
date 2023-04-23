from flask import  Flask  , request

app = Flask(__name__)

@app.route('/')
def main():
   nota1 = request.args.get('primeira')
   nota2 = request.args.get('segunda')
   #http://127.0.0.1:5000/?primeira=5&segunda=10
   
   return  ' a média é : ' + (int(nota1)+ int(nota2))/ 2

if __name__== '__main__':
    app.run(debug=True)
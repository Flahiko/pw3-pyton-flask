# Comentario do Python
# Importando o flask na aplicação
from flask import Flask, render_template 
#render_temmplate renderiza as paginas HTML
from controllers import routes

# Carregando o Flask em uma variavel 
# Declarando variavel no Python
app = Flask(__name__, template_folder='views')
#__name__ é uma váriavel do ambiente do Python que tem o nome do modúlo atual

#enviando a variavel app(flask) para as rotas
routes.init_app(app)


# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) # Ligando o modo de Depuração (reinicia automaticamente)
# Rum() - Iniciar um servidor
# Verificando se app.py for o arquivo principal ele inicia o sercidor


#importando o render_template
#Motor para renderizar as páginas 
from flask import render_template

#criando a função para receber o flask
def init_app(app):
    #a partir daqui virão as rotas
   
   
   
        # Criando a rota principal do site
    @app.route('/')
    # Def serve para criar funçoes no Python
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        #Criando variaveis para passar as informaões de um jogo
        titulo = "SilkSong"
        ano= 2025
        categoria = "Metroid Van"
        
        # Criando um objeto python (dicionario) para representar as propriedades de um jogo
        game={
            "Título" : "Minecraft",
            "Ano" : 2012,
            "Categoria" : "Sandbox" 
        }
        
        #criando vetor(lista)
        jogadores= ['Eduardo', 'Ana', 'Guilherme', 'Vitor',' Antônio']
        
        return render_template('games.html',
                            #enviando as variaveis para a página HTML
                            titulo=titulo,
                            ano=ano,
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game)

    @app.route('/consoles')
    def consoles():
        consoles= ['PlayStation1', 'Xbox', 'Nintendo', 'PlayStation2',' Playstation5']
        return render_template('consoles.html',
                            consoles=consoles)
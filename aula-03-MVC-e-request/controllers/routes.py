#importando o render_template
#Motor para renderizar as páginas 
from flask import render_template, request, redirect, url_for

#criando a função para receber o flask
def init_app(app):
    #a partir daqui virão as rotas
    listaGames =  [{"titulo": "CS-GO", "ano": 2012, "categoria": "fps onlline"}]
   
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
        
        #Rota de cadastro de jogos
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        # verificando se o método da requisição é post
        if request.method =='POST':
         # recebendo os dados do formulario e gravando na lista
         listaGames.append({'titulo' : request.form.get ('titulo'), 'categoria' : request.form.get ('categoria'), 'ano' : request.form.get ('ano')})
         # o metodo append() adicion os valores da lista 
         return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               listaGames = listaGames)
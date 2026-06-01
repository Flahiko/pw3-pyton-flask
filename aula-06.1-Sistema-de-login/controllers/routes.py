# Importando o render_template
# Motor para renderizar as páginas
from flask import render_template, request, redirect, url_for, flash
from markupsafe import Markup
# importandoo o model game e o sqlalchemy
from models.database import Game, db, Usuario
# importando WERKZEUG
from werkzeug.security import generate_password_hash

# Criando a função para receber o Flask (app)


def init_app(app):
    # SIMULANDO UM BANCO DE DADOS
    listaGames = [{"titulo": "CS-GO", "ano": 2012, "categoria": "FPS Online"}]

    # A partir daqui virão as rotas

    # CRIANDO A ROTA PRINCIPAL DO SITE
    @app.route('/')
    # def serve para criar funções no Python
    def home():
        return render_template('index.html')

    # CRIANDO A ROTA DE GAMES
    @app.route('/games')
    def games():
        # Criando variáveis para passar as informações de um jogo
        titulo = "Silk Song"
        ano = 2025
        categoria = "Metroid Van"

        # Criando um objeto Python (dicionário) para representar as propriedades de um jogo
        game = {
            "Título": "Minecraft",
            "Ano": 2012,
            "Categoria": "Sandbox"
        }
        # Criando vetor (lista)
        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antônio']
        return render_template('games.html',
                               # Enviando as variáveis para página HTML
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores,
                               game=game)

    # CRIANDO A ROTA DE CONSOLES
    @app.route('/consoles')
    def consoles():
        # Criando vetor (lista)
        consoles = ['Xbox', 'Playstation 5',
                    'Super Nintendo', 'Gameboy', 'Atari']
        return render_template('consoles.html',
                               consoles=consoles)

    # ROTA DE CADASTRO DE JOGOS
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        # Verificando se o método da requisição é POST
        if request.method == 'POST':
            # Recebendo os dados do formulário e gravando na lista
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria')})
            # o método append() adiciona valores a lista
            return redirect(url_for('cadgames'))    
        return render_template('cadgames.html',
                               listaGames = listaGames)
    
    # ROTA PARA EXIBIR O ESTOQUE DE JOGOS
    @app.route('/estoque_jogos', methods=['GET','POST'])
    #criando um parametro na rota (id) para excluir um registro
    @app.route("/estoque_jogos/delete/<int:id>")
    def estoque_jogos(id=None):
        #verificando se está sendo enviado o parâmetro ID para a rota 
        if id:
            game = Game.query.get(id) #SELECT no banco
            #deleta o jogo no banco
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        #verificando se a requisição é do tipo POST
        if request.method == "POST":
            #coletando os dados preenchidos no formulario
            dados_form = request.form.to_dict()
            #enviando os dados para o Model
            newGame = Game(
                dados_form['titulo'],
                dados_form['ano'],
                dados_form['categoria'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade'],
            )
            #Metodo do SQLAlchemy para gravar os dados no banco 
            db.session.add(newGame)
            #confirmando a operação do banco
            db.session.commit()
            #redirecionando o usuario para a página de estoque
            return redirect(url_for('estoque_jogos'))
            
        #selecionando todos os jogos do banco de dados
        games = Game.query.all()
        return render_template('estoque_jogos.html', games=games)
    
     # ROTA PARA EXIBIR O ESTOQUE DE CONSOLES
    @app.route('/estoque_consoles', methods=['GET','POST'])
    #criando um parametro na rota (id) para excluir um registro
    @app.route("/estoque_consoles/delete/<int:id>")
    def estoque_consoles(id=None):
        #verificando se está sendo enviado o parâmetro ID para a rota 
        if id:
            game = Game.query.get(id) #SELECT no banco
            #deleta o jogo no banco
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_consoles'))
        #verificando se a requisição é do tipo POST
        if request.method == "POST":
            #coletando os dados preenchidos no formulario
            dados_form = request.form.to_dict()
            #enviando os dados para o Model
            newGame = Game(
                dados_form['Nome'],
                dados_form['Fabricante'],
                dados_form['Ano'],
                dados_form['Preco'],
                dados_form['Quantidade'],
            )
            #Metodo do SQLAlchemy para gravar os dados no banco 
            db.session.add(newGame)
            #confirmando a operação do banco
            db.session.commit()
            #redirecionando o usuario para a página de estoque
            return redirect(url_for('estoque_consoles'))
            
        #selecionando todos os jogos do banco de dados
        games = Game.query.all()
        return render_template('estoque_consoles.html', games=games)
    
    @app.route('/editar-jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):
        #BUSCANDO O JOGO NO BANCO
        game = Game.query.get(id)
        #VERIFICANDO SE A REQUISIÇÃO É POST
        if request.method == 'POST':
            dados_form = request.form.to_dict()
            #COLETANDO DADOS DO FORMULARIO
            dados_form = request.form.to_dict()
            #PASSANDO DADOS DO FORMULARIO PARA O JOGO
            game.titulo = dados_form['titulo']
            game.ano = dados_form['ano']
            game.categoria = dados_form['categoria']
            game.plataforma = dados_form['plataforma']
            game.preco = dados_form['preco']
            game.quantidade = dados_form['quantidade']
            #CONFIRMANDO ALTERAÇÕES DO BANCO
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        return render_template('editar-jogos.html', game=game)
    
    # ROTA DE CADASTRO DE USUARIO
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        # Verificando se o metodo é post
        if request.method == 'POST':
            # coletando os dados do formulario
            email = request.form['email']
            senha = request.form['senha']
            # VERIFICANDO SE USUARIO JÁ EXISTE
            # BUSCANDO USUSARIO PELO EMAIL
            usuario = Usuario.query.filter_by(email=email).first()
            # VERIFICANDO SE USUARIO POSSUI VALOR
            if usuario:
                msg = Markup("Usuario já cadastrado. Faça o <a href='/login'>Login</a>")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))
            
            # GERANDO O HASH DA SENHA (CRIPTOGRAFIA)
            senha_criptografada = generate_password_hash(senha, method='scrypt')
            #  enviando dados para o model
            novo_usuario = Usuario(email=email, senha=senha_criptografada)
            novo_usuario = Usuario(email=email, senha=senha)
            # cadastrando no banco
            db.session.add(novo_usuario)
            db.session.commit()
            # GERANDO A MENSAGEM DE SUCESSO
            msgCad = Markup("Cadastro realizado com sucesso! Faça o <a href='/login'>Login</a>")
            flash(msgCad, 'success')
            return redirect(url_for('cadastro'))
        return render_template('cadastro.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return render_template('login.html')

import sqlite3

com = sqlite3.connect('contatos.db')
cor = com.cursor()

def criar_agenda():
    cor.execute('''CREATE TABLE IF NOT EXISTS usuario ( id
                INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)''')
    com.commit()


def criar_contatos(nome):
    cor.execute('INSERT INTO usuario (nome) VALUES (?)', (nome,))
    com.commit()


def ver_contatos():
    usuarios = cor.execute('SELECT * FROM usuario').fetchall()
    if not usuarios:
        print('Usuario Não Encontrado')
        return

    for usuario in usuarios:
        print(f'ID: {usuario[0]} | Nome: {usuario[1]}')


def atualizar_contatos(id, nome):
    cor.execute('UPDATE usuario SET nome=? WHERE id=?', (nome, id))
    com.commit()


def deletar_contatos(id):
    cor.execute('DELETE FROM usuario WHERE id=?', (id,))
    com.commit()


def menu():
    print(f'''{"MENU-CONTATOS":~^39}
    [1] - Criar usuario
    [2] - Listar usuarios
    [3] - Atualizar usuario
    [4] - Deletar usuario
    [5] - Sair''')


criar_agenda()
while True:
    menu()
    op = input('Selecione uma opção: ')
    if op == '5':
        print('Encerrando Sistema...')
        break

    if op == '1':
        nome = input('Digite seu nome: ')
        criar_contatos(nome)
        print(f'Bem Vindo {nome}, Sua Conta Foi Criada com Sucesso!')

    elif op == '2':
        ver_contatos()

    elif op == '3':
        i_d = int(input('Digite o id: '))
        novo_nome = input('Digite o novo nome: ')
        atualizar_contatos(i_d, novo_nome)
        print('Contato Atualizado com Sucesso!')

    elif op == '4':
        i_d = int(input('Digite o id: '))
        deletar_contatos(i_d)
        print('Contato Deletado com Sucesso!')

cor.close()
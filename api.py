import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '12345',
    database = 'cadastro',

)
cursor = conexao.cursor()


nome = ""
nome_usuario = ""
email = ""
senha = 0
confirmarSenha = ""


def cadastro():    

        print('CADASTRO DE USUARIOS')
        nome = input("Digite seu Nome completo:")
        nome_usuario = input("Digite seu Nome de usuario:")
        cpf =  int(input("Digite seu CPF:"))
        email = input("Digite seu email:")
        senha = int(input("digite sua nova senha:"))
        confirmarSenha = int(input("Digite a senha novamente:"))
        if  senha == confirmarSenha:
                print("Cadastro efetuado!!")
                print('_'* 45)
                
        else:
                print("\n")
                print("As senhas não coicidem, Tente novamente")
                print("cadastro não efetuado!!")
                
        
        comandoSql = f'INSERT INTO usuario (nome, nome_usuario, cpf, email, senha) VALUES ("{nome}", "{nome_usuario}", {cpf}, "{email}",{senha})'

        cursor.execute(comandoSql) 

        conexao.commit()

def lerTable():
        comandoSql = f'SELECT * FROM usuario'
        cursor.execute(comandoSql)
        resultado = cursor.fetchall()
        print('_'* 45)
        print(resultado)
        print('_'* 45)

def update():
        print('_'* 45)
        print('MUDAR SENHA')
        cpf = int(input("Entre com o seu Cpf:"))
        senha = int(input("Digite sua nova senha:"))
        confirmarSenha = int(input("Digite sua nova senha novamente:"))
        if  senha == confirmarSenha:
                print("Senha alterada!!")
                print('_'* 45)
                
        else:
                print("\n")
                print("As senhas não coicidem, Tente novamente")
                return

        comandoSql = f'UPDATE usuario SET senha = {senha} WHERE cpf = {cpf}'
        cursor.execute(comandoSql)
        conexao.commit()

def deletar():
 
        print("Deletando cadastro")
        print('_'* 45)
        
        comandoSql = f'DELETE FROM usuario WHERE ID = 1'
        
       
        
        cursor.execute(comandoSql)
        conexao.commit()
        


     
print("Seja muito bem vindo a tela de Cadastro da Life\n")
cadastrar = input(" Digite 'S' para se cadastrar, Se já for cadastrado  clique em qualquer tecla para continuar\n >")
print('_'* 45)

if cadastrar == "S":
         cadastro()


print('_'* 45)
print("Deseja?")
print("M = Mudar senha")
print("D = Deletar cadastro")
print("V = Visualizar cadastro ou alterações")
print("E = Encerrar programa ")

        
mudar = input("(M, D, V, E)\n >")
print('_'* 45)
if mudar == "M":
                update()

elif mudar == "D":
                deletar()
elif mudar == "V":
                lerTable()
elif mudar == "E":
                print("encerrando o programa....")
 
                


        



  



cursor.close()
conexao.close()



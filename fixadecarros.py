import sqlite3

# Conecte-se ao banco de dados local
conn = sqlite3.connect('carros.db')
cursor = conn.cursor()

# Crie a tabela de carros, caso ainda não exista
cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        fabricante TEXT NOT NULL,
        modelo TEXT NOT NULL,
        motor TEXT NOT NULL,
        potencia INTEGER NOT NULL,
        torque INTEGER NOT NULL
    )
''')

# Insira alguns dados de exemplo na tabela de carros
cursor.execute('''
    INSERT OR IGNORE INTO carros (nome, ano, fabricante, modelo, motor, potencia, torque)
    VALUES ('Fiat Uno', 1990, 'Fiat', 'Uno', '1.0', 54, 82),
           ('Volkswagen Gol', 2000, 'Volkswagen', 'Gol', '1.6', 101, 145),
           ('Chevrolet Celta', 2010, 'Chevrolet', 'Celta', '1.0', 70, 93)
''')

# Feche a conexão com o banco de dados
conn.commit()
conn.close()

# Peça ao usuário para inserir o nome e o ano do carro
nome = input('Nome do carro: ')
ano = int(input('Ano do carro: '))

# Consulte o banco de dados local para recuperar as informações relevantes sobre o carro
conn = sqlite3.connect('carros.db')
cursor = conn.cursor()
cursor.execute('''
    SELECT fabricante, modelo, motor, potencia, torque
    FROM carros
    WHERE nome =? AND ano =?
''', (nome, ano))
resultado = cursor.fetchone()
conn.close()

# Verifique se o carro foi encontrado
if resultado is None:
    print('Carro não encontrado')
    exit()

# Exiba as informações recuperadas para o usuário em um formato fácil de entender
fabricante, modelo, motor, potencia, torque = resultado
print(f'Fabricante: {fabricante}')
print(f'Modelo: {modelo}')
print(f'Motor: {motor}')
print(f'Potência: {potencia} cv')
print(f'Torque: {torque} Nm')
from datetime import datetime
import random

# pylint: disable=E0401
from tabulate import tabulate

nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade: ")
data_registro = datetime.now()
cartoes = ["R$ 50,00", "R$ 120,00", "R$ 250,00"]
cartao_selecionado = random.choice(cartoes)
data_aniversario = datetime.strptime(input("data de aniversario: "), "%d/%m/%Y")
data_registro_str = data_registro.strftime("%d/%m/%Y")  # Converte para string
data_aniversario_str = data_aniversario.strftime("%d/%m/%Y")  # Converte para string

cadastroFinal = [
    ["Nome do Usuário", nome_usuario],
    ["Idade do Usuário", idade_usuario],
    ["Data de Registro", data_registro_str],
    ["Cartão Selecionado", cartao_selecionado],
    ["Data de Aniversário", data_aniversario_str],
]

# Define as opções de formatação da tabela
headers = ["Descrição", "Resposta"]
table_format = "fancy_grid"

print(tabulate(cadastroFinal, headers, table_format))

print(
    "olá"
    + nome_usuario
    + " seu registro foi concluido com sucesso no dia "
    + data_registro_str
    + " e você foi premiado com um vale compras de "
    + cartao_selecionado
    + ". "
)

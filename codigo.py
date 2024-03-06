# Passo a Passo do projeto 
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time


pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# abrir o navegador (opera gx)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa  um pouco maior (3segundos)
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=435, y=388)
pyautogui.write("jmfelicio.sp@gmail.com")

# escrever a senha 
pyautogui.press("tab")
pyautogui.write("mafefe4598")

# clicar no botao de logar
pyautogui.click(x=681, y=544)
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:
    
    # clicar no primeiro campo 
    pyautogui.click(x=410, y=278)

    # 1 codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # 2 marca do produto 
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # 3 tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # 4 categoria 
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # 5 preço 
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # 6 custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro até acabar a base de dados
import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 4

#Passo 1: Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#time.sleep(10)
#pyautogui.click(x=654, y=744)

#Passo 2: Abrir o sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Passo 2: Fazer login
time.sleep(5)
pyautogui.click(x=705, y=425)
pyautogui.write("fulano@gmail.com")
pyautogui.click(x=690, y=525)
pyautogui.write("Senha123@")
pyautogui.click(x=718, y=580)

#Passo 3: Abri a base de dados dos produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar o 1 produto
for linha in tabela.index: 
    #index para pegar as informações das linhas da tabela / colun para colunas
    pyautogui.click(x=732, y=309) #clica no primeiro campo

    #codigo
    codigo = tabela.loc[linha,"codigo"] #loc = localizar
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter") #enviar

    #numero positivo = scrool para cima
    #numero negativo = scroll para baixo
    pyautogui.scroll(10000)
#Passo 5: Repetir o passo 4 até acabar todos os produtos


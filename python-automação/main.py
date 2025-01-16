import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 3 #todos os comandos do pyautogui serão executados após 3seg

#Passo 1: Abrir o navegador
pyautogui.press("win") #press pressiona um botão do teclado
pyautogui.write("chrome") #write escreve
pyautogui.press("enter") 
time.sleep(3)

#Passo 2: Abrir o sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Passo 2: Fazer login
time.sleep(3)
pyautogui.click(x=705, y=425) #posição do mause na tela
pyautogui.write("fulano@gmail.com")
pyautogui.click(x=690, y=525)
pyautogui.write("Senha123@")
pyautogui.click(x=718, y=580)

#Passo 3: Abri a base de dados dos produtos
tabela = pd.read_csv("produtos.csv") #utilizando pandas para a leitura do arquivo
print(tabela)

#Passo 4: Cadastrar o 1 produto
#Passo 5: Repetir o passo 4 até acabar todos os produtos
    
for linha in tabela.index: #index é utilizado para pegar as informações das linhas da tabela
    print(linha)

    # clicar no primeio campo
    pyautogui.click(x=630, y=312)

    # pegar da tabela o valor do campo que será preenchido
    codigo = tabela.loc[linha, "codigo"] #loc de localizar
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll de tudo pra cima
    pyautogui.scroll(1000)
    
    #scroll com número positivo pra cima
    #scroll com número negativo pra baixo    
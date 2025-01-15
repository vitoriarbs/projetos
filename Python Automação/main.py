import pyautogui
import time

pyautogui.PAUSE = 10

#Passo 1: Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=654, y=744)

#Passo 2: Abrir o sistema da empresa
#   Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#pyautogui.press("enter")

#Passo 2: Fazer login
time.sleep(10)


#Passo 3: Importar a base de dados dos produtos
#Passo 4: Cadastrar o 1 produto
#Passo 5: Repetir o passo 4 até acabar todos os produtos


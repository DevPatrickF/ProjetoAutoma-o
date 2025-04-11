import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas
import pyperclip

#passo 1: entrar no sistema da empresa
#passo 2: fazer login 
#passo 3: importar a base de dados para cadastrar
#passo 4: cadastrar produto e repetir para todos produtos


#passo1
pyautogui.PAUSE = 0.5

navegador = webdriver.Chrome()
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
navegador.maximize_window()
navegador.switch_to.window(navegador.current_window_handle) 
time.sleep(2) 
pyautogui.click(x=200, y=200)     
navegador.find_element(By. ID, "email").click()
time.sleep(1)

#passo2

pyautogui.write("olaemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

#passo3
tabela = pandas.read_csv("produtos_tenis.csv", encoding="utf-8", sep=",")
print(tabela) 

#passo4
for linha in tabela.index:
    navegador.find_element(By.ID, "codigo").click()

    codigo_produto = tabela.loc[linha, "codigo_produto"]
    pyautogui.write(codigo_produto)
    pyautogui.press("tab")

    marca_produto = tabela.loc[linha, "marca_produto"]
    pyautogui.write(marca_produto)
    pyautogui.press("tab")    

    tipo_produto = tabela.loc[linha, "tipo_produto"]
    pyautogui.write(tipo_produto)
    pyautogui.press("tab")

    categoria_produto = tabela.loc[linha, "categoria_produto"]   
    pyautogui.write(categoria_produto)
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo_produto = tabela.loc[linha, "custo_produto"]
    pyautogui.write(str(custo_produto))
    pyautogui.press("tab")

    observacoes = str(tabela.loc[linha, "observacoes"])
    if observacoes != "nan":
        pyperclip.copy(observacoes)
        pyautogui.hotkey("ctrl", "v")

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

print("Cadastro de produtos finalizado com sucesso!")
time.sleep(6)
navegador.quit()    

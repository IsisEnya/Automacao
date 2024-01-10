from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

def pesquisar(codigo):
    try:
        codigo = str(codigo)
        options = webdriver.ChromeOptions()

        options.add_experimental_option("detach",True)
        options.add_argument("--headless=new")


        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=options)

        driver.get("https://vtc.log.br")

        rastreamento = driver.find_element(By.ID, "btn-tracking")
        rastreamento.click()

        abas = driver.window_handles

        driver.switch_to.window(abas[-1])
        email = driver.find_element(By.NAME, "ds_email")
        rastreio = driver.find_element(By.NAME, "cd_Referencia")

        email.send_keys("teste123@gmail.com")
        rastreio.send_keys(codigo)
        botao = driver.find_element(By.ID,"btnPesquisar")
        botao.click()

        # Verificar se o codigo foi encontrado
        contador = 0
        #======================TODE ESSE TRAMPO PRA ACHAR UM BOTÃO ================================================= 
        while True:
            lista_botoes = driver.find_elements(By.TAG_NAME,"button")
            constante = False
            contador += 1
            if contador == 6:
                driver.quit()
                return (False, {})
            for pos, b in enumerate(lista_botoes):
                if "Detalhes" in b.text:
                    detalhes = lista_botoes[pos]
                    constante = True
                    break
            if constante == True:
                break       
            sleep(1)


        detalhes.click()
        sleep(1)

        fieldset = driver.find_element(By.TAG_NAME,"fieldset")

        div = fieldset.find_element(By.TAG_NAME,"div")
        lista_div = div.find_elements(By.TAG_NAME, "div")

        dados = {}

        for div in lista_div:
            label = div.find_element(By.TAG_NAME,"label")
            input = div.find_element(By.TAG_NAME,"input")
            dados[label.text] =  input.get_attribute("value")


        table = fieldset.find_element(By.TAG_NAME,"table")
        lista_td = table.find_elements(By.TAG_NAME,"td")
        for pos, td in enumerate(lista_td):
            if pos == 0:
                dados["codigo"] = td.text
            if pos == 1:
                dados["medicamento"] = td.text
            if pos == 2:
                dados["quantidade"] = td.text
        driver.quit()
        return (True, dados)
    except:
        return (False, {"codigo":"erro"})


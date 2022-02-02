import pyautogui
import time
import dotenv
import os

dotenv.load_dotenv()

def conectarFunc():
    connect = True
    login = os.getenv("EMAIL")
    senha = os.getenv("SENHA")
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    while procurarImagemSemRetornarErro("login") == False:
        time.sleep(1)
    while connect == True:
        if (procurarImagemSemRetornarErro("login")):
            x, y = procurarLocalizacaoDaImagemPelosEixos("email")
            pyautogui.click(x, y+30, duration=3)
            pyautogui.write(login)
            x, y = procurarLocalizacaoDaImagemPelosEixos("password")
            pyautogui.click(x, y+30, duration=3)
            pyautogui.write(senha)
            pyautogui.click(x, y, duration=3)
            pyautogui.click(searchForHighConfidenceImage("letsGo"), duration=3)
            time.sleep(3)
            pyautogui.click(searchForHighConfidenceImage("farmTelaDeLogin"), duration=3)
            connect = False
        else:
            raise Exception('Erro ao realizar login')

def searchForHighConfidenceImage(imagem):
    print("Procurando imagem em searchForHighConfidenceImage: "+ imagem)
    contadorProcurarImagem = 0
    img = None
    confidence = 0.9
    loading = True
    while img == None:
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 200:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def procurarImagemSemRetornarErro(imagem):
    loop = True
    contador = 0
    time.sleep(3)
    confidence = 0.95
    print("Procurando imagem em procurarImagemSemRetornarErro: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    print(img)
    if img != None:
        return True
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    if procurarImagemSemRetornarErro(imagem):
        confidence = 0.9
        x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        return x, y
    else:
        return None, None

def openTheMenuOfTheTowers():
    if procurarImagemSemRetornarErro("towers"):
        pyautogui.click(searchForHighConfidenceImage("towers"), duration=1.5)
    if procurarImagemSemRetornarErro("lineUp"):
        pyautogui.click(searchForHighConfidenceImage("lineUp"), duration=1.5)

    time.sleep(5)
    x, y = pyautogui.locateCenterOnScreen('./assets/setaRight.png', confidence=0.8)
    for i in range(4):
        makeTowerWorker(i, x, y)
    closeTheMenuAfterConfirmChanges()

def closeTheMenuAfterConfirmChanges():
    if procurarImagemSemRetornarErro("confirm"):
        pyautogui.click(searchForHighConfidenceImage("confirm"), duration=1.5)
    if procurarImagemSemRetornarErro("wait") and procurarImagemSemRetornarErro("farm"):
        pyautogui.click(searchForHighConfidenceImage("farm"), duration=1.5)
    
def makeTowerWorker(i, x, y):
    # CODIGO PARA CLICAR NO BOTÃO IN GAME, SE BASEANDO NA ENERGIA DO PERSONAGEM
    # while procurarImagemSemRetornarErro("inGame"):
    #     x, y = procurarLocalizacaoDaImagemPelosEixos("inGame")     
    #     pyautogui.click(x+75, y, duration=1.5)
    clickOnTheButtonInGame(x, y)
    if i < 3:
        if procurarImagemSemRetornarErro("setaRight"):
            pyautogui.click(searchForHighConfidenceImage("setaRight"), duration=1.5)

def clickOnTheButtonInGame(x, y):
    time.sleep(1)
    pyautogui.click(x+200, y+90)
    time.sleep(2)
    pyautogui.click(x+200, y+220)
    time.sleep(2)
    pyautogui.click(x+200, y+350)
    time.sleep(2)
    pyautogui.click(x+200, y+480)

#CONNECT
time.sleep(2)
openTheMenuOfTheTowers()
while True:
    try:
        conectarFunc()
        reiniciar = False
        while reiniciar == False:
            openTheMenuOfTheTowers()
            time.sleep(7200)
            if procurarImagemSemRetornarErro("meioDaTela") == False:
                reiniciar = True

    except BaseException as err:
        print("Ocorreu um ERRO:")
        print(err)
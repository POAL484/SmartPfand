import pygame as pg
import serial
import threading as th
import sys
#import json
import ast
from time import sleep
import cv2 as cv
import numpy as np
from keras.models import load_model
import math
import codecs as cdcs #импорт библиотек

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, hWWW = 1.1, **kwargs):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.hWWW = hWWW
        try: self.textSize = kwargs['textSize']
        except KeyError: self.textSize = 25
        pg.alreadyPressed = False

        self.fillColors = {
            'normal': '#dadada',
            'hover': '#aaaaaa',
            'pressed': '#bbbbbb',
        }

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)

        font = pg.font.SysFont('Arial', self.textSize)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.st = True

        obj.append(self)

    def process(self):
        if self.st:
            mousePos = pg.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])
                if pg.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])
                    if self.onePress:
                        self.onclickFunction()
                    elif not pg.alreadyPressed:
                        self.onclickFunction()
                        pg.alreadyPressed = True
                else:
                    pg.alreadyPressed = False

            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/self.hWWW - self.buttonSurf.get_rect().height/self.hWWW
            ])
            root.blit(self.buttonSurface, self.buttonRect)

    def hide(self): self.st = False
    def show(self):self.st = True

class Keyboard123():
    def __init__(self):
        self.obj = []
        self.Y1 = Button(110, pg.hs/2+100-150, 95, 95, "Й", hWWW = 2, onclickFunction=lambda lt = "й": self.add(lt))
        self.obj.append(self.Y1)
        self.CE = Button(220, pg.hs/2+100-150, 95, 95, "Ц", hWWW = 2, onclickFunction=lambda lt = "ц": self.add(lt))
        self.obj.append(self.CE)
        self.U = Button(330, pg.hs/2+100-150, 95, 95, "У", hWWW = 2, onclickFunction=lambda lt = "у": self.add(lt))
        self.obj.append(self.U)
        self.KA = Button(440, pg.hs/2+100-150, 95, 95, "К", hWWW = 2, onclickFunction=lambda lt = "к": self.add(lt))
        self.obj.append(self.KA)
        self.E = Button(550, pg.hs/2+100-150, 95, 95, "Е", hWWW = 2, onclickFunction=lambda lt = "е": self.add(lt))
        self.obj.append(self.E)
        self.N = Button(660, pg.hs/2+100-150, 95, 95, "Н", hWWW = 2, onclickFunction=lambda lt = "н": self.add(lt))
        self.obj.append(self.N)
        self.G = Button(770, pg.hs/2+100-150, 95, 95, "Г", hWWW = 2, onclickFunction=lambda lt = "г": self.add(lt))
        self.obj.append(self.G)
        self.SH = Button(880, pg.hs/2+100-150, 95, 95, "Ш", hWWW = 2, onclickFunction=lambda lt = "ш": self.add(lt))
        self.obj.append(self.SH)
        self.SH1 = Button(990, pg.hs/2+100-150, 95, 95, "Щ", hWWW = 2, onclickFunction=lambda lt = "щ": self.add(lt))
        self.obj.append(self.SH1)
        self.Z = Button(1100, pg.hs/2+100-150, 95, 95, "З", hWWW = 2, onclickFunction=lambda lt = "з": self.add(lt))
        self.obj.append(self.Z)
        self.HE = Button(1210, pg.hs/2+100-150, 95, 95, "Х", hWWW = 2, onclickFunction=lambda lt = "х": self.add(lt))
        self.obj.append(self.HE)
        self.TVERDIY = Button(1320, pg.hs/2+100-150, 95, 95, "Ъ", hWWW = 2, onclickFunction=lambda lt = "ъ": self.add(lt))
        self.obj.append(self.TVERDIY)
        self.F = Button(160, pg.hs/2+210-150, 95, 95, "Ф", hWWW = 2, onclickFunction=lambda lt = "ф": self.add(lt))
        self.obj.append(self.F)
        self.bl = Button(270, pg.hs/2+210-150, 95, 95, "Ы", hWWW = 2, onclickFunction=lambda lt = "ы": self.add(lt))
        self.obj.append(self.bl)
        self.V = Button(380, pg.hs/2+210-150, 95, 95, "В", hWWW = 2, onclickFunction=lambda lt = "в": self.add(lt))
        self.obj.append(self.V)
        self.A = Button(490, pg.hs/2+210-150, 95, 95, "А", hWWW = 2, onclickFunction=lambda lt = "а": self.add(lt))
        self.obj.append(self.A)
        self.P = Button(600, pg.hs/2+210-150, 95, 95, "П", hWWW = 2, onclickFunction=lambda lt = "п": self.add(lt))
        self.obj.append(self.P)
        self.R = Button(710, pg.hs/2+210-150, 95, 95, "Р", hWWW = 2, onclickFunction=lambda lt = "р": self.add(lt))
        self.obj.append(self.R)
        self.O = Button(820, pg.hs/2+210-150, 95, 95, "О", hWWW = 2, onclickFunction=lambda lt = "о": self.add(lt))
        self.obj.append(self.O)
        self.L = Button(930, pg.hs/2+210-150, 95, 95, "Л", hWWW = 2, onclickFunction=lambda lt = "л": self.add(lt))
        self.obj.append(self.L)
        self.D = Button(1040, pg.hs/2+210-150, 95, 95, "Д", hWWW = 2, onclickFunction=lambda lt = "д": self.add(lt))
        self.obj.append(self.D)
        self.GE = Button(1150, pg.hs/2+210-150, 95, 95, "Ж", hWWW = 2, onclickFunction=lambda lt = "ж": self.add(lt))
        self.obj.append(self.GE)
        self.AA = Button(1260, pg.hs/2+210-150, 95, 95, "Э", hWWW = 2, onclickFunction=lambda lt = "э": self.add(lt))
        self.obj.append(self.AA)
        self.YA = Button(270, pg.hs/2+320-150, 95, 95, "Я", hWWW = 2, onclickFunction=lambda lt = "я": self.add(lt))
        self.obj.append(self.YA)
        self.CH = Button(380, pg.hs/2+320-150, 95, 95, "Ч", hWWW = 2, onclickFunction=lambda lt = "ч": self.add(lt))
        self.obj.append(self.CH)
        self.S = Button(490, pg.hs/2+320-150, 95, 95, "С", hWWW = 2, onclickFunction=lambda lt = "с": self.add(lt))
        self.obj.append(self.S)
        self.M = Button(600, pg.hs/2+320-150, 95, 95, "М", hWWW = 2, onclickFunction=lambda lt = "м": self.add(lt))
        self.obj.append(self.M)
        self.I = Button(710, pg.hs/2+320-150, 95, 95, "И", hWWW = 2, onclickFunction=lambda lt = "и": self.add(lt))
        self.obj.append(self.I)
        self.T = Button(820, pg.hs/2+320-150, 95, 95, "Т", hWWW = 2, onclickFunction=lambda lt = "т": self.add(lt))
        self.obj.append(self.T)
        self.MYAGK = Button(930, pg.hs/2+320-150, 95, 95, "Ь", hWWW = 2, onclickFunction=lambda lt = "ь": self.add(lt))
        self.obj.append(self.MYAGK)
        self.B = Button(1040, pg.hs/2+320-150, 95, 95, "Б", hWWW = 2, onclickFunction=lambda lt = "б": self.add(lt))
        self.obj.append(self.B)
        self.YU = Button(1150, pg.hs/2+320-150, 95, 95, "Ю", hWWW = 2, onclickFunction=lambda lt = "ю": self.add(lt))
        self.obj.append(self.YU)
        self.space = Button(500, pg.hs/2+300, 500, 95, '', lambda lt = ' ': self.add(lt))
        self.obj.append(self.space)
        self.backspace = Button(1200, pg.hs/2-200, 300, 95, 'Стереть', hWWW = 2, onclickFunction=self.back)
        self.obj.append(self.backspace)
        self.text = ''
    def show(self):
        for i in self.obj:
            i.show()
    def hide(self):
        for i in self.obj:
            i.hide()
    def add(self, lt):
        self.text += lt
    def showText(self):
        addText(pg.font.SysFont('Arial', 40, True), self.text, (0, 0, 0), pg.ws/2, pg.hs/2-300)
    def back(self):
        try: self.text = self.text[0:len(self.text)-1]
        except IndexError: pass
            

def hideAll():
    for i in obj:
        i.hide()

def addText(sfont, text, color, x, y):
    rend = sfont.render(text, True, color)
    root.blit(rend, (x-(sfont.size(text)[0]/2), y-(sfont.size(text)[1]/2)))


def openCam():
    pg.cam = cv.VideoCapture(1)

def loadModel():
    pg.model = load_model("Neural/v0.1/keras_Model.h5", compile=False)
    pg.class_names = open("Neural/v0.1/labels.txt", "r").readlines()


def doBank():
    try:
        pg.bank = pg.Banks[pg.qr2]
        SETaddpoint()
    except KeyError:
        pg.bank = {'name': 'Not Found', 'cost': '0'}
        SETbankerror()
    pg.qr2 = ''



def welcomeScr():
    wlInfo.show()
    wlCardCheck.show()
    wlShop.show()
    wlBank.show()
    #addText(pg.font.SysFont('Arial', 40), "Вставьте банку в ячейку...", (0, 0, 0), pg.ws/2, (pg.hs-100)/2)
    #addText(pg.font.SysFont('Arial', 18), "Для получения дополнительных инструкций нажмите кнопку ниже", (0, 0, 0), pg.ws/2, (pg.hs)/2)

def infoScr():
    infBack.show()
    addText(pg.font.SysFont('Arial', 30), "Фандомат: сдавайте банки - получайте балллы.", (0, 0, 0), pg.ws/2, 100)
    addText(pg.font.SysFont('Arial', 30), "Инструкции:", (0, 0, 0), pg.ws/2, 150)
    addText(pg.font.SysFont('Arial', 30), "1. Вставте банку в ячейку", (0, 0, 0), pg.ws/2, 200)
    addText(pg.font.SysFont('Arial', 30), "2. Если банка есть в базе данных, вы получите баллы, иначе вам надо обратиться в тех поддержку", (0, 0, 0), pg.ws/2, 250)
    addText(pg.font.SysFont('Arial', 30), "3. Для того чтобы получить баллы, прислоните карту к ридеру", (0, 0, 0), pg.ws/2, 300)
    addText(pg.font.SysFont('Arial', 30), "4. Если ваша карта зарегистрирована, вы получите баллы", (0, 0, 0), pg.ws/2, 350)
    addText(pg.font.SysFont('Arial', 30), "5. Иначе, зарегистрируйтесь: либо обращаетесь в тех поддержку, либо регистрируйтесь самостоятельно", (0, 0, 0), pg.ws/2, 400)
    addText(pg.font.SysFont('Arial', 30), "6. Для самостоятельной регистрации: выберете вариант самостоятельной регистрации, затем введите свое ФИО.", (0, 0, 0), pg.ws/2, 450)
    addText(pg.font.SysFont('Arial', 30), "ВАЖНО: Вводите полное и настоящие ФИО", (0, 0, 0), pg.ws/2, 500)
    addText(pg.font.SysFont('Arial', 30), "7. Баллы нужны для покупки сувениров в магазине. 1 Банка = 1 Балл", (0, 0, 0), pg.ws/2, 550)
    addText(pg.font.SysFont('Arial', 30), "8. Полный список магазина вы можете посмотреть нажав Enter и выбрав вариант магазин", (0, 0, 0), pg.ws/2, 600)
    addText(pg.font.SysFont('Arial', 30), "9. Для того чтобы посмотреть баланс: нажмите Enter и выберете выриант информация о карте", (0, 0, 0), pg.ws/2, 650)
    addText(pg.font.SysFont('Arial', 30), "10. Вашу карту могут заблокировать: для разблокировки обратитесь в тех поддержку", (0, 0, 0), pg.ws/2, 700)

def cardcheckScr():
    crdchBack.show()
    addText(pg.font.SysFont('Arial', 40), "Приложите карту к считывателю", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.cardCode == 0: SETcardinfoerror()
    elif pg.cardCode == 1: SETcardinfo()

def cardinfoerrorScr():
    crdinferrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Пользователь не найден", (0, 0, 0), pg.ws/2, pg.hs/2)

def cardinfoScr():
    crdinfBack.show()
    addText(pg.font.SysFont('Arial', 40), f"Имя: {pg.usInfo['name']}", (0, 0, 0), pg.ws/2, pg.hs/3)
    addText(pg.font.SysFont('Arial', 40), f"Баланс: {pg.usInfo['bal']}", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.usInfo['isMod'] == '1': crdinfMod.show()

def addpointScr():
    addText(pg.font.SysFont('Arial', 40), "Приложите карту к считывателю", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.cardCode == 0: SETregisterStep1()
    elif pg.cardCode==1: SETcardinfoadd()

def cardinfoaddScr():
    crdinfBack.show()
    addText(pg.font.SysFont('Arial', 40), f"Имя: {pg.usInfo['name']}", (0, 0, 0), pg.ws/2, pg.hs/3)
    addText(pg.font.SysFont('Arial', 40), f"Баланс: {int(pg.usInfo['bal'])+int(1)}", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 30), f"1 балл добавлен!", (0, 0, 0), pg.ws/2, pg.hs/3-100)

def bankerrorScr():
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Банка не найдена!", (0, 0, 0), pg.ws/2, pg.hs/2)

def bankerrorneuralScr():
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Нейросеть не обнаружила банку. Пожалуйста извлеките ее из аппрата", (0, 0, 0), pg.ws/2, pg.hs/2)

def regStep1Scr():
    kb.showText()

def regStep2Scr():
    addText(pg.font.SysFont('Arial', 40), "Пользователь зарегистрирован!", (0, 0, 0), pg.ws/2, pg.hs/2-200)
    addText(pg.font.SysFont('Arial', 40), f"Теперь твой баланс 1 балл!", (0, 0, 0), pg.ws/2, pg.hs/2)

def shopScr():
    crdchBack.show()

def bankScr():
    bnkNeural.show()
    addText(pg.font.SysFont('Arial', 40), "Приложите банку к штрих коду", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 23), "Моя банка или штрих код", (0, 0, 0), pg.ws/2, pg.hs/2+250)
    addText(pg.font.SysFont('Arial', 23), "повреждены.", (0, 0, 0), pg.ws/2, pg.hs/2+280)
    addText(pg.font.SysFont('Arial', 23), "Использовать нейросеть", (0, 0, 0), pg.ws/2, pg.hs/2+310)

def neuralScr():
    addText(pg.font.SysFont('Arial', 40), "Использую нейросеть для распознования банки...", (0, 0, 0), pg.ws/2, pg.hs/2)
    pg.sin1 += 0.05
    pg.sin2 += 0.05
    pg.draw.line(root, (0, 0, 0), (pg.ws/2-100, 700), (pg.ws/2-100, 700-abs(math.sin(pg.sin1)*100)), width=5)
    pg.draw.line(root, (0, 0, 0), (pg.ws/2, 700), (pg.ws/2, 700-abs(math.sin(pg.sin2)*100)), width=5)
    pg.draw.line(root, (0, 0, 0), (pg.ws/2+100, 700), (pg.ws/2+100, 700-abs(math.sin(pg.sin1)*100)), width=5)

def customerrorScr():
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Произошла непридвиденная ошибка. Обратитесь в тех поддержку", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 15), f"Код ошибки: {pg.code}",  (0, 0, 0), pg.ws/2, pg.hs/2+200)




def cardRead():
    while True:
        r = str(ser.readall())
        #r = "b'AAAAAA11\\r\\n'" #####
        #while not pg.ent: pass
        #r = "b''" #####
        if r != "b''":
            g = r.split('\'')[1].split('\\r\\n')
            try: g.remove('')
            except Exception:
                print("Ошибка при считывании")
                continue
            if len(g) == 1:
                pg.usInfo = {'uuid': "Err", 'name': "Err, not found", 'bal': "Err, not found", 'isMod': '0', 'isBaned': '0'}
                pg.uuid = g[0]
                try:
                    pg.usInfo['uuid'] = pg.uuid
                    pg.usInfo['name'] = pg.Users[pg.uuid]['name']
                    pg.usInfo['bal'] = pg.Users[pg.uuid]['bal']
                    pg.usInfo['isMod'] = pg.Users[pg.uuid]['mod']
                    pg.usInfo['isBaned'] = pg.Users[pg.uuid]['ban']
                    pg.cardCode = 1
                except KeyError: pg.cardCode = 0
                return

def neuralRead():
    _, frame = pg.cam.read()
    if _:
        img_orig = frame 
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = cv.resize(img_orig, (224, 224), interpolation=cv.INTER_AREA) 
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3) 
        image = (image / 127.5) - 1
        prediction = pg.model.predict(image) 
        index = np.argmax(prediction) 
        class_name = pg.class_names[index] 
        confidence_score = prediction[0][index]
        if index == 0: SETaddpoint()
        if index == 1: SETbankerrorneural()
        return
    else:
        SETcustomerror("CAM_RETURNED_NOT_SUCCESS_CODE")
        



def SETwelcome():
    hideAll()
    pg.state = 'welcome'

def SETinfo():
    hideAll()
    pg.state = 'info'

def SETcardcheck():
    hideAll()
    pg.state = 'cardcheck'
    pg.cardCode = -1
    pg.th = th.Thread(target = cardRead)
    pg.th.start()

def SETshop():
    hideAll()
    pg.state = 'shop'

def SETcardinfoerror():
    hideAll()
    pg.state = 'cardinfoerror'

def SETcardinfo():
    hideAll()
    pg.state = 'cardinfo'

def SETmod():
    hideAll()
    pg.state = 'mod'

def SETaddpoint():
    hideAll()
    pg.state = 'addpoint'
    pg.cardCode = -1
    pg.th = th.Thread(target = cardRead)
    pg.th.start()

def SETbankerror():
    hideAll()
    pg.state = 'bankerror'

def SETcardinfoadd():
    hideAll()
    bal = int(pg.Users[pg.usInfo['uuid']]['bal'])
    bal += int(1)
    pg.Users[pg.usInfo['uuid']]['bal'] = str(bal)
    writeTHIS()
    pg.state = 'cardinfoadd'

def SETregisterStep1():
    hideAll()
    pg.regUsInfo = {}
    pg.regUsInfo['uuid'] = pg.uuid
    pg.regUsInfo['bal'] = '1'
    pg.regUsInfo['isBaned'] = '0'
    pg.regUsInfo['isMod'] = '0'
    kb.show()
    regEnter.show()
    pg.state = 'regStep1'

def SETregisterStep2():
    hideAll()
    pg.regUsInfo['name'] = kb.text
    kb.text = ''
    pg.Users[pg.uuid] = {}
    pg.Users[pg.uuid]['uuid'] = pg.uuid
    pg.Users[pg.uuid]['name'] = pg.regUsInfo['name']
    pg.Users[pg.uuid]['bal'] = pg.regUsInfo['bal']
    pg.Users[pg.uuid]['ban'] = pg.regUsInfo['isBaned']
    pg.Users[pg.uuid]['mod'] = pg.regUsInfo['isMod']
    writeTHIS()
    crdinfBack.show()
    pg.state = 'regStep2'

def SETbank():
    hideAll()
    pg.state = 'bank'

def SETneural():
    hideAll()
    pg.sin1 = 0
    pg.sin2 = 30
    pg.state = 'neural'
    th.Thread(target=neuralRead).start()

def SETbankerrorneural():
    hideAll()
    pg.state = 'bankerrorneural'

def SETcustomerror(code): 
    pg.code = code
    hideAll()
    pg.state = 'customerror'




def readTHIS():
    pg.Users = ast.literal_eval(usf.read())
    pg.Banks = ast.literal_eval(bnkf.read())

def writeTHIS():
    wrus = cdcs.open("Base2/Users.txt", 'w', 'utf-8')
    wrbnk=cdcs.open("Base2/Banks.txt", 'w', 'utf-8')
    wrus.write(str(pg.Users))
    wrbnk.write(str(pg.Banks))
    wrus.close()
    wrbnk.close()



pg.processing = True

#ser = serial.Serial("COM5", 9600, timeout = 0)

MYVERSION    = "v.0.2.0"
MYVERSIONGR="v.0.1-b"
BASEMODELVERSION = "v.0.1"

pg.usInfo = {'uuid': "Err", 'name': "Err, not found", 'bal': "Err, not found", 'isMod': '0', 'isBaned': '0'}

usf = cdcs.open("Base2/Users.txt", 'r', 'utf-8')
bnkf = cdcs.open("Base2/Banks.txt", 'r', 'utf-8')
readTHIS()

print('\n\n')
print(f"Version: {MYVERSION}\n")
print(f"Version of GR: {MYVERSIONGR}\n")
print(f"Users Base Version: {pg.Users['Version']}\n")
print(f"Banks Base Version: {pg.Banks['Version']}\n")
print(f"Model Version: {BASEMODELVERSION}\n")

print(f"Opening the camera...")
openCam()
print(f"Camera opened\n")

print(f"Load model...")
loadModel()
print(f"Model loaded\n")

print("Sleepin...", end=' ')
sleep(0.5)
print("Run GR\n")

pg.init()

root = pg.display.set_mode((0, 0), pg.FULLSCREEN)

pg.display.update()

font = pg.font.SysFont('Arial', 25)

fps = 60
fpsClock = pg.time.Clock()

pg.ws = pg.display.get_surface().get_size()[0]
pg.hs = pg.display.get_surface().get_size()[1]

obj = []

kb = Keyboard123()

wlInfo = Button(250, 630, 300, 200, 'Инструкции', SETinfo)
wlCardCheck = Button(600, 630, 300, 200, 'Информация по карте', SETcardcheck)
wlShop = Button(950, 630, 300, 200, 'Магазин', SETshop)
wlBank = Button(450, 300, 600, 250, "Банка", SETbank, textSize = 80)

infBack = Button(50, 630, 300, 200, 'Назад', SETwelcome)

crdchBack = Button(50, 630, 300, 200, 'Назад', SETwelcome)

crdinferrBack = Button(50, 630, 300, 200, 'Назад', SETwelcome)

crdinfBack = Button(50, 630, 300, 200, 'Далее', SETwelcome)
crdinfMod = Button(1000, 630, 300, 200, 'Мод Чек', SETmod)

bnkerrBack = Button(50, 630, 300, 200, 'Назад', SETwelcome)

regEnter = Button(1260, pg.hs/2+320-150, 190, 190, 'Ввод', SETregisterStep2, hWWW=2)

bnkNeural = Button(pg.ws/2-150, pg.hs/2+150, 300, 200, '', SETneural)

hideAll()

pg.state = "welcome"

pg.qr2 = ''

pg.cardData = ''

pg.ent = False

while pg.processing:
    pg.ent = False
    for event in pg.event.get():
        if event.type == pg.QUIT: pass
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                pg.qr2 += '1'
            if event.key == pg.K_2:
                pg.qr2 += '2'
            if event.key == pg.K_3:
                pg.qr2 += '3'
            if event.key == pg.K_4:
                pg.qr2 += '4'
            if event.key == pg.K_5:
                pg.qr2 += '5'
            if event.key == pg.K_6:
                pg.qr2 += '6'
            if event.key == pg.K_7:
                pg.qr2 += '7'
            if event.key == pg.K_8:
                pg.qr2 += '8'
            if event.key == pg.K_9:
                pg.qr2 += '9'
            if event.key == pg.K_0:
                pg.qr2 += '0'
            if event.key == pg.K_RETURN:
                doBank()
            if event.key == pg.K_p:
                pg.ent = True

    root.fill((255, 255, 255))
        
    for i in obj:
        i.process()

    if pg.state == "welcome": welcomeScr()
    if pg.state == "info": infoScr()
    if pg.state == "cardcheck": cardcheckScr()
    if pg.state == "cardinfoerror": cardinfoerrorScr()
    if pg.state == "cardinfo": cardinfoScr()
    if pg.state == "addpoint": addpointScr()
    if pg.state == "cardinfoadd": cardinfoaddScr()
    if pg.state == "bankerror": bankerrorScr()
    if pg.state == "regStep1": regStep1Scr()
    if pg.state == "regStep2": regStep2Scr()
    if pg.state == "shop": shopScr()
    if pg.state == "bank": bankScr()
    if pg.state == "neural": neuralScr()
    if pg.state == "bankerrorneural": bankerrorneuralScr()
    if pg.state == "customerror": customerrorScr()

    pg.display.flip()
    fpsClock.tick(fps)


pg.quit()
quit()



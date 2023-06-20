import pygame as pg #Основная графическая библиотека
import serial #Библиотека для работы с монитором порта
import threading as th #Библиотека для много-поточности
import sys #Библиотека для системных шрифтов
#import json
import ast #Библиотека для работы с json файлами
from time import sleep #Библиотека для задержек
import cv2 as cv #Библиотека для работы с фотографиями
import numpy as np #Библиотека для работы с массивами
from keras.models import load_model #Функция для загрузки модели из файла
import math #Библиотека для математический функций
import codecs as cdcs #Библиотека для правильной работы utf-8 файлов

class Button(): #Класс кнопки
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, hWWW = 1.1, **kwargs): #Инициализация
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.hWWW = hWWW
        try: self.textSize = kwargs['textSize']
        except KeyError: self.textSize = 35
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

    def process(self): #Функция рендера кнопки, используется каждый кадр
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

    def hide(self): self.st = False #Выключает рендер кнопки
    def show(self):self.st = True #Включает рендер кнопки

class Keyboard123(): #Класс для клавиатуры из кнопок
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
    def show(self): #Включает рендер всех "клавиш" клавиатуры
        for i in self.obj:
            i.show() 
    def hide(self): #Выключает рендер всех "клавиш" клавиатуры
        for i in self.obj:
            i.hide()
    def add(self, lt): #Функция которая срабатывает при нажатии на клавишу
        self.text += lt
    def showText(self): #Рендер текста
        addText(pg.font.SysFont('Arial', 40, True), self.text, (0, 0, 0), pg.ws/2, pg.hs/2-300)
    def back(self): #Функция стирания текста
        try: self.text = self.text[0:len(self.text)-1]
        except IndexError: pass
            

def hideAll(): #Вспомогательная функция скрытия всех кнопок
    for i in obj:
        i.hide()

def addText(sfont, text, color, x, y): #Вспомогательная функция рендера любого текста
    rend = sfont.render(text, True, color)
    root.blit(rend, (x-(sfont.size(text)[0]/2), y-(sfont.size(text)[1]/2)))


def openCam(): #Функция открытия камеры
    pg.cam = cv.VideoCapture(1)

def loadModel(): #Функция загрузки модели нейросети из файла
    pg.model = load_model("Neural/v0.2/model.h5", compile=False)
    #pg.class_names = open("Neural/v0.1/labels.txt", "r").readlines()


def doBank(): #Функция которая срабатывает при нажатии на Enter. Клавишу Enter нажимает сканер штрих кодов
    try:
        pg.bank = pg.Banks[pg.qr2]
        SETaddpoint() #Когда нашел банку установить экран добавления очка
    except KeyError:
        pg.bank = {'name': 'Not Found', 'cost': '0'}
        SETbankerror() #Когда не нашел банку установить экран не найденой банки
    pg.qr2 = ''



def welcomeScr(): #Функция начального экрана
    wlInfo.show()
    wlCardCheck.show()
    wlShop.show()
    wlBank.show()
    #addText(pg.font.SysFont('Arial', 40), "Вставьте банку в ячейку...", (0, 0, 0), pg.ws/2, (pg.hs-100)/2)
    #addText(pg.font.SysFont('Arial', 18), "Для получения дополнительных инструкций нажмите кнопку ниже", (0, 0, 0), pg.ws/2, (pg.hs)/2)

def infoScr(): #Функция экрана с инструкциями
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

def cardcheckScr(): #Функция экрана для призыва приложить карту
    crdchBack.show()
    addText(pg.font.SysFont('Arial', 40), "Приложите карту к считывателю", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.cardCode == 0: SETcardinfoerror()
    elif pg.cardCode == 1: SETcardinfo()

def cardinfoerrorScr(): #Функция экрана с ошибкой не найденного пользователя
    crdinferrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Пользователь не найден", (0, 0, 0), pg.ws/2, pg.hs/2)

def cardinfoScr(): #Функция экрана с информацией по карте
    crdinfBack.show()
    addText(pg.font.SysFont('Arial', 40), f"Имя: {pg.usInfo['name']}", (0, 0, 0), pg.ws/2, pg.hs/3)
    addText(pg.font.SysFont('Arial', 40), f"Баланс: {pg.usInfo['bal']}", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.usInfo['isMod'] == '1': crdinfMod.show()

def addpointScr(): #Функция экрана для призыва приложить карту, но при отсканированой банкой, а не по кнопке "Информация по карте", как в функции выше
    addText(pg.font.SysFont('Arial', 40), "Приложите карту к считывателю", (0, 0, 0), pg.ws/2, pg.hs/2)
    if pg.cardCode == 0: SETregisterStep1()
    elif pg.cardCode==1: SETcardinfoadd()

def cardinfoaddScr(): #Функция экрана с информацией по карту, но после внесенной банки
    crdinfBack.show()
    addText(pg.font.SysFont('Arial', 40), f"Имя: {pg.usInfo['name']}", (0, 0, 0), pg.ws/2, pg.hs/3)
    addText(pg.font.SysFont('Arial', 40), f"Баланс: {int(pg.usInfo['bal'])+int(1)}", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 30), f"1 балл добавлен!", (0, 0, 0), pg.ws/2, pg.hs/3-100)

def bankerrorScr(): #функция экрана с не найденной банкой
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Банка не найдена!", (0, 0, 0), pg.ws/2, pg.hs/2)

def bankerrorneuralScr(): #Функция экрана с не найденной нейросетью банкой
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Нейросеть не обнаружила банку. Пожалуйста извлеките ее из аппрата", (0, 0, 0), pg.ws/2, pg.hs/2)

def regStep1Scr(): #Функция экрана с первым этапом регистрации пользователя
    kb.showText()

def regStep2Scr(): #Функция экрана со вторым этапом регистрации (и информации о карте)
    addText(pg.font.SysFont('Arial', 40), "Пользователь зарегистрирован!", (0, 0, 0), pg.ws/2, pg.hs/2-200)
    addText(pg.font.SysFont('Arial', 40), f"Теперь твой баланс 1 балл!", (0, 0, 0), pg.ws/2, pg.hs/2)

def shopScr(): #Функция экрана магазина, не готово
    crdchBack.show()

def bankScr(): #Функция экрана "Банка"
    bnkNeural.show()
    addText(pg.font.SysFont('Arial', 40), "Приложите банку к штрих коду", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 23), "Моя банка или штрих код", (0, 0, 0), pg.ws/2, pg.hs/2+250) #Сооздание надписи для кнопки
    addText(pg.font.SysFont('Arial', 23), "повреждены.", (0, 0, 0), pg.ws/2, pg.hs/2+280)
    addText(pg.font.SysFont('Arial', 23), "Использовать нейросеть", (0, 0, 0), pg.ws/2, pg.hs/2+310)

def neuralScr(): #Функция экрана с распознованией при помощи нейросети
    addText(pg.font.SysFont('Arial', 40), "Использую нейросеть для распознования банки...", (0, 0, 0), pg.ws/2, pg.hs/2)
    pg.sin1 += 0.05
    pg.sin2 += 0.05 #Косметические линии, рисуются функцией синуса
    pg.draw.line(root, (0, 0, 0), (pg.ws/2-100, 700), (pg.ws/2-100, 700-abs(math.sin(pg.sin1)*100)), width=5)
    pg.draw.line(root, (0, 0, 0), (pg.ws/2, 700), (pg.ws/2, 700-abs(math.sin(pg.sin2)*100)), width=5)
    pg.draw.line(root, (0, 0, 0), (pg.ws/2+100, 700), (pg.ws/2+100, 700-abs(math.sin(pg.sin1)*100)), width=5)

def customerrorScr(): #Функция экрана для универсального вывода ошибок
    bnkerrBack.show()
    addText(pg.font.SysFont('Arial', 40), "Произошла непридвиденная ошибка. Обратитесь в тех поддержку", (0, 0, 0), pg.ws/2, pg.hs/2)
    addText(pg.font.SysFont('Arial', 15), f"Код ошибки: {pg.code}",  (0, 0, 0), pg.ws/2, pg.hs/2+200)




def cardRead(): #Функция в отдельном потоке для считывания uuid номера с монитора порта
    ser.readall()
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

def neuralRead(): #Сканирование при помощи нейросети, тоже в отдельном потоке
    _, image = pg.cam.read() #Снятие снимка с камеры
    if _:
        #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #image = cv.cvtColor(cv.resize(img_orig, (224, 224), interpolation=cv.INTER_AREA) , cv.COLOR_BGR2GRAY)
        #image = np.asarray(frame, dtype=np.float32).reshape(1, 224, 224)
        print(image.shape)
        #image = cv.resize(image, (224, 224)) #Изменение размера картинки на нужные
        image = cv.imread("Neural/datasets/not bank/not_bank46.png")
        print(image.shape)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #Преобразование в черно-белую картинку
        print(image.shape)
        cv.imwrite("Neural/frame.png", image) 
        image = image.astype("float32")/255.0 #Преобразование для нейросети: значение цвета будет от 0 до 1
        print(image.shape)
        image = np.expand_dims(image, -1) #Еще одно преобразование для нейросети
        print(image.shape)
        image = np.asarray([image.tolist()])
        print(image.shape)
        #image = (image / 127.5) - 1
        prediction = pg.model.predict(image)  #Предсказание
        index = np.argmax(prediction)
        print(f"conf: {prediction[0][index]}")
        #class_name = pg.class_names[index] 
        #confidence_score = prediction[0][index]
        if index == 1: SETaddpoint()
        if index == 0: SETbankerrorneural()
        return
    else:
        SETcustomerror("CAM_RETURNED_NOT_SUCCESS_CODE")
        



def SETwelcome(): #Функция включения начального экрана
    hideAll()
    pg.state = 'welcome'

def SETinfo():  #Функция включения экрана с информацией
    hideAll()
    pg.state = 'info'

def SETcardcheck(): #Функция включения экрана с призывом приложить карту
    hideAll()
    pg.state = 'cardcheck'
    pg.cardCode = -1
    pg.th = th.Thread(target = cardRead) #Запуск потока
    pg.th.start()

def SETshop(): #Функция включения экрана с магазином
    hideAll()
    pg.state = 'shop'

def SETcardinfoerror(): #Функция включения экрана с ошибкой не найденного пользователя
    hideAll()
    pg.state = 'cardinfoerror'

def SETcardinfo(): #Функция включения экрана с информацией по карте
    hideAll()
    pg.state = 'cardinfo'

def SETmod(): #Функция включения экрана модерации, пока что не используется
    hideAll()
    pg.state = 'mod'

def SETaddpoint(): #Функция включения экрана с призывом приложить карту, с найденной банкой
    hideAll()
    pg.state = 'addpoint'
    pg.cardCode = -1
    pg.th = th.Thread(target = cardRead) #Запуск потока
    pg.th.start()

def SETbankerror(): #Функция включения экрана с не найденной банкой
    hideAll()
    pg.state = 'bankerror' 

def SETcardinfoadd(): #Функция включения экрана с информацией по карте + добавление балла
    hideAll()
    bal = int(pg.Users[pg.usInfo['uuid']]['bal'])
    bal += int(1) #Добавление очка к балансу
    pg.Users[pg.usInfo['uuid']]['bal'] = str(bal) #Обновление баланса
    writeTHIS() #Сохранение в файл
    pg.state = 'cardinfoadd'

def SETregisterStep1(): #Функция включения экрана с первым этапом регистрации
    hideAll()
    pg.regUsInfo = {} #Создание начальных данных нового пользователя
    pg.regUsInfo['uuid'] = pg.uuid
    pg.regUsInfo['bal'] = '1'
    pg.regUsInfo['isBaned'] = '0'
    pg.regUsInfo['isMod'] = '0'
    kb.show()
    regEnter.show()
    pg.state = 'regStep1'

def SETregisterStep2(): #Функция включения экрана с информацией по карте нового пользователя
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

def SETbank(): #Функция включения экрана "Банка"
    hideAll()
    pg.state = 'bank'

def SETneural(): #Функция включения экрана распознования с нейросети
    hideAll()
    pg.sin1 = 0 #Начальные параметры синусоидных линий
    pg.sin2 = 30
    pg.state = 'neural'
    th.Thread(target=neuralRead).start() #Начало потока

def SETbankerrorneural(): #Функция включения экрана не найденной с помощью нейросети банки
    hideAll()
    pg.state = 'bankerrorneural'

def SETcustomerror(code): #Функция включения экрана для универсального вывода ошибки
    pg.code = code
    hideAll()
    pg.state = 'customerror'




def readTHIS(): #Функция для чтения данных из json файлов
    pg.Users = ast.literal_eval(usf.read())
    pg.Banks = ast.literal_eval(bnkf.read())

def writeTHIS(): #Функция для записи данных в json файлы
    wrus = cdcs.open("Base2/Users.txt", 'w', 'utf-8')
    wrbnk=cdcs.open("Base2/Banks.txt", 'w', 'utf-8')
    wrus.write(str(pg.Users))
    wrbnk.write(str(pg.Banks))
    wrus.close()
    wrbnk.close()



pg.processing = True

#ser = serial.Serial("COM5", 9600, timeout = 0) #Привязка к последовательному порту

MYVERSION    = "v.0.2.2" #Константы версий
MYVERSIONGR="v.0.2-a"
BASEMODELVERSION = "v.0.2"

pg.usInfo = {'uuid': "Err", 'name': "Err, not found", 'bal': "Err, not found", 'isMod': '0', 'isBaned': '0'}

usf = cdcs.open("Base2/Users.txt", 'r', 'utf-8')
bnkf = cdcs.open("Base2/Banks.txt", 'r', 'utf-8')
readTHIS() #Чтение данных
 
print('\n\n')
print(f"Version: {MYVERSION}\n")
print(f"Version of GR: {MYVERSIONGR}\n")
print(f"Users Base Version: {pg.Users['Version']}\n")
print(f"Banks Base Version: {pg.Banks['Version']}\n")
print(f"Model Version: {BASEMODELVERSION}\n") #Удобный вывод всех версий

print(f"Opening the camera...")
openCam()
print(f"Camera opened\n") #Открытие камеры

print(f"Load model...")
loadModel()
print(f"Model loaded\n") #Загрузка модели

print("Sleepin...", end=' ')
sleep(0.5) #Время для того чтобы успеть взглянуть на все версии
print("Run GR\n")

pg.init()

root = pg.display.set_mode((0, 0), pg.FULLSCREEN) #Создание окна. Параметр pg.FULLSCREEN пользволяет вывести окно ровно на весь экран, и без рамки

pg.display.update()

font = pg.font.SysFont('Arial', 25)

fps = 60
fpsClock = pg.time.Clock() #Пайгеймовские часы

pg.ws = pg.display.get_surface().get_size()[0]
pg.hs = pg.display.get_surface().get_size()[1] #Переменные размера окна, позволяют удобно привязывать текст и кнопки

obj = []

kb = Keyboard123()

wlInfo = Button(250, 630, 300, 200, 'Инструкции', SETinfo)
wlCardCheck = Button(600, 630, 300, 200, 'Информация по карте', SETcardcheck, textSize=27)
wlShop = Button(950, 630, 300, 200, 'Магазин', SETshop)
wlBank = Button(450, 300, 600, 250, "Банка", SETbank, textSize = 100) #Кнопки начального экрана

infBack = Button(50, 630, 300, 200, 'Назад', SETwelcome) #Кнопка "Назад" экрана с инструкцией

crdchBack = Button(50, 630, 300, 200, 'Назад', SETwelcome) #Кнопка "Назад" экрана с призывом приложить карту, но без сканированной до этого банки

crdinferrBack = Button(50, 630, 300, 200, 'Назад', SETwelcome) #Кнопка "Назад" экрана с не найденным пользователем

crdinfBack = Button(50, 630, 300, 200, 'Далее', SETwelcome) #Кнопка "Назад" экрана с информацией по карте
crdinfMod = Button(1000, 630, 300, 200, 'Мод Чек', SETmod) #Кнопка входа в режим модератора, на том же экране

bnkerrBack = Button(50, 630, 300, 200, 'Назад', SETwelcome) #Кнопка "Назад" для экрана с не найденной банкой
#Кнопки "Назад" могут быть и не на своих экранах, так как создавать кнопку "Назад" каждый раз заново оказалось не практично

regEnter = Button(1260, pg.hs/2+320-150, 190, 190, 'Ввод', SETregisterStep2, hWWW=2) #Кнопка "Ввод" для экрана с регистрацией

bnkNeural = Button(pg.ws/2-150, pg.hs/2+150, 300, 200, '', SETneural) #Кнопка экрана "Банка" для начала сканирования при помощи нейросети, текст на кнопку при создании не передаётся, создается в функции экрана, так как нужен был многострочный текст

hideAll() #Сразу прячем кнопки

pg.state = "welcome" #Устанавливаем экран привествия

pg.qr2 = '' #Переменная в которой хранится введенная сканером штрих кодов информация

pg.cardData = ''

#pg.ent = False

while pg.processing:
    #pg.ent = False
    for event in pg.event.get():
        if event.type == pg.QUIT: pass #Окно не закроется при Alt+F4 и других попытках закрыть окно не через IDLE и диспетчер задач
        if event.type == pg.KEYDOWN:
            """Сканер штрихкода работает по принципу:
                Отсканировал штрих код/qr код
                Ввел информацию с штрих/qr кода, как как-будто информацию ввели с клавиатуры
                В конце нажимает Enter как как-будто с клавиатуры
                Ниже мы отслеживаем нажатия клавиатуры"""
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
            #if event.key == pg.K_p:
                #pg.ent = True

    root.fill((255, 255, 255))
        
    for i in obj:
        i.process() #Рендер каждой кнопки, проверка на включение внутри функции process()

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
    if pg.state == "customerror": customerrorScr() #Включение функций экранов

    pg.display.flip()
    fpsClock.tick(fps) #Обновление экрана и тик часов


pg.quit()
quit()




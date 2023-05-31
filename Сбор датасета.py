import cv2
import tkinter as tk  # библиотека для создания графического интерфейса
from PIL import Image, ImageTk  # библиотека для работы с изображениями

def show_frame(st): 
    global stop, cap, cnt_img

    # Чтение кадра с камеры и преобразование его в RGB формат
    if cap.isOpened(): 
        ret, frame = cap.read() 
        if ret: 
            # Изменить размер кадра видео
            frame = cv2.resize(frame, (224, 224))
           # Конвертация изображения в формат,
           # подходящий для отображения в tkinter окне,
           # и отображение на виджете
            img = Image.fromarray(frame) 
            imgtk = ImageTk.PhotoImage(image = img) 
            video_label.imgtk = imgtk 
            video_label.configure(image = imgtk) 
            # Записать кадр видео в файл
            cnt_img +=1
            
            if st == 1 :
                path = "C://Users/1653107/Documents/RRO/dataset_Banka/b"+ str(cnt_img) +".png"
            else:
                path = "C://Users/1653107/Documents/RRO/dataset_NotBanka/nb"+ str(cnt_img) +".png"
            cv2.imwrite( path , frame)
            Status_label.config(text ="Кол-во снимков:"+str(cnt_img)) 
            # Условие выхода - клавиша q
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                stop  = True 
    if  stop == False and cnt_img < 140:   
        # Если флаг остановки не установлен, то функция будет вызываться снова через 20 миллисекунд
        video_label.after(200, lambda : show_frame(st)) 
    else: 
        # Остановка работы программы и освобождение ресурсов
        cap.release() 
        cv2.destroyAllWindows()

# Функция устанавливает флаг `stop` в значение `True`, что приводит к остановке работы программы. 
def finish():
    global stop
    stop  = True
# Функция отвечает за открытие камеры и запуск функции `show_frame()`.
def open_file(st):
    global cap, is_paused
    cap= cv2.VideoCapture(0)
    show_frame(st)

# Начало программы 
root = tk.Tk()  # создание окна
root.title("Сбор датасет для фандомата ")  # название окна
root["bg"] = "black"  # фон окна
cap = None  # переменная для работы с камерой
stop = False  # переменная для остановки работы программы
cnt_img = 0   # кол-во сохраненных кадров
# Создание кнопок и надписей в графическом окне
banka_button = tk.Button(root , text="Banka", width = 10, height =4, 
                        bg = "black", fg = "red", font = ('Arial', 15, 'bold'), 
                        command=lambda : open_file(1) )
not_banka_button = tk.Button(root , text="Not Banka", width = 10, height =4, 
                        bg = "black", fg = "red", font = ('Arial', 15, 'bold'), 
                        command=lambda : open_file(2)  )

finish_button = tk.Button(root , text="Finish",  width = 10, height =4, 
                          bg = "black", fg = "red", font = ('Arial', 15, 'bold'), 
                        command=finish ) 

Status_label= tk.Label(root , text="Cнимков: 0", 
                       bg = "black", fg = "red", font = ('Arial', 15, 'bold')) 
 
video_label = tk.Label(root  , text="Press 'BANKA' to start.", 
                       bg = "black", fg = "red", font=("Arial", 16)) 

# Размещение кнопок и надписей на окне
banka_button.grid(row = 0,column = 0)
not_banka_button.grid(row = 0,column = 1) 
finish_button.grid(row = 0, column = 2)  
Status_label.grid(row = 0, column = 3)  
video_label.grid(row = 2, columnspan = 4) 

root.mainloop()  # запуск программы через главный цикл окна

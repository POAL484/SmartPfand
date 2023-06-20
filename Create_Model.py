import numpy as np #Библиотека для работы с массивами
import tensorflow as tf #Библиотека для нейросетей
from tensorflow.keras.utils import to_categorical #Вспосогательная функция

import cv2 as cv #Библиотека для работы с изображениями
from sklearn.model_selection import train_test_split #Функция для разбивки тренировочный и тестовых данных

X = [] #Пустые списки
y = []
for i in range(1120): #Перебирает 1120 фотографий банок
  X.append(cv.cvtColor(cv.imread(f"datasets/bank/bank{i+1}.png"), cv.COLOR_BGR2GRAY).tolist()) #Читает фотографию с диска, преобразовывает в черно-белую и преобразовывает из numpy массива в обычный список
for i in range(980): #Перебирает 980 фотографий не банок
  X.append(cv.cvtColor(cv.imread(f"datasets/not bank/not_bank{i+1}.png"), cv.COLOR_BGR2GRAY).tolist()) #Как и выше читает и преобразовывает
for i in range(1120): #Добавляет ответы
  y.append(1)
for i in range(980):
  y.append(0)
X = np.asarray(X) #И преобразовывает обратно в numpy массив
y = np.asarray(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #Разбивает выборку в прапорциях 80:20

y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2) #Преобразование ответов
X_train = X_train.astype("float32")/255.0
X_test = X_test.astype("float32")/255.0 #Преобразование фотографий - все цвета становятся в диапозоне от 0 до 1
X_train = np.expand_dims(X_train, -1)
X_test = np.expand_dims(X_test, -1) #Еще одно преобразование

from tensorflow.keras.models import Sequential

model = Sequential() #Создание модели

from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten

model.add(Conv2D(128, activation = 'relu', kernel_size=(3, 3), input_shape = (224, 224, 1)))
model.add(MaxPooling2D())
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(2, activation="sigmoid")) #Добавляем слои

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics = ['accuracy']) #Компиляция модели

history = model.fit(X_train, y_train, batch_size = 256, epochs = 4) #Обучение модели

model.save("v0.2/model.h5") #Сохранение модели

print("\n\nMODEL READY!\n\n")

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"test loss: {test_loss}")
print(f"test accuracy: {int(round(test_accuracy, 2)*100)}%") #Тест на тренировачных данных


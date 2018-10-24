import keras
from keras.models import load_model

model = keras.applications.mobilenet.MobileNet()
model.save("mobilenet.h5")

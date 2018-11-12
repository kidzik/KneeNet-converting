import tensorflowjs as tfjs
from keras.models import load_model

k_model = load_model("chexnet.h5")
print(k_model.summary())
tfjs.converters.save_keras_model(k_model, "chexnet-tfjs")

from keras.models import load_model
model = load_model('KneeNet-keras.h5')
print(model.summary())

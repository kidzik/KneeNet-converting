# KneeNet

## Converting models

1. Download models (pytorch Kneenet and keras chexnet) with `bash downlnoad_models`
2. Convert chexnet from keras to tfjs with `python chex2tfjs.py`
2. Convert kneenet from pytorch to tfjs with `python pt2ker.py`

## Dependencies

There might be more than that but it definitely needs at least:

* pytorch
* keras
* tfjs https://js.tensorflow.org/
* pytorch2keras https://github.com/nerox8664/pytorch2keras

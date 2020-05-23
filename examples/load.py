import numpy as np
from tensorflow.keras.models import load_model
from utils.BASEDIR import BASEDIR

model = load_model('{}/examples/batch_norm.h5'.format(BASEDIR))
print(model.predict([[[4.5, 4.5]]]).tolist())


# exit()

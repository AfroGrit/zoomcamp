#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('autosave', '0')


# In[2]:


get_ipython().system('wget https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5 -O clothing-model.h5')


# In[7]:



get_ipython().system('wget http://bit.ly/mlbookcamp-pants -O pants.jpg')


# In[3]:


get_ipython().system('python -V')


# In[8]:


import numpy as np

import tensorflow as tf
from tensorflow import keras

tf.__version__

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.xception import preprocess_input


# In[5]:


get_ipython().system('ls')


# In[6]:


model = keras.models.load_model('clothing-model.h5')


# In[9]:


img = load_img('pants.jpg', target_size=(299, 299))

x = np.array(img)
X = np.array([x])

X = preprocess_input(X)
preds = model.predict(X)
preds


# In[10]:


classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

dict(zip(classes, preds[0]))


# In[11]:


converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
with open('clothing-model.tflite', 'wb') as f_out:
    f_out.write(tflite_model)


# In[12]:


get_ipython().system('ls -lh')


# In[14]:


import tensorflow.lite as tflite


# In[15]:


interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']
interpreter.set_tensor(input_index, X)
interpreter.invoke()
preds = interpreter.get_tensor(output_index)
classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

dict(zip(classes, preds[0]))


# In[1]:


get_ipython().system('ls -lh')


# In[2]:


get_ipython().system('jupyter nbconvert --to script tf_lite.ipynb')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
import os
import helpers
import numpy as np

MODEL_NAME = os.getenv('MODEL_NAME', 'dino_dragon.tflite')

interpreter = tflite.Interpreter(model_path=MODEL_NAME)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
    'carcharodontosaurus',
    'smaug',
]

# url = 'https://bit.ly/3VzTUGC'
# predict('https://bit.ly/3VzTUGC') for local test
def predict(url):
    img = helpers.download_image(url)
    img = helpers.prepare_image(img, target_size=(150, 150))

    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = helpers.prepare_input(X)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()

    predictions = interpreter.get_tensor(output_index)
    float_predictions = predictions[0].tolist()
    
    return dict(zip(classes, float_predictions))
    # return float(preds[0, 0])


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }
    print(result)
    return result     
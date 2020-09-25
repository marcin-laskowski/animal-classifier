
import io
import sys
import os
import json
import base64
import numpy as np
import tensorflow as tf

from PIL import Image

checkpoint = 'mobilenet_v2_1.0_224'
model_path = 'models/tensorflow/research/slim/nets/mobilenet/mobilenet_v2.py'

class PythonPredictor:

    def __init__(self, config):
        self._model = None
        
        if not os.path.exists(model_path):
            os.system('git clone https://github.com/tensorflow/models ./models/tensorflow')
        
        sys.path.append(os.path.abspath('./models/tensorflow/research/slim'))        
       

    def predict(self, payload):
        
        from nets.mobilenet import mobilenet_v2

        input_image = io.BytesIO(base64.b64decode(payload["image"]))
        img = np.array(Image.open(input_image).resize((224, 224))).astype(np.float) / 128 - 1

        gd = tf.GraphDef.FromString(open( "models/mobilenet/"+ checkpoint +'_frozen.pb', 'rb').read())
        inp, predictions = tf.import_graph_def(gd,  return_elements = ['input:0', 'MobilenetV2/Predictions/Reshape_1:0'])

        with tf.Session(graph=inp.graph):
            y = predictions.eval(feed_dict={inp: img.reshape(1, 224,224, 3)})

        with open('models/imagenet-simple-labels.json') as f:
            labels = json.load(f)

        return [labels[y.argmax()]]

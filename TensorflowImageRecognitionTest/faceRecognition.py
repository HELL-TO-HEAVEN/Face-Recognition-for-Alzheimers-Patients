
import os
import glob
import numpy as np
import cv2
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from keras import backend as K
from keras.models import load_model
def triplet_loss(y_true, y_pred, alpha = 0.3):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]

    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,
        positive)), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor,
        negative)), axis=-1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
    return loss

K.set_image_data_format('channels_first')
FRmodel = load_model('model.h5')

# distance formula

# prepare database with images of faces
def prepare_database():
    database = {}
# function img_path_to_encoding converts each image into 128 float numbers
    for file in glob.glob("./images/*"):
        identity = os.path.splitext(os.path.basename(file))[0]
        database[identity] = img_path_to_encoding(file, FRmodel)
        return database

# recognize face
def who_is_it(image, database, model):
    encoding = img_to_encoding(image, model)

    min_dist = 100
    identity = None

    # Loop over the database dictionary's names and encodings.
    for (name, db_enc) in database.items():
        dist = np.linalg.norm(db_enc - encoding)
        print('distance for %s is %s' %(name, dist))
        if dist < min_dist:
            min_dist = dist
            identity = name

    if min_dist > 0.52:
        return None
    else:
        return identity
print("Hello")
database = prepare_database()
img = "HOWARD.jpg"
identity = who_is_it(img, database, model)
print(identity)

import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing import image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from keras.applications.vgg16 import VGG16
from sklearn.metrics.pairwise import cosine_similarity

import os
print(os.path.abspath('./temp-pics/wrench1.jpg'))

vgg16 = VGG16(weights='imagenet', include_top=False,
              pooling='max', input_shape=(224, 224, 3))

# print the summary of the model's architecture.
vgg16.summary()

for model_layer in vgg16.layers:
    model_layer.trainable = False


def load_image(image_path):

    input_image = Image.open(image_path)
    resized_image = input_image.resize((224, 224))

    return resized_image


def get_image_embeddings(object_image: image):

    image_array = np.expand_dims(image.img_to_array(object_image), axis=0)
    image_embedding = vgg16.predict(image_array)

    return image_embedding


def get_similarity_score(first_image: str, second_image: str):

    first_image = load_image(first_image)
    second_image = load_image(second_image)

    first_image_vector = get_image_embeddings(first_image)
    second_image_vector = get_image_embeddings(second_image)

    similarity_score = cosine_similarity(
        first_image_vector, second_image_vector).reshape(1,)

    return similarity_score


def show_image(image_path):
    image = mpimg.imread(image_path)
    imgplot = plt.imshow(image)
    plt.show()


def recog(request):
    return HttpResponse("Hello world!")


class MLPrediction(APIView):

    def get(self, request):  # Change to post request later

        # define the path of the images
        wrench1 = './temp-pics/wrench1.jpg'
        # wrench2 = '/content/wrench2.jpg'
        wrenchbroken = './temp-pics/wrenchbroken.jpg'

        # hammer = '/content/hammer.jpg'

        # use the show_image function to plot the images
        # show_image(wrench1), show_image(wrenchbroken)

        similarity_score = get_similarity_score(wrench1, wrenchbroken)
        return HttpResponse(json.dumps({
            'score': similarity_score
        }))

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from put_stress_rus.utils.word_processing import WordsProcessing
from tensorflow.keras.models import load_model
from pathlib import Path


path_model_stress = Path(__file__).parent / "model_put_stress.h5" 
model_stress = load_model(path_model_stress)
print("Trained Model uploaded successfully")


def errors(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Input word includes invalid character, remove it and try again"
    return inner


@errors
def put_stress(word_lowcase):
    word_as_number = WordsProcessing.word2numbers(word_lowcase)
    stress_as_array = model_stress.predict(word_as_number) 
    word_stressed = WordsProcessing.numbers2word_stressed(stress_as_array, word_lowcase)
    return  word_stressed
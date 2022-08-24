import pytest
from put_stress_rus.utils.word_processing import WordsProcessing
import numpy as np


def test_get_unique_chs_from_unstressed_words():
    output = ['-', 'а', 'б', 'в', 'г', 'д', 'е', 'ж',
              'з', 'и', 'й', 'к', 'л', 'м', 'н', 
              'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 
              'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 
              'э', 'ю', 'я', 'ё']
    assert output == WordsProcessing.get_unique_chs_from_unstressed_words()
    


def test_get_number2character_for_unstressed_words():
    output = {1: '-', 2: 'а', 3: 'б', 4: 'в', 5: 'г', 6: 'д', 7: 'е', 
            8: 'ж', 9: 'з', 10: 'и', 11: 'й', 12: 'к', 13: 'л', 
            14: 'м', 15: 'н', 16: 'о', 17: 'п', 18: 'р', 19: 'с', 
            20: 'т', 21: 'у', 22: 'ф', 23: 'х', 24: 'ц', 25: 'ч', 
            26: 'ш', 27: 'щ', 28: 'ъ', 29: 'ы', 30: 'ь', 31: 'э', 
            32: 'ю', 33: 'я', 34: 'ё'}
    assert output == WordsProcessing.get_number2character_for_unstressed_words()     


def test_get_character2number_for_unstressed_words():
    output = {'-': 1, 'а': 2, 'б': 3, 'в': 4, 'г': 5, 'д': 6, 'е': 7, 
            'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13, 
            'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 
            'т': 20, 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25, 
            'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 
            'ю': 32, 'я': 33, 'ё': 34}
    assert output == WordsProcessing.get_character2number_for_unstressed_words()



def test_word2numbers():
    int_list = [ 6, 16, 14,  0,  0,  0,  0,  0,  0,  
            0,  0,  0,  0,  0,  0,  0, 0,  0,  
            0,  0,  0,  0,  0,  0,  0]
    output = np.array([int_list])
    assert output.all() == WordsProcessing.word2numbers("дом").all()
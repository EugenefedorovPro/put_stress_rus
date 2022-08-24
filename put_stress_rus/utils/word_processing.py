from wiktionary_rus.wiktionary import wiki_instances
import numpy as np
from memoization import cached


class WordsProcessing():

  
    @classmethod
    @cached
    def get_unique_chs_from_unstressed_words(cls):
      unique_chs_from_unstressed_words = set()
      for item in wiki_instances:
        if item.status:
          chs = list(item.word_lowcase)
          unique_chs_from_unstressed_words.update(chs)
      unique_chs_from_unstressed_words = list(unique_chs_from_unstressed_words)
      unique_chs_from_unstressed_words.sort()
      return unique_chs_from_unstressed_words


    @classmethod
    @cached
    def get_character2number_for_unstressed_words(cls):
      unique_chs = cls.get_unique_chs_from_unstressed_words() 
      character2number_for_unstressed_words = dict((ch,i) for i, ch in enumerate(unique_chs, start = 1))
      return character2number_for_unstressed_words

  
    @classmethod
    @cached
    def get_number2character_for_unstressed_words(cls): 
      unique_chs = cls.get_unique_chs_from_unstressed_words() 
      number2character_for_unstressed_words = dict((i,ch) for i, ch in enumerate(unique_chs, start = 1))
      return number2character_for_unstressed_words 

  
    @classmethod
    def word2numbers(cls, word_lowcase):
      character2number_for_unstressed_words = cls.get_character2number_for_unstressed_words()
      max_length_of_unstressed_word = 36
      numbers = []
      for ch in word_lowcase:
        n = character2number_for_unstressed_words[ch]
        numbers.append(n)
      n_of_zeros_to_add = max_length_of_unstressed_word - len(numbers) 
      numbers.extend([0 for i in range(n_of_zeros_to_add)])
      numbers = np.array(numbers)
      numbers = numbers.reshape((1,max_length_of_unstressed_word))
      return numbers

    
    @classmethod
    def numbers2word_stressed(cls, stress_as_array, word_lowcase):
      index_of_stress = np.argmax(stress_as_array)
      word_stressed = word_lowcase[:index_of_stress] + "'" + word_lowcase[index_of_stress:]
      return word_stressed

    
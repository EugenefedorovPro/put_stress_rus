from tensorflow.keras.models import load_model
from pathlib import Path


path_model_stress = Path.cwd() / "Model_put_stress" 

model_stress = load_model(path_model_stress)


def put_stress(word_lowcase):

  def _word2numbers(word_lowcase):
    _numbers = []
    for ch in word_lowcase:
      n = character2number_for_unstressed_words[ch]
      _numbers.append(n)
    _n_of_zeros_to_add = max_length_of_unstressed_word - len(_numbers) 
    _numbers.extend([0 for i in range(_n_of_zeros_to_add)])
    _numbers = np.array(_numbers)
    _numbers = _numbers.reshape((1,max_length_of_unstressed_word))
    return _numbers

  stress_as_array = model_stress.predict(_word2numbers(word_lowcase))
  
  def numbers2word_stressed(stress_as_array):
    index_of_stress = np.argmax(stress_as_array)
    word_stressed = word_lowcase[:index_of_stress] + "'" + word_lowcase[index_of_stress:]
    return word_stressed
  
  word_stressed = numbers2word_stressed(stress_as_array)
  return  word_stressed
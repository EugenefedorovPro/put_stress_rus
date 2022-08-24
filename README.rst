##############################
put_stress_rus
##############################

Python package to put stress on a russian word powered by the trained neural network with categorical_accuracy 0.7945

* Version 0.0.1
* Date: 2022, August, 24
* Developer: Eugene Proskulikov
* License: MIT
* Contact: `LinkedIn <https://www.linkedin.com/in/eugene-proskulikov-168050a4/>`_.
* Home: https://github.com/EugenefedorovPro/put_stress_rus



-------------
Dependencies
-------------

* tensorflow==2.9.1
* numpy==1.23.1 


--------
Install
--------

:: 

    pip install git+https://github.com/EugenefedorovPro/put_stress_rus.git
    

------------
Quick start
------------

::
    
    from put_stress_rus.put_stress import put_stress
    
    put_stress("усмеяльно")

Output::

> "усмея'льно"


:: 

    put_stress("жук-олень")

Output::

> "жук-оле'нь"


input - russian word in low_case, only alphabetic characters [а-я] and "-" as the only extra sign 

output - the same word with the stress mark after the accented vowel

-----------------------
Neuron Network training
-----------------------
`nn_training <https://github.com/EugenefedorovPro/put_stress_rus/tree/main/nn_training>`_ directory contains files demanded for training neural network, which is used in `put_stress_rus`:
 
* *put_stress_on_word.ipynb* - preprocessing data, model compile, save, validate, predict. The file demands Jupyter editor (JupyterLab, VS Code with Jupyter extension, PyCharm Professional, etc.)
* *requirements.txt* - list of dependecies, including the two critical ones:
    * `ipapy <https://github.com/pettarin/ipapy>`_ is `my modifications <https://github.com/EugenefedorovPro/ipapy_eugene/tree/forpython310>`_ of the library for working with the Russin language within the framework of International Phonetic Alphabet (IPA)
    * `*wiktionary_rus* <https://github.com/EugenefedorovPro/wiktionary_rus>`_ is my Python package with Russian wiktionary preprocessed for neural networks

------------
NN accuracy
------------
Categorical accuracy of the `put_stress_rus` is 0.7945. The model was trained on the basis of `specially parsed Russian wiktionary <https://github.com/EugenefedorovPro/wiktionary_rus>`_, encompassing 422821 word-stems and word-forms. The Russian language does not have strict rules of accentuation, thus, deploying NN you can enjoy only some probability of correct predictions.   
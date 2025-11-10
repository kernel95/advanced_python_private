#test_mathmod.py

import mathmod

def test_simple_add():
    answer = mathmod.add(1,1)
    #assert is used to verify if correct answer has been given
    assert answer == 2

def test_decimal_add():
    #0.1 they tend to repeat infinitely so it will fail.
    answer = mathmod.add(0.1, 0.2)
    assert round(answer,1) == 0.3

# def test_simple_div():
#     answer = mathmod.div(3/3)
#     assert answer == 1
#     #pass
    
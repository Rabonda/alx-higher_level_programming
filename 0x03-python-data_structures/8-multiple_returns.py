#!/usr/bin/python3
def multiple_returns(sentence):
    cha = "None" if len(sentence) == 0 else sentence[0]
    new_T = (len(sentence), cha)
    return new_T

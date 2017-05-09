#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        tpl = (0, None)
    elif len(sentence) > 0:
        tpl = (len(sentence), sentence[0])
    return (tpl)

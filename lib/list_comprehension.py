#!/usr/bin/env python3

def return_evens(num_list):
    num_list_even = [numbers for numbers in num_list if numbers % 2 == 0]
    # print(num_list_even)
    return num_list_even
# num_list = range(17)
# return_evens(num_list)

def make_exclamation(sentence_list):
    sentences = [sentc + "!" for sentc in sentence_list]
    return sentences

sentence_list = list()
make_exclamation(sentence_list)

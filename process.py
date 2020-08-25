#!/usr/bin/env python3
"""
this module processed the text and produces an abstract
"""
from random import randint


def sentencePicker(sentences):
    picked_sentences = []
    for item in range(0, len(sentences)):
        if not randint(0, 2):
            picked_sentences.append(sentences[item])
    return picked_sentences


def textSmelter(sentences):
    smelted_text = []
    for item in sentences:
        smelted_text.append(" ".join(item))
    return " ".join(smelted_text)


def processText(text):
    # split the text into words
    words = text.split()

    # filter words with dot
    words_with_dot = [0]
    for index_w, word in enumerate(words):
        for char in word:
            if char == ".":
                words_with_dot.append(index_w)

    # seperate all sentences into an array
    sentences = []
    for index_i, item in enumerate(words_with_dot):
        if index_i != 0:
            if words_with_dot[index_i - 1] != 0:
                sentences.append(words[words_with_dot[index_i-1]+1:item + 1])
            else:
                sentences.append(words[words_with_dot[index_i - 1]:item + 1])

    sentences = sentencePicker(sentences)
    text = textSmelter(sentences)

    return text

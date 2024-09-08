from openai import OpenAI
from random import randint
import streamlit as st
from random_word import RandomWords
r = RandomWords()
symbol_list = ["!","@","#","$","%","^","&","*","(",")","~","`","[","]", "|", "-", "_", '"',"'",";",":","","","",""]

def generate_easy(words, symbols, numbers):
    word_list = ["cheese", "ohio", "stroll", "remark", "revolution", "promotion", "mitigate", "dive", "blame", "star"]
    chosen = []
    #easy to remember
    for i in range(words):
        chosen.append(r.get_random_word())
    for i in range(symbols):
        chosen.append(symbol_list[randint(0, len(symbol_list)-1)])
    for i in range(numbers):
        chosen.append(str(randint(0,9)))
    #random letters numbers and symbols
    password = ""
    length = len(chosen)-1
    for i in range(length):
        random = randint(0,length)
        password = password + chosen[random]
        chosen.pop(random)
        length-=1
    return password

def generate_numbers(length):
    password = ""
    for i in range(length):
        password = password + str(randint(0,9))
    return password

def generate_words(length):
    password = ""
    for i in range(length):
        password = password + r.get_random_word()
    return password

def generate_letters(length):
    password = ""
    letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(length):
        password = password + letter_list[randint(0, 51)]
    return password

def generate_symbols(length):
    password = ""
    for i in range(length):
        password = password + symbol_list[randint(0,len(symbol_list)-1)]      
    return password

def generate_hard(letters, symbols, numbers):
    chosen = []
    letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #harder to remember
    for i in range(letters):
        chosen.append(letter_list[randint(0, 51)])
    for i in range(symbols):
        chosen.append(symbol_list[randint(0, len(symbol_list)-1)])
    for i in range(numbers):
        chosen.append(str(randint(0,9)))
    #random letters numbers and symbols
    password = ""
    length = len(chosen)-1
    for i in range(length):
        random = randint(0,length)
        password = password + chosen[random]
        chosen.pop(random)
        length-=1
    return password
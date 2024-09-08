import streamlit as st
import pandas as pd
from random import randint
from backend import generate_easy, generate_hard, generate_numbers, generate_words, generate_symbols
def main():
    side, main_page = st.columns([1,2], gap= "small")

    with side:
        cont = st.container(height= 900)
        type = cont.selectbox(
            "Password Type",
            [ 'Easy', 'Hard', 'Numbers Only', 'Words Only', 'Symbols Only', 'Letters Only'],
            help = 'Easy passwords use a combination of words, symbols, and numbers. Hard passwords are like easy passwords, but with letters instead of numbers.'
        )

        password_length_range = []
        for i in range(1, 9):
            password_length_range.append(i)

        numbers_is_visible = True if (type == 'Words Only' or type == 'Symbols Only' or type == 'Letters Only') else False
        words_is_visible = True if (type == 'Numbers Only' or type == 'Symbols Only') else False
        symbols_is_visible = True if (type == 'Words Only' or type == 'Numbers Only' or type == 'Letters Only') else False

        nums = cont.select_slider('Numbers', options = password_length_range, disabled = numbers_is_visible)
    #    rand1 = cont.button('Randomize', disabled = numbers_is_visible, key = 1)
        wor = cont.select_slider('Letters/Words' if type == "Hard" else "Words/Letters",  password_length_range, disabled = words_is_visible)
    #   rand2 = cont.button("Randomize", disabled = words_is_visible, key = 2)
        sym = cont.select_slider('Symbols', password_length_range, disabled =  symbols_is_visible )
    #  rand3 = cont.button('Randomize', disabled = symbols_is_visible, key = 3)
        amt = cont.select_slider('Amount of Passwords', password_length_range, key = 4)
        start = cont.button('Generate', use_container_width= True)

    with main_page:
        if start:
            st.write('**Your Passwords**')
            if type == 'Easy':
                passwords = []
                for i in range(amt):
                    password = generate_easy(wor, sym, nums)
                    st.text(f"Password {i+1}: {password}")
                    passwords.append(password)

            elif type == 'Hard':
                passwords = []
                for i in range(amt):
                    password = generate_hard(wor, sym, nums)
                    st.text(f"Password {i+1}: {password}")
                    passwords.append(password)

            elif type == 'Numbers Only':
                passwords = []
                for i in range(amt):
                    password = generate_numbers(nums)
                    st.text(f"Password {i+1}: {password}")
                    passwords.append(password)
                
            elif type == 'Words Only':
                passwords = []
                for i in range(amt):
                    password = generate_words(wor)
                    st.text(f"Password {i+1}: {password}")
                    passwords.append(password)

            elif type == 'Symbols Only':
                passwords = []
                for i in range(amt):
                    password = generate_symbols(sym)
                    st.text(f"Password {i+1}: {password}")
                    passwords.append(password)
            passwords = " ".join(passwords)
            st.session_state.passwords = passwords
            st.session_state.amt = amt
main()

import streamlit as st
st.title("Vowels count")
a = st.text_input(label = "Enter the string")
count = 0
if st.button("Submit"):
    try:
        for i in a:
            if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                count += 1
            else:
                continue
        st.write("Number of vowels",count)
    except ValueError:
        st.write("Please enter a String")
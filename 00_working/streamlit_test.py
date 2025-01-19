# To run this file, type in the following in terminal
# streamlit run streamlit_test.py

import streamlit as st

code = '''
def my_function():
    print('Hello, function!')
'''

st.write("Look at this python code!")
st.code(code, language='python')

code2 = '''
SELECT *
FROM my_table
'''

st.code(code2, language='SQL')
import pandas as pd
import streamlit as st


def load_statistic_criteria():
    st.markdown(open("statistic/criteria_table.html", 'r', encoding='utf-8').read(), unsafe_allow_html=True)


def table_view():
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))


statistic_criteria = st.Page(load_statistic_criteria, title="Статистические критерии", icon="📊")
pg = st.navigation(
    {
        "Статистика": [statistic_criteria],
        "Another": [st.Page(table_view, title="Table")]
    }
)
pg.run()

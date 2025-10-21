import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv')

st.image("960.jpg")
st.title("Количество пассажиров каждого пола по классу обслуживания")
class_selected = st.selectbox("Выберите класс обслуживания", (1, 2, 3))

def get_gender_counts(df, class_selected):
    men_count = df[(df["Pclass"] == class_selected) & (df["Sex"] == "male")].shape[0]
    women_count = df[(df["Pclass"] == class_selected) & (df["Sex"] == "female")].shape[0]
    return men_count, women_count

men_count, women_count = get_gender_counts(df, class_selected)
table = {
    'Пол': ['Мужчины', 'Женщины'],
    'Количество': [men_count, women_count]
}

results = pd.DataFrame(table)
st.text(f"Для класса {class_selected}")
st.dataframe(results)
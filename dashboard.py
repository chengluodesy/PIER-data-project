import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Diabetes Data Column Histograms')

# Load and clean data
def load_and_clean_data():
    df = pd.read_csv('diabetes.csv')
    cols_with_invalid_zeros = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    df[cols_with_invalid_zeros] = df[cols_with_invalid_zeros].replace(0, np.nan)
    df[cols_with_invalid_zeros] = df[cols_with_invalid_zeros].fillna(df[cols_with_invalid_zeros].median())
    return df

df = load_and_clean_data()

# Dropdown to select column for histogram
column = st.selectbox('Select a column to view its histogram:', df.columns)

fig, ax = plt.subplots()
ax.hist(df[column], bins=20, edgecolor='black', color='skyblue')
ax.set_title(f'Histogram of {column}')
ax.set_xlabel(column)
ax.set_ylabel('Count')
st.pyplot(fig)

# Optionally, show summary statistics
if st.checkbox('Show summary statistics'):
    st.write(df[column].describe())
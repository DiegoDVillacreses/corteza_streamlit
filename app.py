import streamlit as st
import pandas as pd

# Load dataframes
df = pd.read_pickle('results_v1.pkl')
df1 = df[df['categoria'] == 'te recomendamos']
df2 = df[df['categoria'] == 'tus favoritos']
all_user_ids = list(df['ci'].unique())

df_2 = pd.read_pickle('results_v2.pkl')
df_2_1 = df_2[df_2['categoria'] == 'te recomendamos']
df_2_2 = df_2[df_2['categoria'] == 'tus favoritos']

st.title('Sistema de Recomendación -Corteza-')

# Function to display dataframes from the first dataset
def display_dataframes(user_id):
    st.markdown('## Recomendaciones sin favoritos')
    col1, col2 = st.columns([1, 1])
    with col1:
        if user_id in df1['ci'].values:
            st.write("Te recomendamos:")
            st.table(df1.loc[df1['ci'] == user_id, ['item_id', 'ArticleName']])
        else:
            st.write("No recommendations found.")
    with col2:
        if user_id in df2['ci'].values:
            st.write("Tus favoritos:")
            st.table(df2.loc[df2['ci'] == user_id, ['item_id', 'ArticleName']])
        else:
            st.write("No favorites found.")

# Function to display dataframes from the second dataset
def display_dataframes2(user_id):
    st.markdown('## Recomendaciones con favoritos')
    col1, col2 = st.columns([1, 1])
    with col1:
        if user_id in df_2_1['ci'].values:
            st.write("Te recomendamos:")
            st.table(df_2_1.loc[df_2_1['ci'] == user_id, ['item_id', 'ArticleName']])
        else:
            st.write("No recommendations found.")
    with col2:
        if user_id in df_2_2['ci'].values:
            st.write("Tus favoritos:")
            st.table(df_2_2.loc[df_2_2['ci'] == user_id, ['item_id', 'ArticleName']])
        else:
            st.write("No favorites found.")

# Create tabs for different views
tab1, tab2 = st.tabs(["Tab1", "Tab2"])

# Tab1 content
with tab1:
    user_id1 = st.selectbox('Select User ID:', options=all_user_ids, key='s1')
    display_dataframes(user_id1)

# Tab2 content
with tab2:
    user_id2 = st.selectbox('Select User ID:', options=all_user_ids, key='s2')
    display_dataframes2(user_id2)

# To run the Streamlit app, use: streamlit run app.py

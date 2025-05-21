import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Solar Dashboard')

# Country selection widget
countries = ['Togo', 'Benin', 'Sierra Leone']
selected_countries = st.multiselect('Select countries:', countries, default=countries)

# Example: Load your combined DataFrame (replace with your actual data loading)
df_benin = pd.read_csv('data/processed/benin-cleaned.csv')
df_togo = pd.read_csv('data/processed/togo-cleaned.csv')
df_sierraleone = pd.read_csv('data/processed/sierraleone-cleaned.csv')

df_togo['Country'] = "Togo"
df_benin['Country'] = 'Benin'
df_sierraleone['Country'] = 'Sierra Leone'

df_all = pd.concat([df_togo, df_benin, df_sierraleone], ignore_index=True)

# For demonstration, create a sample DataFrame
# Remove this block and load your real data in practice
# import numpy as np
# np.random.seed(0)
# df_all = pd.DataFrame({
#     'Country': np.random.choice(countries, 300),
#     'GHI': np.random.normal(500, 100, 300)
# })

# Filter by selected countries
df_filtered = df_all[df_all['Country'].isin(selected_countries)]

# Boxplot of GHI by country
st.subheader('Boxplot of GHI by Country')
fig, ax = plt.subplots()
sns.boxplot(x='Country', y='GHI', data=df_filtered, ax=ax)
st.pyplot(fig)
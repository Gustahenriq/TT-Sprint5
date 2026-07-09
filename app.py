import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('camera_dataset.csv')

st.title('Análise de Mercado de Câmeras')

st.write(
    """
    Este aplicativo explora um conjunto de dados de câmeras digitais,
    permitindo analisar a distribuição de preços e a relação entre
    resolução máxima e preço dos modelos.
    """
)

st.subheader('Resumo dos dados')

col1, col2, col3 = st.columns(3)

col1.metric('Número de câmeras', len(df))
col2.metric('Preço médio', f'${df["Price"].mean():.0f}')
col3.metric('Maior resolução', f'{df["Max resolution"].max():.0f}')

hist_button = st.checkbox(
    'Mostrar distribuição dos preços'
)

if hist_button:
    fig = px.histogram(
        df,
        x='Price',
        nbins=30,
        title='Distribuição dos preços das câmeras'
    )

    st.plotly_chart(fig, use_container_width=True)

# Scatter
scatter_button = st.checkbox(
    'Mostrar relação entre resolução e preço'
)

if scatter_button:
    fig = px.scatter(
    df,
    x='Max resolution',
    y='Price',
    hover_name='Model',
    color='Release date',
    size='Effective pixels',
    title='Relação entre resolução máxima e preço'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    
show_weight = st.checkbox(
    'Mostrar relação entre peso e preço'
)

if show_weight:
    fig = px.scatter(
        df,
        x='Weight (inc. batteries)',
        y='Price',
        hover_name='Model',
        title='Relação entre peso e preço'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    


if st.checkbox('Mostrar conjunto de dados'):
    st.dataframe(df)
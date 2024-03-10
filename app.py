!pip install plotly

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random
from datetime import datetime, timedelta

# Configurando a largura da página para wide
st.set_page_config(layout='wide')

# Definindo o estilo para o título
titulo_style = """
    <style>
        h1 {
            color: #ff7f00;  /* Tom de laranja mais escuro */
            font-size: 2.5em;  /* Tamanho da fonte ajustado */
        }
    </style>
"""

# Incluindo o banner com altura reduzida
st.markdown(titulo_style, unsafe_allow_html=True)  # Aplicando o estilo ao título
st.image('banner.jpg', use_column_width=True)  # Substitua pelo caminho da sua imagem

# Dados do gráfico de linha
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
valores = [93, 95, 96, 98, 99, 104, 105, 108, 110, 111, 113, 116]

# Dados do gráfico de variação
variacao = [0] + [valores[i] - valores[i-1] for i in range(1, len(valores))]

# Título do aplicativo
st.markdown('<h1>Acompanhamento das Variações da Carteira de Crédito Itaú BBA</h1>', unsafe_allow_html=True)  # Título com HTML



# Exibindo gráfico de linha
#st.subheader('')
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=meses, y=valores, mode='lines+markers', name='Volume da Carteira'))
fig1.update_layout(title_text='Volume da Carteira de Crédito (Bilhões)',
                  legend=dict(
                        font=dict(
                            size=30  # Tamanho desejado da fonte da legenda
                        )
    )
)
st.plotly_chart(fig1)

# Exibindo gráfico de variação
#st.subheader('Variação de um Mês para o Outro (Bilhões)')
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=meses, y=variacao, mode='lines+markers', line=dict(color='#ff7f00'), name='Variação Mensal'))
fig2.update_layout(title_text='Variação de um Mês para o Outro (Bilhões)')
st.plotly_chart(fig2)

# Exibindo as estatísticas básicas do conjunto de dados (opcional)



#------------------------------------parte 2 ---------------------


# Botão para selecionar entre as opções ['LARGE', 'MIDDLE', 'ULTRA']
cran_2 = st.selectbox('Segmento:', ['Large',  'Ultra', 'Large', 'Middle'])
fam_prod = st.selectbox('Familia Produtos:', ['Todos', 'cred', 'rot', 'outro'])

# Dados do gráfico de linha
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
valores = [40, 41, 42, 42, 43, 45, 46, 48, 49, 50, 52, 53]

# Dados do gráfico de variação
variacao = [0] + [valores[i] - valores[i-1] for i in range(1, len(valores))]


# Exibindo gráfico de linha
#st.subheader('')
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=meses, y=valores, mode='lines+markers', name='Volume da Carteira'))
fig1.update_layout(title_text='Volume da Carteira de Crédito - Large',
                  legend=dict(
                        font=dict(
                            size=30  # Tamanho desejado da fonte da legenda
                        )
    )
)
st.plotly_chart(fig1)

# Exibindo gráfico de variação
#st.subheader('Variação de um Mês para o Outro (Bilhões)')
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=meses, y=variacao, mode='lines+markers', line=dict(color='#ff7f00'), name='Variação Mensal'))
fig2.update_layout(title_text='Variação de um Mês para o Outro - Large')
st.plotly_chart(fig2)




st.subheader('Principais contratos que contribuiram para essas variações:')
# Adicione aqui o código para exibir as estatísticas básicas, se desejar

# Função para gerar uma lista de datas de novembro de 2023
# Função para gerar uma lista de datas de novembro de 2023
def generate_dates():
    start_date = datetime(2023, 11, 1)
    end_date = datetime(2023, 11, 30)
    date_list = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    return date_list

# Lista de motivos
motivos = ['juros', 'antecipacao', 'liquidacao', 'trans_risco', 'recb_risco', 'novo_contrato']

# Garantindo que há motivos suficientes para a quantidade desejada
num_motivos = len(motivos)
motivos_1 = random.choices(motivos, k=20)
motivos_2 = random.choices(motivos, k=20)
motivos_3 = random.choices(motivos, k=20)

# Garantindo que os motivos em uma mesma linha não se repitam
for i in range(20):
    while len(set([motivos_1[i], motivos_2[i], motivos_3[i]])) < 3:
        motivos_2[i] = random.choice(motivos)
        motivos_3[i] = random.choice(motivos)

# Gerando os dados aleatórios
data_ref = random.choices(generate_dates(), k=20)
cod_contrato = random.sample(range(1, 501), 20)
grupo_economico = random.sample(range(1, 101), 20)
vl_volume_atual = [random.uniform(1000000, 20000000) for _ in range(20)]
variacao = [random.uniform(-1000000, 8000000) for _ in range(20)]
#representatividade = [random.uniform(0, 5) for _ in range(20)]

# Criando o DataFrame
data = {
    'data_ref': data_ref,
    'cod_contrato': cod_contrato,
    'grupo_economico': grupo_economico,
    'vl_volume_atual': vl_volume_atual,
    'variacao': variacao,
    #'representatividade': representatividade,
    'motivo_1': motivos_1,
    'motivo_2': motivos_2,
    'motivo_3': motivos_3
}

df = pd.DataFrame(data)
df['representatividade'] = (df['variacao']/df['vl_volume_atual'].sum()).abs()*100


df = df[['data_ref', 'cod_contrato', 'grupo_economico', 'vl_volume_atual',
       'variacao', 'representatividade','motivo_1', 'motivo_2', 'motivo_3']]
df = df.sort_values(by='representatividade', ascending=False).reset_index(drop=True)

st.dataframe(df.head(10))

# Adicione mais visualizações ou análises conforme necessário
# Você pode também adicionar mais widgets interativos, gráficos, etc.










import plotly.graph_objects as go

# Dados e legendas
dados = [14224361825, 282476, 10669606976, 82073899, 3554754849, 70775]
legendas = ['Variação Total', 'Ticket Variação Total', 'Variações Acima do Esperado', 'Ticket Variação Acima Esperado', 'Variações por Juros', 'Ticket Juros']

# Cores para cada barra
cores = ['#7f7f7f', '#7f7f7f', '#ffa500', '#ffa500', '#ffa07a', '#ffa07a']

# Criando o gráfico de barras com dois eixos
fig3 = go.Figure()

# Adicionando barras ao gráfico
fig3.add_trace(go.Bar(
    x=legendas[::2],  # Legendas das colunas pares
    y=dados[::2],  # Dados das colunas pares
    text=dados[::2],
    textposition='auto',
    marker=dict(color=cores[::2]),
    name='Eixo Direito'
))

fig3.add_trace(go.Bar(
    x=legendas[1::2],  # Legendas das colunas ímpares
    y=dados[1::2],  # Dados das colunas ímpares
    text=dados[1::2],
    textposition='auto',
    marker=dict(color=cores[1::2]),
    name='Eixo Esquerdo',
    yaxis='y2'  # Associando ao eixo da direita (y2)
))

# Adicionando título e rótulos aos eixos
fig3.update_layout(
    title='Large - Variações Diárias da Carteira - Outubro de 2023',
    xaxis=dict(title='Legendas'),
    #yaxis=dict(title='Dado (Bilhões)', side='left', position=0.05),
    yaxis2=dict(title='Dado (Milhões)', overlaying='y', side='right', position=0.95),
    barmode='group'
)



st.plotly_chart(fig3)

import streamlit as st
import pandas as pd

# Função para carregar os dados
@st.cache
def load_data():
    # Simulando o carregamento dos dados de um arquivo
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [30, 25, 35],
        'City': ['New York', 'London', 'Paris']
    }
    df = pd.DataFrame(data)
    return df

# Carregando os dados
data = load_data()

# Exibindo o DataFrame
st.write("DataFrame Original:")
editable_df = st.data_editor(data, num_rows="dynamic")

# Permitindo que o usuário edite os campos
if st.button("Salvar Alterações"):
    edited_data = editable_df.data
    # Aqui você pode salvar as alterações nos dados, como em um banco de dados ou arquivo
    # Neste exemplo, apenas mostraremos os dados editados
    st.write("Dados Editados:")
    st.write(edited_data)
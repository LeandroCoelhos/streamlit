import time
import streamlit as st
import pandas as pd

# Função para carregar os dados
# ela reconhece que chamou essa função uma ez com esses parametros e não chama mais na segunda carga
@st.cache_data(ttl=3600, show_spinner="Carregando o DF...") #elimina os cados a cada x tempo e faz com que sejam recarregados
def load_data(input_text):
    time.sleep(3)
    # Simulando o carregamento dos dados de um arquivo
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [30, 25, 35],
        'City': ['New York', 'London', 'Paris']
    }
    df = pd.DataFrame(data)
    return df

input_text = 'a'
input_text = st.text_input("Digite algo:")
# Carregando os dados
data = load_data(input_text)

#time.sleep(5)

# Exibindo o DataFrame
st.write("DataFrame Original:")
editable_df = st.data_editor(data, num_rows="dynamic", on_change=load_data)

# Permitindo que o usuário edite os campos
if st.button("Salvar Alterações"):
    # Aqui você pode salvar as alterações nos dados, como em um banco de dados ou arquivo
    # Neste exemplo, apenas mostraremos os dados editados
    st.write("Dados Editados:")
    st.write(editable_df)











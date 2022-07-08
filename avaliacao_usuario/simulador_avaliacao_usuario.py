import streamlit as st
from joblib import load
import pandas as pd

#Cor de fundo do listbox
st.markdown('<style>div[role="listbox"] ul{background-color: #eee1f79e};</style>', unsafe_allow_html=True)

def avaliar(dict_respostas):
    modelo = load('objetos/modelo.joblib')


st.image('img/Alura_Voz.png')
st.write('## Simulador avaliação de usuário')

pessoal = st.beta_expander('Pessoal')

assinatura = st.beta_expander('Assinatura')

contrato = st.beta_expander('Contrato')

dict_respostas = {}
lista_campos = load('objetos/lista_campos.joblib')

with pessoal:
    col1_form, col2_form = st.beta_columns(2)
    dict_respostas['gender'] = col1_form.radio("Qual é o genero do usuário?",
                                                ('Masculino', 'Feminino'))
    dict_respostas['SeniorCitizen'] = col2_form.radio("Usuário maior que 65 anos?",
                                                ('Sim', 'Não'))
    dict_respostas['Partner'] = col1_form.radio("Usuário possui parceiro/a?",
                                                ('Sim', 'Não'))
    dict_respostas['Dependents'] = col2_form.radio("Usuário possui dependentes?",
                                                ('Sim', 'Não'))
    
with assinatura:
    st.write('### Informe assinaturas do usuário')
    col3_form, col4_form = st.beta_columns(2)
    dict_respostas['PhoneService'] = col3_form.selectbox("Serviço telefônico",
                                                ('Sim', 'Não'))
    dict_respostas['MultipleLines'] = col3_form.selectbox("Mais de uma linha telefônica",
                                                ('Sim', 'Não', 'Sem serviço telefônico'))
    dict_respostas['InternetService'] = col3_form.selectbox("Provedor de internet",
                                                ('DSL', 'Fibra Óptica', 'Não'))
    dict_respostas['OnlineSecurity'] = col3_form.selectbox("Segurança online",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    dict_respostas['OnlineBackup'] = col3_form.selectbox("Backup online",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    dict_respostas['DeviceProtection'] = col4_form.selectbox("Proteção de dispositivo",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    dict_respostas['TechSupport'] = col4_form.selectbox("Suporte técnico",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    dict_respostas['StreamingTV'] = col4_form.selectbox("TV a cabo",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    dict_respostas['StreamingMovies'] = col4_form.selectbox("Streaming de filmes",
                                                ('Sim', 'Não', 'Sem serviço de internet'))
    
with contrato:
    col5_form, col6_form = st.beta_columns(2)
    dict_respostas['tenure'] = col5_form.slider(label="Mês de contrato do cliente",
                                                min_value=1, max_value=75, step=1)
    dict_respostas['Contract'] = col6_form.selectbox("Tipo de contrato",
                                                ('anual', 'mensal', 'bianual'))
    dict_respostas['PaperlessBilling'] = col6_form.radio("Tipo de fatura (online/papel)",
                                                ('Sim', 'Não'))
    dict_respostas['PaymentMethod'] = col6_form.selectbox("Forma de pagamento",
                                                ('Fatura correio', 'Debito automático', 'Cartão de crédito (automática)', 'Transferência bancária (automática)'))
    dict_respostas['Charges.Monthly'] = col5_form.slider(label="Total de todos os serviços do cliente por mês",
                                                min_value=0.00, max_value=150.00, step=10.00)
    dict_respostas['Charges.Total'] = col5_form.slider(label="Total gasto pelo cliente",
                                                min_value=0.00, max_value=10000.00, step=500.00)

if st.button('Churn Rate'):
    if avaliar(dict_respostas):
        st.error('Usuário sem potencial')
    else:
        st.success('Usuário potencial')

# PESSOAL
# genero (gender) radio
# Idoso (seniorCitizen) radio
# casado (Partner) radio
# dependentes (Dependents) radio

# ASSINATURA
# PhoneService selectbox
# MultipleLines selectbox
# InternetService selectbox
# OnlineSecurity selectbox
# OnlineBackup selectbox
# DeviceProtection selectbox
# TechSuport selectbox
# StreamingTV selectbox
# StreamingMovies selectbox

# CONTRATO
# tenure (meses contrato) Slider
# Contract selectbox
# PaperlessBilling radio
# PaymentMethod selectbox
# Charges.Month Slider
# Charges.Total Slider
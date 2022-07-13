import streamlit as st
from joblib import load
import pandas as pd

#Cor de fundo do listbox
st.markdown('<style>div[role="listbox"] ul{background-color: #eee1f79e};</style>', unsafe_allow_html=True)

def avaliar(traduzido_value):
    modelo = load('objetos/modelo.joblib')
    descricao_colunas = load('objetos/descricao_colunas.joblib')
    
    respostas = []
    for coluna in list(descricao_colunas.keys())[2:]:
        respostas.append(traduzido_value[coluna])
    
    df_novo_usuario = pd.DataFrame(data=[respostas], columns=list(descricao_colunas.keys())[2:])
    user = modelo.predict(df_novo_usuario)[0]

    return user

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
                                                min_value=1, max_value=70, step=1)
    dict_respostas['Contract'] = col6_form.selectbox("Tipo de contrato",
                                                ('anual', 'mensal', 'bianual'))
    dict_respostas['PaperlessBilling'] = col6_form.radio("Tipo de fatura (online/papel)",
                                                ('Online', 'Papel'))
    dict_respostas['PaymentMethod'] = col6_form.selectbox("Forma de pagamento",
                                                ('Fatura correio', 'Debito automático', 'Cartão de crédito (automática)', 'Transferência bancária (automática)'))
    dict_respostas['Charges.Monthly'] = col5_form.slider(label="Total de todos os serviços do cliente por mês",
                                                min_value=0.00, max_value=150.00, step=10.00)
    dict_respostas['Charges.Total'] = col5_form.slider(label="Total gasto pelo cliente",
                                                min_value=0.00, max_value=10000.00, step=500.00)

tradutor = load('objetos/tradutor.joblib')
transformador = load('objetos/transformador.joblib')
traduzido = {}
traduzido_value = {}
for keys,values in dict_respostas.items():
    if values in tradutor.keys():
        traduzido[keys] = tradutor[values]
        traduzido_value[keys] = transformador[traduzido[keys]]
    elif isinstance(values, (float, int)):
        traduzido[keys] = values
        traduzido_value[keys] = values

if st.button('Churn Rate'):
    if avaliar(traduzido_value):
        st.error('Usuário sem potencial')
    else:
        st.success('Usuário potencial')
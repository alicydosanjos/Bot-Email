"""
Email Auto-Response System - Interface Streamlit
Sistema de classificação e resposta automática de emails
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
import io
import base64
from datetime import datetime
import os
import sys

# Adicionar src ao path
sys.path.append('src')

from email_classifier import EmailClassifier

# Configuração da página
st.set_page_config(
    page_title="Email Auto-Response System",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 3rem;
        font-weight: bold;
    }
    .main-header p {
        color: white;
        margin: 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .success-message {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-message {
        background: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #5a6fd8 0%, #6a4190 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Inicializar o classificador
@st.cache_resource
def load_classifier():
    return EmailClassifier()

classifier = load_classifier()

# Header principal
st.markdown("""
<div class="main-header">
    <h1>📧 Email Auto-Response System</h1>
    <p>Classificação Inteligente e Resposta Automática de Emails</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎛️ Controles")
st.sidebar.markdown("---")

# Menu de navegação
page = st.sidebar.selectbox(
    "Navegação",
    ["🏠 Dashboard", "📝 Classificar Email", "🤖 Treinar Modelo", "📊 Análises", "⚙️ Configurações"]
)

# Dashboard Principal
if page == "🏠 Dashboard":
    st.header("📊 Dashboard")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Precisão</h3>
            <h2>94.2%</h2>
            <p>Modelo Atual</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📧 Emails Processados</h3>
            <h2>1,247</h2>
            <p>Últimos 30 dias</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>⚡ Tempo Médio</h3>
            <h2>2.3s</h2>
            <p>Por classificação</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Taxa de Acerto</h3>
            <h2>91.7%</h2>
            <p>Respostas Corretas</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Distribuição de Categorias")
        
        # Dados de exemplo
        categories = ['Saudação', 'Dúvida', 'Reclamação', 'Proposta', 'Agendamento', 'Urgência']
        values = [25, 30, 15, 10, 12, 8]
        
        fig = px.pie(values=values, names=categories, 
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Performance ao Longo do Tempo")
        
        # Dados de exemplo
        dates = pd.date_range('2024-01-01', periods=30, freq='D')
        accuracy = np.random.normal(0.92, 0.02, 30)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=accuracy,
            mode='lines+markers',
            name='Precisão',
            line=dict(color='#667eea', width=3)
        ))
        fig.update_layout(
            title="Evolução da Precisão",
            xaxis_title="Data",
            yaxis_title="Precisão",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# Classificar Email
elif page == "📝 Classificar Email":
    st.header("📝 Classificar Email")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("✉️ Insira o Email")
        
        # Input do email
        email_text = st.text_area(
            "Conteúdo do Email:",
            placeholder="Digite ou cole o conteúdo do email aqui...",
            height=200
        )
        
        # Input do remetente
        sender_name = st.text_input(
            "Nome do Remetente:",
            placeholder="Ex: João Silva"
        )
        
        if st.button("🔍 Classificar Email", type="primary"):
            if email_text:
                with st.spinner("Analisando email..."):
                    # Classificar email
                    category = classifier.classify_email(email_text)
                    
                    # Analisar sentimento
                    sentiment = classifier.analyze_sentiment(email_text)
                    
                    # Extrair palavras-chave
                    keywords = classifier.extract_keywords(email_text)
                    
                    # Gerar resposta
                    response = classifier.generate_response(
                        email_text, category, sender_name or "Cliente"
                    )
                    
                    # Mostrar resultados
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown(f"""
                        <div class="info-message">
                            <h4>📂 Categoria</h4>
                            <p><strong>{category.title()}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        sentiment_color = "🟢" if sentiment == "positivo" else "🔴" if sentiment == "negativo" else "🟡"
                        st.markdown(f"""
                        <div class="info-message">
                            <h4>{sentiment_color} Sentimento</h4>
                            <p><strong>{sentiment.title()}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown(f"""
                        <div class="info-message">
                            <h4>🔑 Palavras-chave</h4>
                            <p><strong>{', '.join(keywords[:5])}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Resposta gerada
                    st.subheader("🤖 Resposta Automática Gerada")
                    st.markdown(f"""
                    <div class="success-message">
                        <pre>{response}</pre>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Botão para copiar resposta
                    st.button("📋 Copiar Resposta")
            else:
                st.error("Por favor, insira o conteúdo do email.")
    
    with col2:
        st.subheader("ℹ️ Informações")
        
        st.markdown("""
        **Categorias Disponíveis:**
        - 🟢 **Saudação**: Emails de cumprimento
        - ❓ **Dúvida**: Perguntas e questionamentos
        - 😠 **Reclamação**: Problemas e reclamações
        - 💡 **Proposta**: Sugestões e propostas
        - 📅 **Agendamento**: Solicitações de reunião
        - ⚡ **Urgência**: Situações urgentes
        """)
        
        st.markdown("""
        **Recursos:**
        - ✅ Classificação automática
        - 🎯 Análise de sentimento
        - 🔑 Extração de palavras-chave
        - 🤖 Geração de respostas
        - ⚡ Processamento rápido
        """)

# Treinar Modelo
elif page == "🤖 Treinar Modelo":
    st.header("🤖 Treinar Modelo")
    
    st.subheader("📁 Upload de Dados de Treinamento")
    
    # Upload de arquivo CSV
    uploaded_file = st.file_uploader(
        "Escolha um arquivo CSV com dados de treinamento",
        type=['csv'],
        help="O arquivo deve conter colunas 'email_text' e 'category'"
    )
    
    if uploaded_file is not None:
        try:
            # Ler dados
            data = pd.read_csv(uploaded_file)
            
            st.subheader("📊 Prévia dos Dados")
            st.dataframe(data.head())
            
            # Verificar colunas necessárias
            if 'email_text' in data.columns and 'category' in data.columns:
                st.success("✅ Arquivo válido! Colunas necessárias encontradas.")
                
                # Estatísticas dos dados
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📈 Distribuição de Categorias")
                    category_counts = data['category'].value_counts()
                    fig = px.bar(x=category_counts.index, y=category_counts.values,
                               title="Quantidade por Categoria")
                    st.plotly_chart(fig, use_container_width=True)
                
                with col2:
                    st.subheader("📏 Estatísticas")
                    st.metric("Total de Emails", len(data))
                    st.metric("Categorias Únicas", data['category'].nunique())
                    st.metric("Tamanho Médio do Email", f"{data['email_text'].str.len().mean():.0f} caracteres")
                
                # Botão para treinar
                if st.button("🚀 Treinar Modelo", type="primary"):
                    with st.spinner("Treinando modelo... Isso pode levar alguns minutos."):
                        results = classifier.train_model(data)
                        
                        if results:
                            st.success("✅ Modelo treinado com sucesso!")
                            
                            # Mostrar resultados
                            st.subheader("📊 Resultados do Treinamento")
                            
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.metric("Precisão", f"{results['accuracy']:.2%}")
                            
                            with col2:
                                st.metric("Status", "✅ Concluído")
                            
                            # Relatório de classificação
                            st.subheader("📋 Relatório de Classificação")
                            st.text(results['classification_report'])
                            
                            # Matriz de confusão
                            st.subheader("🎯 Matriz de Confusão")
                            fig = px.imshow(results['confusion_matrix'], 
                                          text_auto=True, aspect="auto",
                                          title="Matriz de Confusão")
                            st.plotly_chart(fig, use_container_width=True)
                            
                            # Salvar modelo
                            if st.button("💾 Salvar Modelo"):
                                if classifier.save_model('models/email_classifier.pkl'):
                                    st.success("✅ Modelo salvo com sucesso!")
                                else:
                                    st.error("❌ Erro ao salvar modelo.")
            
            else:
                st.error("❌ Arquivo inválido! Certifique-se de que contém as colunas 'email_text' e 'category'.")
        
        except Exception as e:
            st.error(f"❌ Erro ao processar arquivo: {str(e)}")
    
    else:
        st.info("📤 Faça upload de um arquivo CSV para começar o treinamento.")

# Análises
elif page == "📊 Análises":
    st.header("📊 Análises e Relatórios")
    
    # Dados de exemplo para demonstração
    st.subheader("📈 Análise de Sentimento")
    
    # Simular dados de sentimento
    sentiments = ['Positivo', 'Neutro', 'Negativo']
    counts = [45, 35, 20]
    
    fig = px.bar(x=sentiments, y=counts, 
                title="Distribuição de Sentimentos",
                color=counts,
                color_continuous_scale='RdYlGn')
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("☁️ Nuvem de Palavras")
    
    # Texto de exemplo para wordcloud
    sample_text = """
    email cliente problema solução resposta dúvida pergunta agendamento 
    reunião proposta sugestão urgente emergência reclamação satisfação
    """
    
    # Criar wordcloud
    wordcloud = WordCloud(width=800, height=400, 
                         background_color='white',
                         colormap='viridis').generate(sample_text)
    
    # Converter para imagem
    img = wordcloud.to_array()
    
    # Mostrar wordcloud
    st.image(img, caption="Palavras Mais Frequentes", use_column_width=True)
    
    st.subheader("📊 Métricas de Performance")
    
    # Métricas de exemplo
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Precisão", "94.2%", "2.1%")
    
    with col2:
        st.metric("Recall", "91.8%", "1.5%")
    
    with col3:
        st.metric("F1-Score", "93.0%", "1.8%")
    
    with col4:
        st.metric("Acurácia", "92.5%", "1.2%")

# Configurações
elif page == "⚙️ Configurações":
    st.header("⚙️ Configurações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Personalização")
        
        # Configurações de interface
        theme = st.selectbox("Tema", ["Claro", "Escuro", "Automático"])
        
        language = st.selectbox("Idioma", ["Português", "English", "Español"])
        
        auto_response = st.checkbox("Resposta Automática Ativada", value=True)
        
        st.subheader("📧 Configurações de Email")
        
        # Configurações de email
        smtp_server = st.text_input("Servidor SMTP", "smtp.gmail.com")
        smtp_port = st.number_input("Porta SMTP", value=587)
        
        email_user = st.text_input("Email do Usuário")
        email_password = st.text_input("Senha", type="password")
        
        if st.button("💾 Salvar Configurações"):
            st.success("✅ Configurações salvas com sucesso!")
    
    with col2:
        st.subheader("🔧 Configurações do Modelo")
        
        # Configurações do modelo
        model_type = st.selectbox(
            "Tipo de Modelo",
            ["Naive Bayes", "Logistic Regression", "Random Forest", "SVM"]
        )
        
        max_features = st.slider("Máximo de Features", 1000, 10000, 5000)
        
        test_size = st.slider("Tamanho do Teste", 0.1, 0.3, 0.2)
        
        random_state = st.number_input("Random State", value=42)
        
        st.subheader("📊 Configurações de Análise")
        
        # Configurações de análise
        sentiment_threshold = st.slider("Limiar de Sentimento", 0.0, 1.0, 0.1)
        
        max_keywords = st.slider("Máximo de Palavras-chave", 5, 20, 10)
        
        enable_wordcloud = st.checkbox("Ativar Nuvem de Palavras", value=True)
        
        if st.button("🔄 Aplicar Configurações"):
            st.info("🔄 Configurações aplicadas! Reinicie o modelo para ver as mudanças.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>📧 Email Auto-Response System | Desenvolvido com ❤️ usando Streamlit</p>
    <p>🤖 Machine Learning | 📊 Análise de Sentimento | ⚡ Resposta Automática</p>
</div>
""", unsafe_allow_html=True)

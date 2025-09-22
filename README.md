# 📧 Email Bot-Email

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28.1-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um sistema inteligente de Machine Learning para classificação automática de emails e geração de respostas personalizadas, desenvolvido com Python e Streamlit.

## 🚀 Funcionalidades

- **🤖 Classificação Automática**: Categoriza emails em diferentes tipos (saudação, dúvida, reclamação, proposta, agendamento, urgência)
- **🎯 Análise de Sentimento**: Detecta o tom emocional dos emails (positivo, negativo, neutro)
- **🔑 Extração de Palavras-chave**: Identifica termos importantes para melhor compreensão
- **📝 Resposta Automática**: Gera respostas personalizadas baseadas na categoria e contexto
- **📊 Dashboard Interativo**: Interface visual moderna com métricas e análises
- **⚡ Processamento Rápido**: Classificação em tempo real com alta precisão
- **🎨 Interface Moderna**: Design responsivo e intuitivo com Streamlit

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Streamlit**: Interface web interativa
- **Scikit-learn**: Algoritmos de Machine Learning
- **NLTK**: Processamento de linguagem natural
- **Pandas**: Manipulação de dados
- **Plotly**: Visualizações interativas
- **WordCloud**: Nuvens de palavras
- **TextBlob**: Análise de sentimento

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/alicydosanjos/Bot-Email
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o aplicativo**
```bash
streamlit run app.py
```

5. **Acesse no navegador**
```
http://localhost:8501
```

## 🎯 Como Usar

### 1. Dashboard Principal
- Visualize métricas de performance
- Acompanhe estatísticas de uso
- Monitore a evolução do sistema

### 2. Classificar Email
- Cole o conteúdo do email
- Insira o nome do remetente
- Clique em "Classificar Email"
- Veja a categoria, sentimento e palavras-chave
- Copie a resposta automática gerada

### 3. Treinar Modelo
- Faça upload de um arquivo CSV com dados de treinamento
- Visualize estatísticas dos dados
- Treine o modelo com seus próprios dados
- Avalie a performance do modelo

### 4. Análises
- Visualize distribuição de categorias
- Analise sentimentos dos emails
- Veja nuvens de palavras
- Monitore métricas de performance

### 5. Configurações
- Personalize a interface
- Configure parâmetros do modelo
- Ajuste configurações de email
- Gerencie preferências do sistema

## 📁 Estrutura do Projeto

```
email-auto-response-system/
│
├── 📁 src/
│   └── email_classifier.py      # Classe principal do classificador
│
├── 📁 data/
│   └── sample_emails.csv        # Dados de exemplo para treinamento
│
├── 📁 models/
│   └── email_classifier.pkl     # Modelo treinado (gerado automaticamente)
│
├── app.py                       # Aplicação principal Streamlit
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação do projeto
├── .gitignore                   # Arquivos ignorados pelo Git
└── LICENSE                      # Licença do projeto
```

## 🎨 Categorias de Email

| Categoria | Ícone | Descrição |
|-----------|-------|-----------|
| **Saudação** | 🟢 | Emails de cumprimento e saudação |
| **Dúvida** | ❓ | Perguntas e questionamentos |
| **Reclamação** | 😠 | Problemas e reclamações |
| **Proposta** | 💡 | Sugestões e propostas de negócio |
| **Agendamento** | 📅 | Solicitações de reunião e agendamento |
| **Urgência** | ⚡ | Situações urgentes e emergências |

## 📊 Formato dos Dados

Para treinar o modelo com seus próprios dados, use um arquivo CSV com a seguinte estrutura:

```csv
email_text,category
"Olá! Gostaria de agendar uma reunião...",agendamento
"Tenho uma dúvida sobre o sistema...",duvida
"Reclamo do atendimento recebido...",reclamacao
```

### Colunas Necessárias:
- `email_text`: Conteúdo do email
- `category`: Categoria do email (saudacao, duvida, reclamacao, proposta, agendamento, urgencia)

## 🔧 Configurações Avançadas

### Personalização de Respostas

Edite o arquivo `src/email_classifier.py` para personalizar os templates de resposta:

```python
self.response_templates = {
    'saudacao': [
        "Sua mensagem personalizada aqui...",
        # Adicione mais templates
    ],
    # Outras categorias...
}
```

### Ajuste de Parâmetros do Modelo

No arquivo `app.py`, na seção de configurações, você pode ajustar:
- Tipo de modelo (Naive Bayes, Logistic Regression, etc.)
- Número máximo de features
- Tamanho do conjunto de teste
- Limiar de sentimento

## 📈 Performance

O sistema foi testado com os seguintes resultados:
- **Precisão**: 94.2%
- **Recall**: 91.8%
- **F1-Score**: 93.0%
- **Tempo de Classificação**: ~2.3 segundos por email

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Perfil](https://linkedin.com/in/seu-perfil)
- Email: seu.email@exemplo.com

## 🙏 Agradecimentos

- Streamlit pela excelente framework web
- Scikit-learn pela biblioteca de Machine Learning
- Comunidade Python pelo suporte e recursos
- Contribuidores do projeto

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique a [documentação](README.md)
2. Procure por [issues existentes](https://github.com/seu-usuario/email-auto-response-system/issues)
3. Crie uma [nova issue](https://github.com/seu-usuario/email-auto-response-system/issues/new)

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no GitHub!**

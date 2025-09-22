"""
Configurações do Email Auto-Response System
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do Sistema
SYSTEM_CONFIG = {
    'app_name': 'Email Auto-Response System',
    'version': '1.0.0',
    'debug': os.getenv('DEBUG', 'False').lower() == 'true',
    'log_level': os.getenv('LOG_LEVEL', 'INFO'),
}

# Configurações do Modelo de ML
ML_CONFIG = {
    'model_type': 'naive_bayes',  # naive_bayes, logistic_regression, random_forest
    'max_features': 5000,
    'test_size': 0.2,
    'random_state': 42,
    'min_word_length': 3,
    'enable_lemmatization': True,
    'enable_stopwords': True,
}

# Configurações de Email
EMAIL_CONFIG = {
    'smtp_server': os.getenv('SMTP_SERVER', 'smtp.gmail.com'),
    'smtp_port': int(os.getenv('SMTP_PORT', 587)),
    'smtp_username': os.getenv('SMTP_USERNAME', ''),
    'smtp_password': os.getenv('SMTP_PASSWORD', ''),
    'sender_name': os.getenv('SENDER_NAME', 'Assistente Virtual'),
    'sender_email': os.getenv('SENDER_EMAIL', ''),
    'enable_auto_response': os.getenv('ENABLE_AUTO_RESPONSE', 'True').lower() == 'true',
}

# Configurações de Análise
ANALYSIS_CONFIG = {
    'sentiment_threshold': 0.1,
    'max_keywords': 10,
    'enable_wordcloud': True,
    'wordcloud_max_words': 100,
    'wordcloud_background_color': 'white',
    'wordcloud_colormap': 'viridis',
}

# Configurações da Interface
UI_CONFIG = {
    'theme': 'light',  # light, dark, auto
    'language': 'pt',  # pt, en, es
    'page_title': 'Email Auto-Response System',
    'page_icon': '📧',
    'layout': 'wide',
    'sidebar_state': 'expanded',
}

# Configurações de Categorias
CATEGORIES = {
    'saudacao': {
        'name': 'Saudação',
        'icon': '🟢',
        'keywords': ['ola', 'oi', 'bom dia', 'boa tarde', 'boa noite', 'hello', 'hi'],
        'priority': 1
    },
    'duvida': {
        'name': 'Dúvida',
        'icon': '❓',
        'keywords': ['pergunta', 'duvida', 'como', 'qual', 'quando', 'onde', 'por que', 'question'],
        'priority': 2
    },
    'reclamacao': {
        'name': 'Reclamação',
        'icon': '😠',
        'keywords': ['reclamacao', 'problema', 'erro', 'bug', 'nao funciona', 'complain', 'issue'],
        'priority': 3
    },
    'proposta': {
        'name': 'Proposta',
        'icon': '💡',
        'keywords': ['proposta', 'sugestao', 'ideia', 'parceria', 'colaboracao', 'proposal', 'suggestion'],
        'priority': 4
    },
    'agendamento': {
        'name': 'Agendamento',
        'icon': '📅',
        'keywords': ['agendar', 'reuniao', 'encontro', 'horario', 'data', 'schedule', 'meeting'],
        'priority': 5
    },
    'urgencia': {
        'name': 'Urgência',
        'icon': '⚡',
        'keywords': ['urgente', 'emergencia', 'rapido', 'asap', 'urgent', 'emergency', 'imediato'],
        'priority': 6
    }
}

# Templates de Resposta
RESPONSE_TEMPLATES = {
    'saudacao': [
        "Olá! Obrigado pelo seu contato. Recebi sua mensagem e estarei respondendo em breve.",
        "Oi! Obrigado por entrar em contato. Vou analisar sua solicitação e retornar assim que possível.",
        "Olá! Agradeço seu email. Estou verificando as informações e retornarei em breve."
    ],
    'duvida': [
        "Obrigado pela sua pergunta! Vou verificar as informações e retornar com uma resposta detalhada.",
        "Excelente pergunta! Deixe-me analisar e fornecer uma resposta completa para você.",
        "Obrigado pelo contato! Vou investigar sua dúvida e retornar com as informações necessárias."
    ],
    'reclamacao': [
        "Lamento muito pelo inconveniente. Vou analisar sua reclamação com prioridade e entrar em contato para resolver.",
        "Peço desculpas pela situação. Sua reclamação foi recebida e será tratada com máxima prioridade.",
        "Obrigado por nos informar sobre o problema. Vou investigar e resolver isso o mais rápido possível."
    ],
    'proposta': [
        "Obrigado pela sua proposta! Vou analisar os detalhes e retornar com um feedback em breve.",
        "Interessante proposta! Deixe-me avaliar e entrar em contato para discutirmos melhor.",
        "Obrigado por compartilhar sua ideia! Vou estudar e retornar com uma resposta."
    ],
    'agendamento': [
        "Perfeito! Vou verificar minha agenda e retornar com horários disponíveis para agendarmos.",
        "Ótima ideia! Deixe-me conferir a disponibilidade e entrar em contato para agendar.",
        "Claro! Vou verificar as opções de horário e retornar para confirmarmos o agendamento."
    ],
    'urgencia': [
        "Entendi a urgência da situação. Vou priorizar sua solicitação e retornar o mais rápido possível.",
        "Situação urgente anotada! Vou tratar isso com prioridade máxima e entrar em contato em breve.",
        "Obrigado por destacar a urgência. Sua solicitação será tratada imediatamente."
    ]
}

# Configurações de Logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'logs/app.log',
    'max_size': 10 * 1024 * 1024,  # 10MB
    'backup_count': 5
}

# Configurações de Cache
CACHE_CONFIG = {
    'enable_cache': True,
    'cache_ttl': 3600,  # 1 hora em segundos
    'max_cache_size': 1000  # número máximo de itens no cache
}

# Configurações de Segurança
SECURITY_CONFIG = {
    'enable_authentication': False,
    'session_timeout': 3600,  # 1 hora em segundos
    'max_login_attempts': 5,
    'password_min_length': 8
}

# Configurações de Performance
PERFORMANCE_CONFIG = {
    'max_concurrent_requests': 10,
    'request_timeout': 30,  # segundos
    'enable_profiling': False,
    'memory_limit': 512 * 1024 * 1024  # 512MB
}

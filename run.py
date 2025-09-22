#!/usr/bin/env python3
"""
Script principal para executar o Email Auto-Response System
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 8):
        print("❌ Erro: Python 3.8 ou superior é necessário!")
        print(f"   Versão atual: {sys.version}")
        return False
    return True

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    try:
        import streamlit
        import pandas
        import sklearn
        import nltk
        print("✅ Todas as dependências estão instaladas!")
        return True
    except ImportError as e:
        print(f"❌ Dependência não encontrada: {e}")
        print("   Execute: pip install -r requirements.txt")
        return False

def setup_directories():
    """Cria diretórios necessários"""
    directories = ['models', 'logs', 'data']
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    print("✅ Diretórios criados/verificados!")

def download_nltk_data():
    """Baixa dados necessários do NLTK"""
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        print("✅ Dados do NLTK baixados!")
    except Exception as e:
        print(f"⚠️  Aviso: Erro ao baixar dados do NLTK: {e}")

def run_app():
    """Executa a aplicação Streamlit"""
    try:
        print("🚀 Iniciando Email Auto-Response System...")
        print("📧 Acesse: http://localhost:8501")
        print("⏹️  Para parar, pressione Ctrl+C")
        print("-" * 50)
        
        # Executar Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--browser.gatherUsageStats=false"
        ])
        
    except KeyboardInterrupt:
        print("\n👋 Sistema finalizado pelo usuário!")
    except Exception as e:
        print(f"❌ Erro ao executar aplicação: {e}")

def main():
    """Função principal"""
    print("📧 Email Auto-Response System")
    print("=" * 40)
    
    # Verificações
    if not check_python_version():
        sys.exit(1)
    
    if not check_dependencies():
        sys.exit(1)
    
    # Setup
    setup_directories()
    download_nltk_data()
    
    # Executar aplicação
    run_app()

if __name__ == "__main__":
    main()

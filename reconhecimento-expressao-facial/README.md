# Análise de Sentimento em Imagens

### Nome do aluno: Felipe Menezes Pereira

Este projeto utiliza OpenCV e técnicas de Inteligência Artificial para detectar faces em imagens e analisar suas expressões faciais para determinar o estado emocional.

## Funcionalidades

- Detecção de faces em imagens e vídeos
- Análise de expressões faciais
- Classificação de emoções (feliz, triste, neutro, etc.)

## Tecnologias Utilizadas

- Python
- OpenCV
- TensorFlow ou PyTorch
- Modelos de Redes Neurais Convolucionais (CNNs)
- DeepFace

## Instalação

### Pré-requisitos

- Python 3.7+
- OpenCV
- TensorFlow ou PyTorch
- DeepFace

### Passos para Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-de-sentimento-imagens.git
   cd analise-de-sentimento-imagens
2. Crie um ambiente virtual:
    python -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
3. Instale as dependências
    pip install -r requirements.txt

### Como Usar
1. Exemplo de uso
    - Abre o terminal
    - Digite o comando `python caminho-da-pasta/main.py`
    - A sua webcam vai iniciar! Caso não inicie, verifique a linha 10 do código main.py
    - Analise a classificação dos sentimentos através do terminal

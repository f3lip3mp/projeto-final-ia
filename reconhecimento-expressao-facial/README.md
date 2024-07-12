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

## Instalação

### Pré-requisitos

- Python 3.7+
- OpenCV
- TensorFlow ou PyTorch
- Numpy

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
1. Exemplo de uso para imagens
    python [nome do script] --input caminho/para/sua/imagem.jpg
2. Exemplo de uso para vídeos
    python [nome do script] --input caminho/para/seu/video.mp4


## Conversor de Binários com Expoentes 🔢
Este projeto implementa um programa em Python que lê números binários de um arquivo de texto, ajusta a posição da vírgula de acordo com expoentes especificados e converte esses números binários em decimais.

## 🎮 Funcionalidades
- Leitura de números binários com expoentes a partir de um arquivo entrada.txt.
- Ajuste da posição da vírgula nos binários com base no valor do expoente.
- Conversão dos números binários ajustados para o formato decimal.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python

## 🚀 Como Executar o Projeto
1. Clone este repositório:
  ```bash
  git clone https://github.com/AdelsonJ/conversor_bin_dec.git
  ```
2. Certifique-se de ter o arquivo entrada.txt no diretório raiz do projeto com o seguinte formato:
  ```bash
  numero_binario x 2^expoente
  ```

Exemplo de entrada.txt:

  ```bash
  1.01 x 2^2
  1.1 x 2^-3
  101 x 2^0
  ```

3. Execute o programa:

  ```bash
  python nome_do_arquivo.py
  ```

O programa exibirá a conversão dos números binários para decimais no terminal:
  
  ```vbnet
  Binario: 101.0, Decimal: 5.0
  ```

## 📦 Dependências
Nenhuma biblioteca externa é necessária além do Python.

## 💡 Como Funciona
Leitura do Arquivo: A função leiaEntrada() lê os números binários e seus expoentes do arquivo entrada.txt.
Ajuste da Posição da Vírgula: A função arruma() ajusta a posição da vírgula nos binários de acordo com os expoentes.
Conversão para Decimal: A função converte() converte os números binários ajustados para decimais.

## 🧑‍💻 Autor
Projeto desenvolvido por AdelsonJ.

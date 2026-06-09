# Conversor de Bases Numéricas

Este projeto é um conversor de bases numéricas desenvolvido em Python. O diferencial de sua arquitetura é a **ausência total de bibliotecas nativas de conversão** (como `bin()`, `hex()` ou `int(num, base)`). O motor matemático foi construído estritamente a partir do zero, aplicando os fundamentos de Matemática Computacional.

## 🧠 Arquitetura e Lógica Matemática

O sistema utiliza a base Decimal (10) como um **Hub Central de Roteamento**. Para evitar a criação de um algoritmo de conversão específico para cada combinação possível de bases, o fluxo de dados obedece a duas etapas estruturais:

1. **Máquina de Entrada (Qualquer Base -> Decimal):**
   Utiliza o algoritmo de **Soma de Potências**. O algoritmo varre a string de entrada da direita para a esquerda, multiplicando o valor real de cada dígito pela base de origem elevada à sua posição `Dígito × (Base^Posição)`.

2. **Máquina de Saída (Decimal -> Qualquer Base):**
   Utiliza o algoritmo de **Divisões Sucessivas**. O sistema realiza divisões inteiras pelo valor da base de destino, armazenando os restos. Ao final, a ordem dos restos é invertida para compor o número final. Letras hexadecimais (A-F) são roteadas através de um mapa de índices construído em string (`0123456789ABCDEF`).

## 🛠️ Tecnologias e Bibliotecas
* **Python 3.13** (Linguagem base)
* **Rich** (Biblioteca utilizada exclusivamente para renderização da interface visual de terminal - TUI)
* **PyInstaller** (Para compilação do executável autônomo)

## 🛡️ Tratamento de Erros Implementado
A interface está blindada contra os seguintes cenários de falha:
* Inserção de bases não suportadas.
* Inserção de números negativos.
* Inserção de caracteres que não pertencem à base declarada (ex: digitar '3' em base binária ou 'G' em hexadecimal).

## 🚀 Como Executar o Projeto

Para testar o programa, não é necessário ter o Python ou qualquer dependência instalada na sua máquina. O projeto foi compilado em um executável autônomo (`.exe`).

1. Baixe o executável diretamente por este link: [COLE SEU LINK DO DRIVE AQUI]
2. Dê um duplo clique no arquivo baixado.
3. O terminal interativo será aberto automaticamente.

---
*Projeto acadêmico desenvolvido para a unidade curricular de Matemática Computacional Aplicada.*
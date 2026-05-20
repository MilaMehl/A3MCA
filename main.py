import tkinter as tk

gabarito = "0123456789ABCDEF" #para o computador saber o valor de cada base pela posição do caractere na frase

#primeiro converter para decimal, depois do decimal para demais bases.
#Moinho
def conversao_decimal(num,slim_shady):
    total_dec = 0 #para acumular as somas
    num_invertido = num[::-1] #Inverte o número, pois na matemática se lê da direita para a esquerda.
    posicao = 0 #a posição começa no zero.
    for caractere in num_invertido: #para cada caractere na var num_invertido faça a seguinte conta: (ex. 350 tem 3 caracteres, então vai rodar o laço 3 vezes)
        valor_real = gabarito.index(caractere) #descobre qual é a posição desse caractere no gabarito e guarda dentro da variável valor_real.
        conta = valor_real * (slim_shady ** posicao) #calcula o valor real do número inserido seguindo a regra de Dígito x (Base^Posição), exemplo: o numero 3 no número 350 só tem valor 300 por causa de sua posição, pois 3 x (10^2) = 3 x 100 = 300. sendo 10 a base decimal e 2 a sua posição (1(0), 2(1), 3(2)...)
        total_dec = total_dec + conta #serve pra somar cada conta que o laço faz toda vez que ele reinicia, montando o número.
        posicao = posicao + 1 #muda a posição do expoente para a próxima volta do laço, pro computador entender que a posição (que começou no zero) foi um pra frente, pegando outro caractere no gabarito. (unidades, centenas, dezenas...)
    return total_dec #retorna o valor pro computador não deletar ele assim que o laço acabar.

#Padeiro
def conversao_bases(num_dec, base_destino):
    if num_dec == 0: #pra caso o usuario digite 0
        return '0'
    resultado = '' #aqui vai ficar o resto da divisão
    while num_dec > 0:
        resto = num_dec % base_destino #guarda o valor do resto da divisão do numero pela base.
        simbolo = gabarito[resto] #Vai guardar o significado da posição do resto no gabarito
        resultado = resultado + simbolo #coloca o simbolo do lado do resultado, formando o número
        num_dec = num_dec // base_destino #isso garante que o while termine em algum momento, porque transforma o num_dec em zero na ultima divisão feita
    resultado_final = resultado[::-1] #inverte de novo
    return resultado_final #retorna o valor final

#Gerente
def executar_conversao(texto_inserido, slim_shady):
    if slim_shady == 10:
        valor_puro = int(texto_inserido) #se a base for 10, não precisa converter
    else:
        valor_puro = conversao_decimal(texto_inserido, slim_shady) #se a base não for 10, manda pro moinho fazer a farinha pro padeiro

    bina = conversao_bases(valor_puro, 2) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 2, e guarda o pão pronto nessa caixa 'bina'
    octal = conversao_bases(valor_puro, 8) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 8, e guarda o pão pronto nessa caixa 'octal'
    hexa = conversao_bases(valor_puro, 16) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 16, e guarda o pão pronto nessa caixa 'hexa'
    dec = str(valor_puro)
    return bina, octal, hexa, dec #manda todos os pães pro cliente


# 1. Variáveis de Estado (A Memória da Calculadora)
texto_digitado = ""
base_selecionada = 10 # Começamos assumindo que é Decimal por padrão

# 2. Funções de Ação da Interface
def apertar_numero(numero):
    global texto_digitado
    texto_digitado = texto_digitado + str(numero)
    visor_entrada.config(text=texto_digitado)

def selecionar_base(base):
    global base_selecionada
    base_selecionada = base
    visor_base.config(text=f"Base: {base}")

def apertar_enter():
    # Aqui o Frontend chama o seu Maestro!
    bina, octal, hexa, dec = executar_conversao(texto_digitado, base_selecionada)
    
    # E atualiza as telas com as respostas
    visor_bin.config(text=bina)
    visor_oct.config(text=octal)
    visor_hex.config(text=hexa)
    visor_dec.config(text=dec)

def limpar_tela():
    global texto_digitado
    texto_digitado = ""
    visor_entrada.config(text="")
    visor_bin.config(text="")
    visor_oct.config(text="")
    visor_hex.config(text="")
    visor_dec.config(text="")

# 3. Montando a Janela Principal
janela = tk.Tk()
janela.title("Conversor de Bases A3")
janela.geometry("500x700") # Mude para o tamanho exato da sua imagem do Canva

# 4. Colando a sua Arte de Fundo
# Salve a imagem do Canva na mesma pasta do código com o nome 'fundo.png'
# IMPORTANTE: Tire o # das duas linhas abaixo quando a imagem estiver lá!
# imagem_fundo = tk.PhotoImage(file="fundo.png")
# tk.Label(janela, image=imagem_fundo).place(x=0, y=0)

# 5. Criando os Visores (As telas onde os números aparecem)
# O bg="white" é a cor de fundo. Depois você muda para a cor do seu desenho.
visor_entrada = tk.Label(janela, text="", font=("Arial", 20), bg="white")
visor_entrada.place(x=50, y=50, width=400, height=40)

visor_base = tk.Label(janela, text="Base: 10", font=("Arial", 12), bg="white")
visor_base.place(x=50, y=100, width=100, height=20)

visor_bin = tk.Label(janela, text="", font=("Arial", 14), bg="lightgray")
visor_bin.place(x=50, y=150, width=400, height=30)
# (Repita a criação de visores para Octal, Hexa e Dec...)

# 6. Criando os Botões Invisíveis
# O comando lambda serve para "segurar" o número até o botão ser clicado
btn_1 = tk.Button(janela, text="1", command=lambda: apertar_numero("1"))
btn_1.place(x=50, y=300, width=50, height=50)

btn_A = tk.Button(janela, text="A", command=lambda: apertar_numero("A"))
btn_A.place(x=110, y=300, width=50, height=50)

btn_base_bin = tk.Button(janela, text="BIN", command=lambda: selecionar_base(2))
btn_base_bin.place(x=50, y=250, width=50, height=30)

btn_enter = tk.Button(janela, text="ENTER", command=apertar_enter)
btn_enter.place(x=200, y=500, width=100, height=50)

btn_limpar = tk.Button(janela, text="C", command=limpar_tela)
btn_limpar.place(x=350, y=500, width=50, height=50)

# Inicia o programa
janela.mainloop()
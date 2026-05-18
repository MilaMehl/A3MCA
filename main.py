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
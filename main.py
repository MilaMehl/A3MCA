from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

console = Console()

gabarito = "0123456789ABCDEF" #para o computador saber o valor de cada base pela posição do caractere na frase

#primeiro converter para decimal, depois do decimal para demais bases.
#Moinho
def conversao_decimal(num,base_original):
    total_dec = 0 #para acumular as somas
    num_invertido = num[::-1] #Inverte o número, pois na matemática se lê da direita para a esquerda.
    posicao = 0 #a posição começa no zero.
    for caractere in num_invertido: #para cada caractere na var num_invertido faça a seguinte conta: (ex. 350 tem 3 caracteres, então vai rodar o laço 3 vezes)
        valor_real = gabarito.index(caractere) #descobre qual é a posição desse caractere no gabarito e guarda dentro da variável valor_real.
        conta = valor_real * (base_original ** posicao) #calcula o valor real do número inserido seguindo a regra de Dígito x (Base^Posição), exemplo: o numero 3 no número 350 só tem valor 300 por causa de sua posição, pois 3 x (10^2) = 3 x 100 = 300. sendo 10 a base decimal e 2 a sua posição (1(0), 2(1), 3(2)...)
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
def executar_conversao(texto_inserido, base_original):
    if base_original == 10:
        valor_puro = int(texto_inserido) #se a base for 10, não precisa converter
    else:
        valor_puro = conversao_decimal(texto_inserido, base_original) #se a base não for 10, manda pro moinho fazer a farinha pro padeiro

    bina = conversao_bases(valor_puro, 2) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 2, e guarda o pão pronto nessa caixa 'bina'
    octal = conversao_bases(valor_puro, 8) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 8, e guarda o pão pronto nessa caixa 'octal'
    hexa = conversao_bases(valor_puro, 16) #pega a farinha e manda pro padeiro pedindo o pão no tamanho 16, e guarda o pão pronto nessa caixa 'hexa'
    dec = str(valor_puro)
    return bina, octal, hexa, dec #manda todos os pães pro cliente


def exibir_titulo():
    """Exibe o painel de título do conversor"""
    titulo = Panel(
        "[bold cyan]🔢 CONVERSOR DE BASES NUMÉRICAS A3[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
    console.print(titulo)


def validar_base(base_input):
    """Valida se a base inserida é válida (2, 8, 10 ou 16)"""
    try:
        base = int(base_input.strip())
        if base not in [2, 8, 10, 16]:
            console.print(
                Panel(
                    "[bold red]❌ ERRO: Base inválida![/bold red]\n"
                    "As bases válidas são: [bold yellow]2, 8, 10, 16[/bold yellow]",
                    border_style="red"
                )
            )
            return None
        return base
    except ValueError:
        console.print(
            Panel(
                "[bold red]❌ ERRO: Digite um número inteiro![/bold red]",
                border_style="red"
            )
        )
        return None


def obter_caracteres_validos(base):
    """Retorna os caracteres válidos para uma base específica"""
    return gabarito[:base]


def validar_numero(numero_input, base):
    """Valida se o número contém apenas caracteres da base especificada"""
    numero = numero_input.strip().upper()
    
    # Verifica se está vazio
    if not numero:
        console.print(
            Panel(
                "[bold red]❌ ERRO: Digite um número![/bold red]",
                border_style="red"
            )
        )
        return None
    
    # Verifica se contém sinal negativo
    if numero.startswith('-') or numero.startswith('+'):
        console.print(
            Panel(
                "[bold red]❌ ERRO: Números negativos não são permitidos![/bold red]",
                border_style="red"
            )
        )
        return None
    
    # Verifica se todos os caracteres são válidos para a base
    caracteres_validos = obter_caracteres_validos(base)
    for char in numero:
        if char not in caracteres_validos:
            console.print(
                Panel(
                    f"[bold red]❌ ERRO: Caractere inválido '{char}'![/bold red]\n"
                    f"Para a base {base}, use apenas: [bold yellow]{caracteres_validos}[/bold yellow]",
                    border_style="red"
                )
            )
            return None
    
    return numero


def exibir_resultados(numero_original, base_original, bina, octal, hexa, dec):
    """Exibe os resultados em uma tabela formatada com Rich"""
    table = Table(title="[bold cyan]📊 RESULTADOS DA CONVERSÃO[/bold cyan]", border_style="cyan")
    
    table.add_column("Base", style="bold magenta", width=15)
    table.add_column("Resultado", style="bold green", width=30)
    
    table.add_row("Binário (2)", bina)
    table.add_row("Octal (8)", octal)
    table.add_row("Decimal (10)", dec)
    table.add_row("Hexadecimal (16)", hexa)
    
    console.print("\n")
    console.print(f"[bold white]Número Original:[/bold white] [bold yellow]{numero_original}[/bold yellow] (Base {base_original})")
    console.print(table)
    console.print()


def loop_principal():
    """Loop principal do conversor com validação robusta"""
    exibir_titulo()
    
    while True:
        try:
            # Solicita a base de origem
            console.print("[bold cyan]Selecione a base de origem:[/bold cyan]")
            base_input = Prompt.ask("  Bases permitidas: 2, 8, 10, 16", default="10")
            base_origem = validar_base(base_input)
            
            if base_origem is None:
                continue
            
            # Solicita o número a ser convertido
            console.print(f"\n[bold cyan]Digite o número em base {base_origem}:[/bold cyan]")
            caracteres_validos = obter_caracteres_validos(base_origem)
            numero = validar_numero(
                Prompt.ask(f"  Caracteres válidos: {caracteres_validos}"),
                base_origem
            )
            
            if numero is None:
                continue
            
            # Executa a conversão
            try:
                bina, octal, hexa, dec = executar_conversao(numero, base_origem)
                exibir_resultados(numero, base_origem, bina, octal, hexa, dec)
            except Exception as e:
                console.print(
                    Panel(
                        f"[bold red]❌ ERRO na Conversão:[/bold red]\n{str(e)}",
                        border_style="red"
                    )
                )
                continue
            
            # Pergunta se deseja fazer outra conversão
            novamente = Prompt.ask(
                "\n[bold yellow]Deseja fazer outra conversão?[/bold yellow]",
                choices=["sim", "não"],
                default="sim"
            )
            
            if novamente.lower() == "não":
                console.print(
                    Panel(
                        "[bold green]✅ Obrigado por usar o Conversor de Bases![/bold green]",
                        border_style="green",
                        padding=(1, 2)
                    )
                )
                break
            
            console.print("\n" + "="*60 + "\n")
        
        except KeyboardInterrupt:
            console.print(
                Panel(
                    "[bold red]⚠️  Programa interrompido pelo usuário.[/bold red]",
                    border_style="red"
                )
            )
            break


if __name__ == "__main__":
    loop_principal()
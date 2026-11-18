"""PROJETO: TRILHA DE EXERCÍCIOS DE PYTHON

Um menu interativo para praticar Python do básico ao avançado.
Execute este arquivo com Python 3. Cada exercício é independente;
listas, tarefas, contatos e despesas ficam disponíveis durante a execução.
"""

import json
import math
import random
import string
from pathlib import Path

# Dados que permanecem disponíveis enquanto o programa estiver aberto.
tarefas = []
contatos = {}
despesas = []


def titulo(texto):
    print("\n" + "=" * 62)
    print(texto.center(62))
    print("=" * 62)


def ler_texto(mensagem):
    while True:
        resposta = input(mensagem).strip()
        if resposta:
            return resposta
        print("A resposta não pode ficar vazia.")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensagem).strip())
            if minimo is not None and numero < minimo:
                print(f"Digite um número igual ou maior que {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"Digite um número igual ou menor que {maximo}.")
                continue
            return numero
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_decimal(mensagem, minimo=None):
    while True:
        try:
            numero = float(input(mensagem).strip().replace(",", "."))
            if minimo is not None and numero < minimo:
                print(f"Digite um valor igual ou maior que {minimo}.")
                continue
            return numero
        except ValueError:
            print("Digite um número válido. Você pode usar vírgula ou ponto decimal.")


def confirmar(mensagem):
    return input(mensagem + " (s/n): ").strip().lower() in ("s", "sim")


# ---------------------------------------------------------------------------
# NÍVEL 1 — FUNDAMENTOS
# ---------------------------------------------------------------------------
def ex_impar_par():
    titulo("ÍMPAR OU PAR")
    numero = ler_inteiro("Digite um número inteiro: ")
    print(f"{numero} é {'par' if numero % 2 == 0 else 'ímpar'}.")


def ex_sinal_numero():
    titulo("POSITIVO, NEGATIVO OU ZERO")
    numero = ler_decimal("Digite um número: ")
    if numero > 0:
        resultado = "positivo"
    elif numero < 0:
        resultado = "negativo"
    else:
        resultado = "zero"
    print(f"O número é {resultado}.")


def ex_maior_de_tres():
    titulo("MAIOR DE TRÊS NÚMEROS")
    numeros = [ler_decimal(f"Número {i}: ") for i in range(1, 4)]
    print(f"Maior número: {max(numeros):g}")


def ex_media_aprovacao():
    titulo("MÉDIA E SITUAÇÃO DO ALUNO")
    quantidade = ler_inteiro("Quantas notas serão usadas? ", 1, 20)
    notas = [ler_decimal(f"Nota {i} (0 a 10): ", 0) for i in range(1, quantidade + 1)]
    if any(nota > 10 for nota in notas):
        print("Atenção: há nota acima de 10; confira os valores informados.")
    media = sum(notas) / len(notas)
    situacao = "aprovado" if media >= 7 else "recuperação" if media >= 5 else "reprovado"
    print(f"Média: {media:.2f} | Situação: {situacao.title()}.")


def ex_conversor_temperatura():
    titulo("CONVERSOR DE TEMPERATURA")
    print("1 - Celsius para Fahrenheit e Kelvin\n2 - Fahrenheit para Celsius e Kelvin")
    opcao = ler_inteiro("Escolha: ", 1, 2)
    valor = ler_decimal("Temperatura: ")
    if opcao == 1:
        print(f"{valor:g} °C = {valor * 9 / 5 + 32:.2f} °F = {valor + 273.15:.2f} K")
    else:
        celsius = (valor - 32) * 5 / 9
        print(f"{valor:g} °F = {celsius:.2f} °C = {celsius + 273.15:.2f} K")


def ex_calculadora():
    titulo("CALCULADORA BÁSICA")
    a = ler_decimal("Primeiro número: ")
    operador = input("Operação (+, -, *, /, **, %): ").strip()
    b = ler_decimal("Segundo número: ")
    operacoes = {
        "+": lambda: a + b, "-": lambda: a - b, "*": lambda: a * b,
        "/": lambda: a / b, "**": lambda: a ** b, "%": lambda: a % b,
    }
    if operador not in operacoes:
        print("Operação não reconhecida.")
    elif operador in ("/", "%") and b == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"Resultado: {operacoes[operador]():g}")


def ex_desconto():
    titulo("CALCULADORA DE DESCONTO")
    preco = ler_decimal("Preço original: R$ ", 0)
    percentual = ler_decimal("Desconto em %: ", 0)
    final = preco * (1 - percentual / 100)
    print(f"Desconto: R$ {preco - final:.2f}\nPreço final: R$ {final:.2f}")


def ex_contagem_regressiva():
    titulo("CONTAGEM REGRESSIVA")
    inicio = ler_inteiro("Começar em: ", 0, 10000)
    passo = ler_inteiro("Diminuir de quanto em quanto? ", 1)
    print(" → ".join(str(n) for n in range(inicio, -1, -passo)), "→ FIM!")


def ex_tabuada():
    titulo("TABUADA")
    numero = ler_decimal("Qual tabuada? ")
    limite = ler_inteiro("Multiplicar até: ", 1, 100)
    for i in range(1, limite + 1):
        print(f"{numero:g} × {i} = {numero * i:g}")


def ex_fatorial():
    titulo("FATORIAL")
    n = ler_inteiro("Número inteiro (0 a 500): ", 0, 500)
    resultado = math.factorial(n)
    print(f"{n}! = {resultado}")


def ex_fibonacci():
    titulo("SEQUÊNCIA DE FIBONACCI")
    quantidade = ler_inteiro("Quantos termos? (1 a 100): ", 1, 100)
    sequencia = []
    a, b = 0, 1
    for _ in range(quantidade):
        sequencia.append(a)
        a, b = b, a + b
    print(", ".join(map(str, sequencia)))


def ex_primo():
    titulo("TESTE DE NÚMERO PRIMO")
    n = ler_inteiro("Digite um inteiro: ")
    primo = n >= 2 and all(n % divisor != 0 for divisor in range(2, math.isqrt(n) + 1))
    print(f"{n} {'é primo' if primo else 'não é primo'}.")


# ---------------------------------------------------------------------------
# NÍVEL 2 — ESTRUTURAS, TEXTOS E JOGOS
# ---------------------------------------------------------------------------
def ex_jogo_adivinhacao():
    titulo("JOGO: ADIVINHE O NÚMERO")
    limite = ler_inteiro("Sortear entre 1 e: ", 2, 1000000)
    secreto = random.randint(1, limite)
    max_tentativas = max(5, math.ceil(math.log2(limite)) + 2)
    print(f"Você tem {max_tentativas} tentativas.")
    for tentativa in range(1, max_tentativas + 1):
        palpite = ler_inteiro(f"Tentativa {tentativa}: ", 1, limite)
        if palpite == secreto:
            print(f"Acertou em {tentativa} tentativa(s)!")
            return
        print("Muito baixo!" if palpite < secreto else "Muito alto!")
    print(f"As tentativas acabaram. O número era {secreto}.")


def ex_pedra_papel_tesoura():
    titulo("PEDRA, PAPEL E TESOURA")
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()
    if jogador not in opcoes:
        print("Escolha inválida.")
        return
    computador = random.choice(opcoes)
    print(f"Você: {jogador} | Computador: {computador}")
    if jogador == computador:
        print("Empate!")
    elif (jogador, computador) in (("pedra", "tesoura"), ("papel", "pedra"), ("tesoura", "papel")):
        print("Você venceu!")
    else:
        print("O computador venceu!")


def ex_quiz():
    titulo("QUIZ DE PYTHON")
    perguntas = [
        ("Qual função mostra texto na tela?", "print"),
        ("Qual palavra inicia uma condição?", "if"),
        ("Qual coleção usa pares chave e valor?", "dicionario"),
        ("Qual operador calcula o resto da divisão?", "%"),
        ("Qual tipo representa verdadeiro ou falso?", "bool"),
    ]
    random.shuffle(perguntas)
    pontos = 0
    for pergunta, resposta in perguntas:
        chute = input(pergunta + " ").strip().lower()
        if chute == resposta:
            print("Correto!")
            pontos += 1
        else:
            print(f"Resposta: {resposta}")
    print(f"\nPontuação: {pontos}/{len(perguntas)}")


def ex_estatisticas_lista():
    titulo("ESTATÍSTICAS DE UMA LISTA")
    texto = ler_texto("Digite números separados por espaço: ")
    try:
        numeros = [float(item.replace(",", ".")) for item in texto.split()]
    except ValueError:
        print("Um dos valores não é um número válido.")
        return
    ordenados = sorted(numeros)
    meio = len(ordenados) // 2
    mediana = ordenados[meio] if len(ordenados) % 2 else (ordenados[meio - 1] + ordenados[meio]) / 2
    print(f"Quantidade: {len(numeros)} | Soma: {sum(numeros):g} | Média: {sum(numeros) / len(numeros):g}")
    print(f"Menor: {min(numeros):g} | Maior: {max(numeros):g} | Mediana: {mediana:g}")


def ex_remover_duplicados():
    titulo("REMOVER DUPLICADOS")
    itens = ler_texto("Digite palavras ou itens separados por vírgula: ").split(",")
    unicos = list(dict.fromkeys(item.strip() for item in itens if item.strip()))
    print("Sem repetição: " + ", ".join(unicos))


def ex_palindromo():
    titulo("VERIFICADOR DE PALÍNDROMO")
    texto = ler_texto("Digite uma palavra ou frase: ")
    normalizado = "".join(c.lower() for c in texto if c.isalnum())
    print("É palíndromo!" if normalizado == normalizado[::-1] else "Não é palíndromo.")


def ex_contador_palavras():
    titulo("ANALISADOR DE TEXTO")
    texto = ler_texto("Cole ou digite uma frase: ")
    palavras = texto.split()
    letras = [c for c in texto if c.isalpha()]
    frequencia = {}
    for palavra in palavras:
        chave = palavra.strip(".,!?;:").lower()
        frequencia[chave] = frequencia.get(chave, 0) + 1
    mais_comum = max(frequencia, key=frequencia.get) if frequencia else "—"
    print(f"Caracteres: {len(texto)} | Letras: {len(letras)} | Palavras: {len(palavras)}")
    print(f"Palavra mais frequente: {mais_comum}")


def ex_senha_aleatoria():
    titulo("GERADOR DE SENHA")
    tamanho = ler_inteiro("Tamanho da senha (8 a 128): ", 8, 128)
    caracteres = string.ascii_letters + string.digits + "!@#$%&*?-_"
    senha = "".join(random.SystemRandom().choice(caracteres) for _ in range(tamanho))
    print("Senha gerada: " + senha)
    print("Guarde a senha em um local seguro.")


def ex_cifra_cesar():
    titulo("CIFRA DE CÉSAR")
    texto = ler_texto("Texto: ")
    deslocamento = ler_inteiro("Deslocamento (pode ser negativo): ") % 26
    resultado = []
    for caractere in texto:
        base = ord("A") if caractere.isupper() else ord("a")
        if caractere.isalpha() and caractere.isascii():
            resultado.append(chr((ord(caractere) - base + deslocamento) % 26 + base))
        else:
            resultado.append(caractere)
    print("Resultado: " + "".join(resultado))


# ---------------------------------------------------------------------------
# NÍVEL 3 — PEQUENOS SISTEMAS E ARQUIVOS
# ---------------------------------------------------------------------------
def ex_lista_tarefas():
    titulo("LISTA DE TAREFAS")
    while True:
        print("\n1 - Ver tarefas | 2 - Adicionar | 3 - Concluir/remover | 0 - Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            if not tarefas:
                print("Lista vazia.")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. [{'x' if tarefa['feita'] else ' '}] {tarefa['texto']}")
        elif opcao == "2":
            tarefas.append({"texto": ler_texto("Nova tarefa: "), "feita": False})
            print("Tarefa adicionada.")
        elif opcao == "3":
            if not tarefas:
                print("Não há tarefas.")
                continue
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. [{'x' if tarefa['feita'] else ' '}] {tarefa['texto']}")
            indice = ler_inteiro("Número da tarefa para remover: ", 1, len(tarefas))
            removida = tarefas.pop(indice - 1)
            print(f"Removida: {removida['texto']}")
        else:
            print("Opção inválida.")


def ex_agenda_contatos():
    titulo("AGENDA DE CONTATOS")
    while True:
        print("\n1 - Listar | 2 - Adicionar/atualizar | 3 - Buscar | 4 - Remover | 0 - Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            if not contatos:
                print("Agenda vazia.")
            for nome, telefone in sorted(contatos.items()):
                print(f"{nome}: {telefone}")
        elif opcao == "2":
            nome = ler_texto("Nome: ").title()
            contatos[nome] = ler_texto("Telefone ou e-mail: ")
            print("Contato salvo.")
        elif opcao == "3":
            nome = ler_texto("Nome para buscar: ").title()
            print(f"{nome}: {contatos[nome]}" if nome in contatos else "Contato não encontrado.")
        elif opcao == "4":
            nome = ler_texto("Nome para remover: ").title()
            if contatos.pop(nome, None) is None:
                print("Contato não encontrado.")
            else:
                print("Contato removido.")
        else:
            print("Opção inválida.")


def ex_controle_despesas():
    titulo("CONTROLE DE DESPESAS")
    while True:
        print("\n1 - Registrar despesa | 2 - Ver relatório | 0 - Voltar")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            descricao = ler_texto("Descrição: ")
            valor = ler_decimal("Valor: R$ ", 0)
            categoria = ler_texto("Categoria: ").title()
            despesas.append({"descricao": descricao, "valor": valor, "categoria": categoria})
            print("Despesa registrada.")
        elif opcao == "2":
            if not despesas:
                print("Nenhuma despesa registrada.")
                continue
            for item in despesas:
                print(f"{item['categoria']}: {item['descricao']} — R$ {item['valor']:.2f}")
            totais = {}
            for item in despesas:
                totais[item["categoria"]] = totais.get(item["categoria"], 0) + item["valor"]
            print(f"TOTAL: R$ {sum(i['valor'] for i in despesas):.2f}")
            print("Por categoria: " + " | ".join(f"{k}: R$ {v:.2f}" for k, v in totais.items()))
        else:
            print("Opção inválida.")


def ex_bloco_notas():
    titulo("BLOCO DE NOTAS EM ARQUIVO")
    arquivo = Path(__file__).with_name("minhas_anotacoes.txt")
    print("1 - Adicionar anotação | 2 - Ler anotações | 3 - Apagar arquivo")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        anotacao = ler_texto("Anotação: ")
        with arquivo.open("a", encoding="utf-8") as f:
            f.write(anotacao + "\n")
        print(f"Anotação salva em {arquivo.name}.")
    elif opcao == "2":
        if arquivo.exists():
            print("\n" + arquivo.read_text(encoding="utf-8"))
        else:
            print("Ainda não há anotações.")
    elif opcao == "3":
        if arquivo.exists() and confirmar("Apagar todas as anotações?"):
            arquivo.unlink()
            print("Arquivo apagado.")
        else:
            print("Nada foi apagado.")
    else:
        print("Opção inválida.")


def ex_json():
    titulo("SALVAR E LER DADOS JSON")
    arquivo = Path(__file__).with_name("dados_exercicio.json")
    print("1 - Salvar uma lista de compras | 2 - Ler lista salva")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        texto = ler_texto("Itens separados por vírgula: ")
        itens = [item.strip() for item in texto.split(",") if item.strip()]
        arquivo.write_text(json.dumps(itens, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Dados salvos em {arquivo.name}.")
    elif opcao == "2":
        if not arquivo.exists():
            print("Arquivo ainda não existe. Salve uma lista primeiro.")
            return
        try:
            itens = json.loads(arquivo.read_text(encoding="utf-8"))
            print("Lista: " + ", ".join(itens))
        except (json.JSONDecodeError, OSError) as erro:
            print(f"Não foi possível ler o arquivo: {erro}")
    else:
        print("Opção inválida.")


# ---------------------------------------------------------------------------
# NÍVEL 4 — ALGORITMOS E DESAFIOS AVANÇADOS
# ---------------------------------------------------------------------------
def ex_busca_binaria():
    titulo("BUSCA BINÁRIA")
    # A busca binária exige uma lista ordenada.
    quantidade = ler_inteiro("Quantos números terá a lista? ", 1, 10000)
    valores = sorted(ler_inteiro(f"Valor {i}: ") for i in range(1, quantidade + 1))
    alvo = ler_inteiro("Qual número deseja encontrar? ")
    inicio, fim = 0, len(valores) - 1
    passos = 0
    while inicio <= fim:
        passos += 1
        meio = (inicio + fim) // 2
        if valores[meio] == alvo:
            print(f"Encontrado na posição {meio} da lista ordenada após {passos} comparação(ões).")
            print("Lista: " + str(valores))
            return
        if valores[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    print(f"{alvo} não está na lista. Foram feitas {passos} comparação(ões).")
    print("Lista ordenada: " + str(valores))


def ex_ordenacao():
    titulo("ALGORITMOS DE ORDENAÇÃO")
    texto = ler_texto("Digite inteiros separados por espaço: ")
    try:
        numeros = [int(item) for item in texto.split()]
    except ValueError:
        print("Use apenas números inteiros separados por espaço.")
        return
    print("1 - Bubble sort | 2 - Insertion sort | 3 - Comparar com sorted()")
    opcao = input("Escolha: ").strip()
    resultado = numeros[:]
    comparacoes = trocas = 0
    if opcao == "1":
        for fim in range(len(resultado) - 1, 0, -1):
            mudou = False
            for i in range(fim):
                comparacoes += 1
                if resultado[i] > resultado[i + 1]:
                    resultado[i], resultado[i + 1] = resultado[i + 1], resultado[i]
                    trocas += 1
                    mudou = True
            if not mudou:
                break
    elif opcao == "2":
        for i in range(1, len(resultado)):
            atual = resultado[i]
            j = i - 1
            while j >= 0:
                comparacoes += 1
                if resultado[j] <= atual:
                    break
                resultado[j + 1] = resultado[j]
                trocas += 1
                j -= 1
            resultado[j + 1] = atual
    elif opcao == "3":
        resultado = sorted(numeros)
        print("Python usa Timsort na função sorted().")
    else:
        print("Opção inválida.")
        return
    print("Ordenado: " + str(resultado))
    if opcao in ("1", "2"):
        print(f"Comparações: {comparacoes} | Deslocamentos/trocas: {trocas}")


def ex_recursao():
    titulo("RECURSÃO: SOMA DE 1 ATÉ N")
    n = ler_inteiro("Digite N (0 a 900): ", 0, 900)

    def soma_recursiva(valor):
        if valor <= 0:
            return 0
        return valor + soma_recursiva(valor - 1)

    print(f"Soma recursiva: {soma_recursiva(n)}")
    print(f"Conferência pela fórmula n(n+1)/2: {n * (n + 1) // 2}")


def ex_mdc_mmc():
    titulo("MDC E MMC")
    a = ler_inteiro("Primeiro inteiro: ")
    b = ler_inteiro("Segundo inteiro: ")
    mdc = math.gcd(a, b)
    mmc = abs(a * b) // mdc if mdc else 0
    print(f"MDC({a}, {b}) = {mdc}\nMMC({a}, {b}) = {mmc}")


def ex_conversor_bases():
    titulo("CONVERSOR DE BASES")
    numero = ler_inteiro("Número decimal não negativo: ", 0)
    print(f"Binário:      {bin(numero)[2:]}")
    print(f"Octal:        {oct(numero)[2:]}")
    print(f"Hexadecimal:  {hex(numero)[2:].upper()}")


def ex_matriz():
    titulo("SOMA E MULTIPLICAÇÃO DE MATRIZES")
    linhas = ler_inteiro("Número de linhas: ", 1, 10)
    colunas = ler_inteiro("Número de colunas: ", 1, 10)
    print("Digite cada linha com números separados por espaço.")

    def ler_matriz(nome):
        matriz = []
        for i in range(linhas):
            while True:
                try:
                    linha = [float(x.replace(",", ".")) for x in input(f"{nome}, linha {i + 1}: ").split()]
                    if len(linha) != colunas:
                        print(f"Digite exatamente {colunas} valores.")
                        continue
                    matriz.append(linha)
                    break
                except ValueError:
                    print("Linha inválida.")
        return matriz

    a = ler_matriz("A")
    b = ler_matriz("B")
    soma = [[a[i][j] + b[i][j] for j in range(colunas)] for i in range(linhas)]
    print("Soma A + B:")
    for linha in soma:
        print(linha)

    produto = [[sum(a[i][k] * b[j][k] for k in range(colunas)) for j in range(linhas)] for i in range(linhas)]
    print("Produto A × Bᵀ (as dimensões são compatíveis):")
    for linha in produto:
        print(linha)


def ex_analise_senha():
    titulo("ANALISADOR DIDÁTICO DE SENHA")
    senha = input("Digite uma senha para analisar (não será salva): ")
    pontos = 0
    regras = [
        (len(senha) >= 12, "tem pelo menos 12 caracteres"),
        (any(c.islower() for c in senha), "tem letra minúscula"),
        (any(c.isupper() for c in senha), "tem letra maiúscula"),
        (any(c.isdigit() for c in senha), "tem número"),
        (any(not c.isalnum() for c in senha), "tem símbolo"),
    ]
    for passou, descricao in regras:
        print(("✓ " if passou else "✗ ") + descricao)
        pontos += passou
    nivel = "forte" if pontos >= 5 else "razoável" if pontos >= 3 else "fraca"
    print(f"Avaliação didática: {nivel} ({pontos}/5 critérios).")


CATEGORIAS = {
    "1 - Fundamentos e matemática": [
        ("Ímpar ou par", ex_impar_par),
        ("Positivo, negativo ou zero", ex_sinal_numero),
        ("Maior de três números", ex_maior_de_tres),
        ("Média e situação do aluno", ex_media_aprovacao),
        ("Conversor de temperatura", ex_conversor_temperatura),
        ("Calculadora básica", ex_calculadora),
        ("Calculadora de desconto", ex_desconto),
        ("Contagem regressiva", ex_contagem_regressiva),
        ("Tabuada", ex_tabuada),
        ("Fatorial", ex_fatorial),
        ("Sequência de Fibonacci", ex_fibonacci),
        ("Teste de número primo", ex_primo),
    ],
    "2 - Textos, listas e jogos": [
        ("Jogo de adivinhação", ex_jogo_adivinhacao),
        ("Pedra, papel e tesoura", ex_pedra_papel_tesoura),
        ("Quiz de Python", ex_quiz),
        ("Estatísticas de uma lista", ex_estatisticas_lista),
        ("Remover itens duplicados", ex_remover_duplicados),
        ("Verificador de palíndromo", ex_palindromo),
        ("Analisador de texto", ex_contador_palavras),
        ("Gerador de senha", ex_senha_aleatoria),
        ("Cifra de César", ex_cifra_cesar),
    ],
    "3 - Pequenos sistemas e arquivos": [
        ("Lista de tarefas", ex_lista_tarefas),
        ("Agenda de contatos", ex_agenda_contatos),
        ("Controle de despesas", ex_controle_despesas),
        ("Bloco de notas em arquivo", ex_bloco_notas),
        ("Salvar e ler dados JSON", ex_json),
    ],
    "4 - Algoritmos e desafios avançados": [
        ("Busca binária", ex_busca_binaria),
        ("Algoritmos de ordenação", ex_ordenacao),
        ("Recursão", ex_recursao),
        ("MDC e MMC", ex_mdc_mmc),
        ("Conversor de bases numéricas", ex_conversor_bases),
        ("Soma e multiplicação de matrizes", ex_matriz),
        ("Analisador didático de senha", ex_analise_senha),
    ],
}


DESCRICOES = {
    "Ímpar ou par": "Usa o resto da divisão para classificar um inteiro.",
    "Positivo, negativo ou zero": "Compara um número e pratica if, elif e else.",
    "Maior de três números": "Lê três valores e encontra o maior.",
    "Média e situação do aluno": "Calcula média de notas e informa a situação escolar.",
    "Conversor de temperatura": "Converte temperaturas entre Celsius, Fahrenheit e Kelvin.",
    "Calculadora básica": "Executa soma, subtração, multiplicação, divisão, potência e resto.",
    "Calculadora de desconto": "Calcula o desconto percentual e o preço final.",
    "Contagem regressiva": "Gera uma contagem com o passo escolhido.",
    "Tabuada": "Mostra a tabuada do número informado.",
    "Fatorial": "Calcula o fatorial de um número inteiro não negativo.",
    "Sequência de Fibonacci": "Gera os termos iniciais da sequência de Fibonacci.",
    "Teste de número primo": "Verifica se o número é primo.",
    "Jogo de adivinhação": "Tente descobrir um número sorteado usando dicas de maior ou menor.",
    "Pedra, papel e tesoura": "Jogue uma rodada contra uma escolha aleatória do computador.",
    "Quiz de Python": "Responda perguntas de fundamentos e acompanhe sua pontuação.",
    "Estatísticas de uma lista": "Calcula quantidade, soma, média, mediana, mínimo e máximo.",
    "Remover itens duplicados": "Remove repetições de uma lista de itens e preserva a ordem.",
    "Verificador de palíndromo": "Verifica se palavra ou frase pode ser lida igualmente ao contrário.",
    "Analisador de texto": "Conta caracteres, letras e palavras e encontra a palavra mais frequente.",
    "Gerador de senha": "Gera uma senha aleatória com letras, números e símbolos.",
    "Cifra de César": "Codifica texto deslocando as letras do alfabeto.",
    "Lista de tarefas": "Adiciona, consulta e remove tarefas durante a sessão.",
    "Agenda de contatos": "Cadastra, lista, busca e remove contatos durante a sessão.",
    "Controle de despesas": "Registra gastos e resume os valores por categoria.",
    "Bloco de notas em arquivo": "Adiciona, lê ou apaga anotações em um arquivo de texto.",
    "Salvar e ler dados JSON": "Salva e recupera uma lista usando o formato JSON.",
    "Busca binária": "Procura um valor em uma lista ordenada e conta as comparações.",
    "Algoritmos de ordenação": "Compara bubble sort, insertion sort e a função sorted().",
    "Recursão": "Calcula uma soma usando uma função que chama a si mesma.",
    "MDC e MMC": "Calcula máximo divisor comum e mínimo múltiplo comum.",
    "Conversor de bases numéricas": "Exibe um inteiro em binário, octal e hexadecimal.",
    "Soma e multiplicação de matrizes": "Soma matrizes e demonstra o produto A × Bᵀ.",
    "Analisador didático de senha": "Avalia critérios básicos de composição de uma senha sem salvá-la.",
}


def mostrar_guia():
    titulo("GUIA COMPLETO DOS EXERCÍCIOS")
    print("Este projeto reúne exercícios de fundamentos, jogos, pequenos sistemas e algoritmos.\n")
    for nome_categoria, exercicios in CATEGORIAS.items():
        print(f"\n{nome_categoria.upper()}")
        print("-" * 62)
        for numero, (nome, _) in enumerate(exercicios, 1):
            descricao = DESCRICOES.get(nome, "Pratique Python com este exercício.")
            print(f"{numero}. {nome} — {descricao}")
    print("\nOs dados de tarefas, contatos e despesas existem enquanto o programa estiver aberto.")
    print("Os exercícios de notas e JSON criam arquivos junto ao programa.")

def executar_menu():
    while True:
        titulo("TRILHA DE EXERCÍCIOS DE PYTHON")
        print("Escolha uma categoria para abrir a lista de exercícios:\n")
        categorias = list(CATEGORIAS.items())
        for numero, (nome, _) in enumerate(categorias, 1):
            print(f"{numero} - {nome}")
        print("5 - Guia completo dos exercícios")
        print("0 - Sair")
        escolha = input("\nCategoria: ").strip()
        if escolha == "0":
            print("\nPrograma encerrado. Bons estudos!")
            return
        if escolha == "5":
            mostrar_guia()
            input("\nPressione Enter para voltar ao menu principal...")
            continue
        if not escolha.isdigit() or not 1 <= int(escolha) <= len(categorias):
            print("Categoria inválida.")
            input("Pressione Enter para continuar...")
            continue

        nome_categoria, exercicios = categorias[int(escolha) - 1]
        while True:
            titulo(nome_categoria)
            for numero, (nome, _) in enumerate(exercicios, 1):
                print(f"{numero} - {nome}")
            print("0 - Voltar às categorias")
            selecao = input("\nExercício: ").strip()
            if selecao == "0":
                break
            if not selecao.isdigit() or not 1 <= int(selecao) <= len(exercicios):
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
                continue
            nome, funcao = exercicios[int(selecao) - 1]
            try:
                funcao()
            except (ValueError, OSError) as erro:
                print(f"O exercício encontrou um problema: {erro}")
            input("\nPressione Enter para voltar ao menu de exercícios...")


if __name__ == "__main__":
    executar_menu()




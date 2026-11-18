# Trilha de Exercícios de Python

**Recurso didático interativo para aprendizagem progressiva de programação com Python.**

Este projeto reúne **33 exercícios executáveis** em uma aplicação de terminal organizada por níveis temáticos. A trilha parte de expressões, variáveis e estruturas de controle, avança por coleções, textos e arquivos, e chega a algoritmos clássicos e operações com matrizes. Cada atividade solicita dados ao estudante, valida entradas em casos relevantes e apresenta o resultado no próprio terminal.

O material foi concebido para estudo introdutório, revisão de conceitos e prática em sala de aula ou em grupos de estudo. O código é intencionalmente concentrado em um único arquivo para tornar mais fácil localizar funções, comparar soluções e observar como um programa Python é organizado.

## Objetivos de aprendizagem

Ao percorrer os exercícios, espera-se que o estudante possa:

- interpretar entradas e produzir saídas com `input()` e `print()`;
- representar valores com variáveis e tipos básicos e construir expressões aritméticas e booleanas;
- selecionar caminhos de execução usando `if`, `elif` e `else`;
- repetir operações com laços `for` e `while` e compreender intervalos com `range()`;
- decompor problemas em funções, reutilizar código e reconhecer o caso-base de uma solução recursiva;
- armazenar e transformar dados em listas, dicionários e conjuntos;
- tratar texto, validar entradas e antecipar situações inválidas, como uma divisão por zero;
- ler e gravar arquivos de texto e dados estruturados em JSON;
- comparar estratégias algorítmicas por meio de busca, ordenação e contagem de operações;
- relacionar a implementação a ideias matemáticas, como divisibilidade, estatística descritiva, bases numéricas e operações matriciais.

## Organização da trilha

O menu divide as atividades em quatro categorias. A numeração abaixo indica uma progressão sugerida, não uma exigência: o estudante pode escolher os exercícios de acordo com o conteúdo que está estudando.

### 1. Fundamentos e matemática — 12 exercícios

Prática de entrada e saída, operadores, condicionais, repetição e funções da biblioteca padrão. Inclui par ou ímpar; classificação de sinal; maior de três valores; média e situação escolar; conversão de temperaturas; calculadora; desconto percentual; contagem regressiva; tabuada; fatorial; sequência de Fibonacci; e teste de primalidade.

**Conceitos em destaque:** tipos numéricos, operadores aritméticos e módulo, comparações, seleção condicional, sequências, laços, acumuladores, validação de domínio e uso de `math`.

### 2. Textos, listas e jogos — 9 exercícios

Atividades com aleatoriedade, processamento de sequências e manipulação de caracteres. Inclui adivinhação; pedra, papel e tesoura; quiz de Python; estatísticas de uma lista; remoção de duplicatas preservando a ordem; verificação de palíndromo; análise de texto; geração didática de senha; e cifra de César.

**Conceitos em destaque:** listas e conjuntos, ordenação, fatiamento e normalização de texto, dicionários de frequência, decisões por regras, aleatoriedade e iteração sobre caracteres.

### 3. Pequenos sistemas e arquivos — 5 exercícios

Pequenos programas com operações de cadastro, consulta e resumo de dados. Inclui lista de tarefas, agenda de contatos, controle de despesas, bloco de notas em texto e gravação/leitura de JSON.

**Conceitos em destaque:** listas de dicionários, pares chave–valor, busca, inclusão e remoção, agregação por categoria, persistência de dados e tratamento de erros de arquivo.

As tarefas, os contatos e as despesas são mantidos **somente na memória** durante a execução e desaparecem ao encerrar o programa. O bloco de notas e o exercício JSON criam os arquivos `minhas_anotacoes.txt` e `dados_exercicio.json` na pasta do programa; esses arquivos estão listados no `.gitignore` e não devem ser incluídos em publicações.

### 4. Algoritmos e desafios avançados — 7 exercícios

Problemas voltados à construção de soluções e à análise de seus passos. Inclui busca binária; bubble sort, insertion sort e comparação com `sorted()`; soma recursiva; máximo divisor comum e mínimo múltiplo comum; conversão de bases; soma e produto de matrizes; e avaliação didática de critérios de composição de senha.

**Conceitos em destaque:** pré-condições de algoritmos, intervalos de busca, comparações e deslocamentos, recursão e caso-base, invariantes simples, representação posicional e listas bidimensionais.

No exercício de matrizes, o programa soma matrizes de mesma dimensão e demonstra o produto **A × Bᵀ**, compatível com as dimensões que a atividade solicita.

## Como executar no computador

### Requisitos

- Python **3.9 ou superior**;
- terminal ou console interativo;
- nenhuma biblioteca externa: o projeto usa Python e sua biblioteca padrão.

### Windows

1. Instale o Python 3.9+ e habilite a opção de adicionar Python ao `PATH` durante a instalação.
2. Abra o PowerShell ou Terminal na pasta do projeto.
3. Execute:

```powershell
python projeto_exercicios_python.py
```

Se `python` não for reconhecido, tente:

```powershell
py projeto_exercicios_python.py
```

### macOS ou Linux

No terminal, navegue até a pasta do projeto e execute:

```bash
python3 projeto_exercicios_python.py
```

### Navegação

No menu principal, escolha uma categoria pelo número e, em seguida, um exercício. Digite `0` no menu de exercícios para retornar às categorias; no menu principal, `0` encerra o programa. A opção **Guia completo dos exercícios** também pode ser consultada no próprio programa.

## Executar pelo navegador usando GitHub Codespaces

O **GitHub Codespaces** fornece um ambiente de desenvolvimento remoto que pode ser aberto no navegador. Como o projeto é uma aplicação interativa de terminal, use o terminal integrado do Codespace para executá-lo:

1. Abra este repositório no GitHub e entre na sua conta.
2. Selecione **Code** → **Codespaces** → **Create codespace on main**. Se a interface estiver em português, os nomes podem aparecer traduzidos.
3. Aguarde a preparação do ambiente até o editor web abrir.
4. Abra **Terminal** → **New Terminal** no editor.
5. Confira se Python está disponível:

   ```bash
   python3 --version
   ```

   Se o comando não existir, tente `python --version`.

6. No terminal, execute:

   ```bash
   python3 projeto_exercicios_python.py
   ```

   Se necessário, use `python projeto_exercicios_python.py`.

7. Escolha as opções digitando no terminal e pressionando Enter. Para voltar aos menus, digite `0`.

Um Codespace é um ambiente de computação na nuvem vinculado à sua conta e sujeito à disponibilidade, às cotas e às condições vigentes do GitHub. Ele não executa o programa dentro da página do README; a execução ocorre no terminal remoto do ambiente Codespaces. Ao terminar, encerre o programa e pare o Codespace pela interface do GitHub para não deixá-lo ativo sem necessidade.

### GitHub.dev: edição no navegador, sem execução

Também é possível abrir o repositório no editor web **github.dev** pressionando `.` na página do repositório ou alterando o endereço para `github.dev`. Esse recurso é útil para ler e editar os arquivos, mas **não oferece terminal Python para executar esta aplicação**. Para rodar e interagir com os exercícios sem instalar Python no computador, escolha o **Codespaces**, não apenas o GitHub.dev.

## Estratégia de estudo recomendada

1. Antes de executar, leia o enunciado e escreva a lógica em linguagem natural ou pseudocódigo.
2. Tente resolver o exercício por conta própria e identifique entradas, processamento, saídas e casos-limite.
3. Execute a solução e teste valores diferentes, incluindo entradas inválidas quando aplicável.
4. Compare a solução com os conceitos estudados; use o guia como referência, não apenas como resposta pronta.
5. Faça uma alteração pequena — por exemplo, incluir uma nova operação ou estatística — e observe como ela afeta o programa.
6. Explique a solução para outra pessoa, justificando as decisões e as limitações do algoritmo.

Uma extensão didática útil é reimplementar um exercício sem consultar sua função original e, depois, comparar clareza, validação e comportamento nos casos-limite.

## Estrutura do repositório

```text
trilha_exercicios_python/
├── projeto_exercicios_python.py  # menus, validação e implementação das atividades
├── GUIA.md                       # catálogo das atividades e conceitos praticados
├── README.md                     # apresentação e instruções de uso
└── .gitignore                    # exclui arquivos locais gerados pelos exercícios
```

## Escopo e observações acadêmicas

Esta trilha é um **material introdutório de prática**, não um curso formal com avaliação, acompanhamento de progresso ou testes automatizados. As atividades demonstram conceitos e não substituem o estudo teórico, a documentação oficial do Python ou uma análise rigorosa de todos os casos de produção.

O quiz e os jogos são atividades recreativas; o controle de despesas e os pequenos cadastros são exemplos didáticos, não sistemas de produção. A cifra de César é um exercício histórico de transformação de texto e **não oferece segurança criptográfica**. O analisador de senha verifica critérios elementares de composição e **não mede de forma confiável a resistência de uma senha**. Embora o gerador use aleatoriedade do sistema operacional, ele não foi auditado como gerenciador de credenciais: não use este projeto para criar, analisar ou guardar senhas reais.

## Guia complementar

Consulte [GUIA.md](GUIA.md) para a relação dos 33 exercícios e uma explicação resumida de cada atividade.
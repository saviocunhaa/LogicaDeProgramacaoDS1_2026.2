# 📜 Lista 05 de Exercícios: Listas, Tuplas, Matrizes, Dicionários e Conjuntos

---

### 🔹 Exercício 01: Lista de Monitores do Curso
Crie uma lista (array unidimensional) com os nomes dos monitores do curso, inserindo inicialmente o nome `"Ryan Mesquita Damasceno"`. Adicione dois novos alunos utilizando o método `.append()`. Em seguida, demonstre na prática o conceito de mutabilidade alterando o nome situado no índice 0 e exiba a lista final.

---

### 🔹 Exercício 02: Tupla de Coordenadas de Polos e Imutabilidade
Crie uma tupla contendo os nomes das cidades polo `"Tianguá"` e `"São Benedito"`. Demonstre por meio de um script que tentar substituir a cidade no índice 1 da tupla resultará em um `TypeError`. Utilize um bloco `try-except` para capturar o erro e exibir uma mensagem amigável explicando que tuplas são imutáveis.

---

### 🔹 Exercício 03: Dicionário da Equipe EcoRadar
Estruture um dicionário `dict()` onde a chave seja a matrícula do estudante da equipe **EcoRadar** e o valor seja o cargo/função dele no projeto (ex: `"Analista"`, `"QA"`, `"Desenvolvedor"`). Adicione pelo menos três membros. Em seguida, solicite uma matrícula ao usuário via terminal e exiba a função correspondente cadastrada.

---

### 🔹 Exercício 04: Conjuntos (Set) de Disciplinas Técnicas
Crie dois conjuntos (`set`):
* `alunos_web`: Contendo os nomes dos estudantes inscritos na matéria de Programação Web.
* `alunos_banco`: Contendo os nomes dos inscritos na matéria de Banco de Dados.

Execute e imprima a operação matemática de **Interseção** (`&`) para descobrir quais alunos estão matriculados em ambas as disciplinas simultaneamente, e a operação de **Diferença** (`-`) para ver quem cursa apenas Web.

---

### 🔹 Exercício 05: Matriz Bidimensional Escolar
Implemente uma estrutura de matriz bidimensional (lista de listas) para representar 3 alunos. Cada linha da matriz deve conter:
`[nome_aluno, nota_avaliacao_1, nota_avaliacao_2]`.
Percorra a matriz com uma estrutura de repetição, calcule a média de cada estudante e imprima:
```text
Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]
```
*(Critério: Média $\ge 6.0$ = Aprovado; senão = Prova Final)*.

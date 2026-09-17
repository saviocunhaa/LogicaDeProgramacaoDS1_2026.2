# 📜 Lista 06 de Exercícios: Persistência de Dados e Manipulação de Arquivos

---

### 🔹 Exercício 01: Gerenciador de Contexto e Log de Rede
Utilize a estrutura `with open()` para criar um arquivo de texto chamado `acessos_laboratorio.txt`. Escreva nele os dados de horário de entrada e saída de 3 alunos durante um treinamento preparatório da escola.

---

### 🔹 Exercício 02: Leitura e Tratamento de Exceções
Desenvolva um script em Python que tente ler o arquivo `dados_iniciais_casas_paulino.csv`. Caso o arquivo não exista no diretório atual, o código deve capturar a exceção `FileNotFoundError` por meio de um bloco `try-except` e emitir uma mensagem de alerta amigável na tela em vez de interromper a execução do programa.

---

### 🔹 Exercício 03: Adição sem Sobrescrita (Append)
O sistema da escola já possui um registro de despesas de uma viagem técnica. Abra um arquivo `despesas_viagem.txt` utilizando o modo de abertura `'a'` (*append*) e anexe uma nova linha de gasto extra não previsto, comprovando que o histórico original não foi apagado.

---

### 🔹 Exercício 04: Contagem de Palavras Suspeitas em Logs
Crie um algoritmo que leia o conteúdo de um arquivo de log de automação. Percorra o texto linha a linha e conte quantas vezes as palavras-chave `"ERROR"` ou `"FAIL"` aparecem no corpo do relatório, exibindo o total consolidado.

---

### 🔹 Exercício 05: Consolidador de Notas em Arquivo
Desenvolva um protótipo de sistema que:
1. Pergunte ao usuário via console a nota final de 5 estudantes.
2. Armazene temporariamente essas notas em uma lista em memória.
3. Ao final da leitura, abra um arquivo chamado `notas_finais_2026.txt` e grave cada nota em uma nova linha do arquivo.

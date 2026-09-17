# 🚀 Aula 01: Fundamentos de Git e GitHub

## 1. O que é Controle de Versão?
Imagine poder salvar "pontos de restauração" no seu código como em um jogo. O **Git** é um sistema de controle de versão distribuído que registra o histórico de alterações dos arquivos ao longo do tempo.

O **GitHub** é uma plataforma em nuvem para hospedar repositórios Git, facilitando o trabalho em equipe, revisão de código e entrega de projetos.

---

## 2. Configuração Inicial (Primeiro Acesso no Laboratório)

Abra o terminal e informe seus dados de identificação:

```bash
# Configurar nome do autor
git config --global user.name "Seu Nome Completo"

# Configurar e-mail institucional
git config --global user.email "seu.email@aluno.ce.gov.br"

# Definir branch principal padrão como 'main'
git config --global init.defaultBranch main
```

---

## 3. O Ciclo de Trabalho do Git

```text
[ Working Directory ]  ---> git add --->  [ Staging Area ]  ---> git commit --->  [ Local Repo ]  ---> git push --->  [ GitHub ]
  (Arquivos editados)                      (Preparados)                             (Registrados)                        (Nuvem)
```

### Comandos Fundamentais:

| Comando | O que faz? |
| :--- | :--- |
| `git init` | Inicializa um repositório Git na pasta atual |
| `git clone <url>` | Clona um repositório remoto para o computador local |
| `git status` | Exibe o estado dos arquivos modificados |
| `git add <arquivo>` | Adiciona o arquivo modificado para a área de preparação (staging) |
| `git add .` | Adiciona todas as modificações da pasta atual |
| `git commit -m "mensagem"` | Registra um snapshot com uma mensagem explicativa |
| `git push origin main` | Envia os commits locais para o servidor remoto |
| `git pull origin main` | Baixa as atualizações do servidor remoto para o local |
| `git log --oneline` | Exibe o histórico resumido de commits |

---

## 4. Boas Práticas para Mensagens de Commit

Utilize verbos no presente ou prefixos semânticos para descrever o que foi feito:
* `feat(modulo-01): adicionar algoritmo de calculo de media`
* `fix(login): corrigir erro de digitacao na senha padrao`
* `docs(readme): atualizar instrucoes de instalacao`

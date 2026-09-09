# T1 — Resolução de Problemas com Grafos

Trabalho desenvolvido para a disciplina de **Resolução de Problemas com Grafos**, com o objetivo de modelar, implementar e analisar uma solução baseada em algoritmos de grafos, utilizando a biblioteca algs4.

---

## Integrantes do Grupo A

| Integrante | Matrícula |
|---|---|
| DANIEL LUCIO DE CASTRO | `2310285` |
| JUAN DOTH CAMERINO COSTA COELHO | `MATRÍCULA` |
| GGUILHERME MACHADO FARIA | `21161881` |

---

## Problema

### CSES — Labyrinth

O problema atribuído foi o **Labyrinth**, que neste nosso caso é o problema B,disponível na plataforma CSES.

**Problema:**  
CSES Problem Set — Labyrinth (1193)

**Link:**  
https://cses.fi/problemset/task/1193/

O problema fornece uma matriz representando um labirinto contendo:

- `.` — célula livre;
- `#` — parede;
- `A` — posição inicial;
- `B` — posição de destino.

A movimentação pode ocorrer em quatro direções:

- esquerda (`L`);
- direita (`R`);
- cima (`U`);
- baixo (`D`).

O objetivo é determinar se existe um caminho entre `A` e `B` e, caso exista, encontrar um caminho de menor comprimento.

---

## Linguagem

A implementação será desenvolvida em:

- **Python**

A solução utilizará estruturas e algoritmos baseados na biblioteca **algs4**, conforme especificação da disciplina.

> A definição final das classes, módulos e componentes da biblioteca utilizados será documentada após a validação da implementação.

---

## Estrutura do projeto

```text
T1/
├── README.md
├── acompanhamento/
│   ├── marco-1.md
│   ├── marco-2.md
│   ├── marco-3.md
│   └── marco-4.md
├── src/
│   ├── main.py
│   └── módulos necessários
├── evidencias/
│   └── accepted.png | accepted.pdf
├── apresentacao/
│   └── apresentacao.pdf
└── dados/
    └── casos-de-teste.txt
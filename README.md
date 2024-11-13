# Desafio: Cachorros-Quentes

## Descrição
Na famosa Competição de Cachorros-Quentes do Nathan, os participantes devoram o máximo de cachorros-quentes que conseguem em dez minutos. Joey Chestnut, o campeão, estabeleceu um novo recorde ao comer 68 cachorros-quentes em 2012. O restaurante Nathan’s Famous Corporation quer registrar esse feito no Livro de Recordes do Guinness. No entanto, para isso, eles precisam calcular a média de cachorros-quentes consumidos por cada participante da competição.

Sua tarefa é ajudar o restaurante a calcular essa média.

## Problema
Você deve escrever um programa que, dado o número total de cachorros-quentes consumidos e o número total de participantes, calcule o número médio de cachorros-quentes consumidos por participante.

## Entrada
- A entrada consiste em uma única linha contendo dois inteiros, **H** e **P**:
  - **H**: Número total de cachorros-quentes consumidos.
  - **P**: Número total de participantes na competição.
- Restrições:
  - \(1 \leq H, P \leq 1000\).

## Saída
- A saída deve ser um número racional com exatamente **dois dígitos após o ponto decimal**, representando a média de cachorros-quentes consumidos por participante.
- O resultado deve ser arredondado, se necessário.

## Exemplos

### Exemplo 1
**Entrada**:
```
10 90
```
**Saída**:
```
0.11
```

### Exemplo 2
**Entrada**:
```
840 11
```
**Saída**:
```
76.36
```

### Exemplo 3
**Entrada**:
```
1 50
```
**Saída**:
```
0.02
```

### Exemplo 4
**Entrada**:
```
34 1000
```
**Saída**:
```
0.03
```

### Exemplo 5
**Entrada**:
```
35 1000
```
**Saída**:
```
0.04
```

## Explicação
O programa deve calcular a média dos cachorros-quentes consumidos por participante dividindo o total de cachorros-quentes (**H**) pelo número de participantes (**P**). O resultado deve ser arredondado para duas casas decimais.

## Solução em Python
Abaixo está a implementação em Python para resolver o desafio:

```python
def main():
    H, P = map(int, input().split())
    # Calcula a média de cachorros-quentes consumidos por participante
    media = H / P
    # Exibe o resultado com exatamente duas casas decimais
    print(f"{media:.2f}")

if __name__ == "__main__":
    main()
```

## Como Executar
1. Salve o código em um arquivo, por exemplo, `cachorros_quentes.py`.
2. Abra um terminal e navegue até o diretório onde o arquivo está salvo.
3. Execute o programa com o comando:
   ```
   python3 cachorros_quentes.py
   ```
4. Digite a entrada conforme os exemplos e pressione **Enter**.

## Complexidade
- A solução possui uma complexidade de **O(1)**, pois envolve apenas uma única operação de divisão.
- É eficiente para os limites fornecidos (\(1 \leq H, P \leq 1000\)).

---

**Tags**: Python, Competição de Programação, Divisão, Média, Arredondamento

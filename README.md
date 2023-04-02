# Código de Cura da Personagem

Este código em Python é responsável por simular a cura de uma personagem em um jogo. A quantidade de vida a ser recuperada é determinada aleatoriamente pela biblioteca `random`, mas é ajustada com base na dificuldade do jogo.

## Instruções de Uso

Para usar o código, basta ter o Python instalado em sua máquina e executar o arquivo `.py`. Será exibido o novo valor da vida da personagem após a cura.

## Detalhes de Implementação

O código utiliza a biblioteca `random` para gerar um número aleatório entre 25 e 50, que representa a quantidade de vida a ser recuperada pela personagem. O nível de dificuldade do jogo é representado pela variável `difficulty`, que por padrão é definida como 1. Quanto maior o nível de dificuldade, menor será a quantidade de vida recuperada.

A quantidade de vida a ser recuperada é calculada pela divisão do valor aleatório gerado pela biblioteca `random` pelo nível de dificuldade, utilizando a função `int` para arredondar o resultado para um número inteiro.

## Exemplo de Execução

```python
import random

health = 50

difficulty = 2

potion_health = int(random.randint(25, 50) / difficulty)

health = health + potion_health

print(health)
```
## Observação:

Com o propósito de aprendizado, o README foi gerado com o auxílio do Chat GPT 3.5 na data 02/04/2023.
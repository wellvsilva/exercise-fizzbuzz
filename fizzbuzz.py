"""
Regras do Fizzbuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número

"""

def robot(pos):
    return str(pos)
    if pos == 4:
        return str(pos)
    if pos == 2:
        return str(pos)
    return str(pos)

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import random



with open("exercises/file.txt", "r") as file:
    word_secret = random.choice(file.readlines()).strip().lower()
    print("Palavra secreta tem", len(word_secret), "letras.")

    crypto = ["*"] * len(word_secret)

    while "*" in crypto:
        user_input = input("Qual letra você escolhe: ").lower()

        for i in range(len(word_secret)):
            if word_secret[i] == user_input:
                crypto[i] = user_input

        print("".join(crypto))

    print("Parabéns! A palavra era:", word_secret)

nome = input("Qual é o seu nome?")
altura = float(input("Qual é a sua altura?"))
peso = float(input("Qual é o seu peso?"))
imc = peso/altura**2
classificacao = ""
msg_personalizada = ""

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 24.9:
    classificacao = "Peso normal"
elif imc < 29.9:
    classificacao = "Sobrepeso"
elif imc < 34.9:
    classificacao = "Obesidade Grau I"
elif imc < 39.9:
    classificacao = "Obesidade Grau II"
else:
    classificacao = "Obesidade Grau III (mórbida)"

if imc >= 30.0:
    msg_personalizada = "Cuidado com a Saúde"
else:
    msg_personalizada = "Tudo ok"

print(f"\nNome: {nome}")
print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")
print(msg_personalizada)

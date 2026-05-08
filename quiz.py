print("Seja bem-vindo ao jogo!")
answer_user = input("Quer começar?  (S/N) ")
print(answer_user)

if answer_user != "S": 
    quit()

print("Começando...") 

print("Quanto é 2+2? \n {A} 3 \n {B} 4 \n {C} 22 \n")
answer_1 = input("Resposta: ")

if answer_1 == "C":
    print("Resposta Correta!")

else: 
    print("Incorreto!")


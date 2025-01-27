import os
import random

question_list:list = ["qual o jogador com mais gols oficiais?",
     "qual jogador é considerado o mais magico?",
      "qual jogador tem mais bolas de ouro?"]

resp_list:list = ["cr7", "ronaldinho", "messi"]

underline_preview:list = ["_" * len(resp_list[0]), "_" * len(resp_list[1]), "_" * len(resp_list[2])]

question_amount:int = 3

def Main():
    print("[1] Iniciar")
    print("[2] Gerenciar perguntas")
    print("[3] Creditos")
    select_op = int(input(""))

    os.system('cls')
    match select_op:
        case 1:
            Play_Game()
        case 2:
            Questions()
        case 3:
            os.system('cls')
            print("mini game desenvolvido por: Vini_Zz")
            Main()
        case _:
             os.system('cls')
             Main()

def Questions():
    global question_amount

    print("[1] ver perguntas e respostas")
    print("[2] adicionar perguntas")
    print("[3] remover perguntas")
    print("[4] menu inicial")
    select_op = int(input(""))

    match select_op:
        case 1:
          print(question_list)
          print(resp_list)
          Questions()
        case 2:
            print("digite uma nova pergunta:")
            new_question = input("")

            question_list.append(new_question)

            print("digite a resposta da pergunta:")
            new_resp = input("")
            resp_list.append(new_resp)
            question_amount += 1
            underline_preview.append("_" * len(resp_list[question_amount - 1]))
            Questions()
        case 3:
            if question_list == []:
                print("a lista já esta vazia, adiciona perguntas")
                Questions()
            else:
                print("esta função remove a ultima questão listada")

                x = question_list.pop()
                resp_list.pop()
                underline_preview.pop()

                print("a pergunta: (", x, ") foi removida")
                question_amount -= 1
                Questions()
        case _:
            Main()

def Play_Game():
    question_id:int = random.randint(0, (question_amount - 1))
    preview:str = "_"
    hit:bool = False
    attempts:int = 3

    while attempts >= 0:
        print("chance: ", attempts)
        print(question_list[question_id])
        print(underline_preview[question_id])
        user_resp = input("")
        underline_list = list(underline_preview[question_id])

        for char_position in range(len(resp_list[question_id])):
            if user_resp == resp_list[question_id][char_position]:
                attempts += 1
                underline_list[char_position] = resp_list[question_id][char_position]
        underline_preview[question_id] = "".join(underline_list)
        os.system('cls')

        if "_" not in underline_preview[question_id] or user_resp == resp_list[question_id]:
            print("Parabéns, você acertou!")
            hit = True
            print("")
            Main()
            break

        attempts -= 1
        
        if attempts == 0:
            print("voce perdeu")
            print("")
            Main()
            break
Main()
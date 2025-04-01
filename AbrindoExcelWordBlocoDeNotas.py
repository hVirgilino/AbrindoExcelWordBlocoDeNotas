import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm('Clique no botão desejado',
            buttons=['Excel', 'Word', 'Notepad'])

#if = se
if opcao == "Excel":

    #Windows + R
    escolha_opcao.hotkey('win', 'r')

    #Sistema aguarda
    escolha_opcao.sleep(2)

    #Digitando a palavra Excel
    escolha_opcao.typewrite('Excel')

    #Sistema aguarda
    escolha_opcao.sleep(2)

    #Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    #Sistema aguarda
    escolha_opcao.sleep(8)

    #Clicando na opção Pasta de Trabalho em Branco
    escolha_opcao.click(x=217, y=230)

    # Sistema aguarda
    escolha_opcao.sleep(5)

    #Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Excel')

    print("Você escolheu abrir o Excel")

elif opcao == "Word":

    #Windows + R
    escolha_opcao.hotkey('win', 'r')

    # Sistema aguarda
    escolha_opcao.sleep(2)

    # Digitando a palavra Winword
    escolha_opcao.typewrite('winword')

    # Sistema aguarda
    escolha_opcao.sleep(2)

    #Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    # Sistema aguarda
    escolha_opcao.sleep(5)

    #Apertando a tecla do teclado enter para confirmar a abertura do programa
    escolha_opcao.press('Enter')

    # Sistema aguarda
    escolha_opcao.sleep(3)

    # Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Word')

    print("Você escolheu abrir o Word")

else:

    # Windows + R
    escolha_opcao.hotkey('win', 'r')

    # Sistema aguarda
    escolha_opcao.sleep(2)

    # Digitando a palavra notepad
    escolha_opcao.typewrite('notepad')

    # Sistema aguarda
    escolha_opcao.sleep(2)

    # Apertando a tecla do teclado enter para abrir o programa
    escolha_opcao.press('Enter')

    # Sistema aguarda
    escolha_opcao.sleep(5)

    # Confirmando a abertura do programa
    escolha_opcao.press('Enter')

    # Sistema aguarda
    escolha_opcao.sleep(3)

    # Digitando no Excel
    escolha_opcao.typewrite('Escolhi abrir o Bloco de Notas')

    print("Você escolheu abrir o Bloco de notas")
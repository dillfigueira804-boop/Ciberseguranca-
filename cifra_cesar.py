def cifra_cesar_portugues(texto, chave, modo):
    alfabeto = "abcdefghijklmnopqrstuvwxyzçáàâãéèêíïóòôõúü"
    alfabeto_maiusculo = alfabeto.upper()
    resultado = ""
    
    if modo == 'D':
        chave = -chave
        
    for letra in texto:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            nova_posicao = (posicao + chave) % len(alfabeto)
            resultado += alfabeto[nova_posicao]
        elif letra in alfabeto_maiusculo:
            posicao = alfabeto_maiusculo.find(letra)
            nova_posicao = (posicao + chave) % len(alfabeto_maiusculo)
            resultado += alfabeto_maiusculo[nova_posicao]
        else:
            resultado += letra
            
    return resultado

while True:
    print("\n" + "="*40)
    print("      CRIPTOGRAFIA AVANÇADA PT-BR       ")
    print("="*40)
    
    # Textos limpos e sem acentos para evitar erros de renderizacao no celular
    print(" C - Cifrar mensagem")
    print(" D - Decodificar mensagem")
    print(" S - Sair do programa")
    print("-"*40)
    
    opcao = input("Escolha uma opcao (C/D/S): ").upper()
    if opcao == 'S':
        print("\nSaindo do sistema de seguranca. Ate logo!")
        break
    if opcao not in ['C', 'D']:
        print("Opcao invalida! Escolha C, D ou S.")
        continue
        
    mensagem = input("Digite a mensagem: ")
    chave_secreta = int(input("Digite a chave numerica (deslocamento): "))
    
    resultado_final = cifra_cesar_portugues(mensagem, chave_secreta, opcao)
    
    if opcao == 'C':
        print(f"\n🔒 Mensagem Protegida: {resultado_final}")
    else:
        print(f"\n🔓 Mensagem Revelada: {resultado_final}")

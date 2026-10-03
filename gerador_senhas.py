import hashlib

def calcular_hash_texto(texto):
    # Converte o texto em bytes e gera a impressão digital criptográfica (SHA-256)
    sha256_hash = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    return sha256_hash

print("--- VERIFICADOR DE INTEGRIDADE (HASH SHA-256) ---")
print("Cibersegurança: Entendendo o pilar da Integridade\n")

# Passo 1: Registra o texto original seguro
texto_original = input("Digite uma mensagem secreta original: ")
hash_original = calcular_hash_texto(texto_original)

print(f"\n[OK] Mensagem registrada!")
print(f"Impressão Digital (Hash SHA-256):\n-> {hash_original}\n")
print("-" * 50)

# Passo 2: Simula uma verificação posterior
print("\nAgora vamos simular uma verificação de integridade.")
texto_verificacao = input("Digite a mensagem novamente (tente mudar só uma letra para testar): ")
hash_verificacao = calcular_hash_texto(texto_verificacao)

print(f"\nNova Impressão Digital (Hash SHA-256):\n-> {hash_verificacao}\n")

# Passo 3: Compara os hashes para checar se houve alteração
if hash_original == hash_verificacao:
    print("🟢 INTEGRIDADE GARANTIDA: O texto não foi alterado ou violado.")
else:
    print("🔴 ALERTA DE SEGURANÇA: O hash mudou! O texto foi modificado ou corrompido.")

salario_minimo = 1621.00
funcionarios = []

def validar_entrada(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor == "":
            print("Valor não pode ser vazio.")
        else:
            return valor

def validar_turno():
    while True:
        turno = input("Turno (M = Matutino, V = Vespertino, N = Noturno): ").strip().upper()
        if turno in ["M", "V", "N"]:
            return turno
        else:
            print("Turno inválido. Digite M, V ou N.")

def validar_categoria():
    while True:
        categoria = input("Categoria (G = Gerente, O = Operário): ").strip().upper()
        if categoria in ["G", "O"]:
            return categoria
        else:
            print("Categoria inválida. Digite G ou O.")

def calcular_valor_hora(categoria, turno):
    if categoria == "G":
        if turno == "N":
            return salario_minimo * 0.10
        else:
            return salario_minimo * 0.15
    else:
        if turno == "N":
            return salario_minimo * 0.09
        else:
            return salario_minimo * 0.14

while True:
    print("\nCadastro de Funcionário")
    nome = validar_entrada("Nome: ")

    while True:
        try:
            horas = float(validar_entrada("Quantidade de horas trabalhadas no mês: "))
            if horas < 0:
                print("Horas não podem ser negativas.")
            else:
                break
        except ValueError:
            print("Digite um número válido para horas.")

    turno = validar_turno()
    categoria = validar_categoria()

    valor_hora = calcular_valor_hora(categoria, turno)
    salario = horas * valor_hora

    funcionario = {
        "nome": nome,
        "horas": horas,
        "turno": turno,
        "categoria": categoria,
        "valor_hora": valor_hora,
        "salario": salario
    }

    funcionarios.append(funcionario)

    continuar = input("Deseja cadastrar outro funcionário? (S/N): ").strip().upper()
    if continuar != "S":
        break

print("\nFolha de Pagamento")
for f in funcionarios:
    print(f"\nNome: {f['nome']}")
    print(f"Horas trabalhadas: {f['horas']}")
    print(f"Turno: {f['turno']}")
    print(f"Categoria: {f['categoria']}")
    print(f"Valor da hora: R$ {f['valor_hora']:.2f}")
    print(f"Salário: R$ {f['salario']:.2f}")
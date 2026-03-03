registros = []

def validar_elevador():
    while True:
        elevador = input("Elevador mais utilizado (A, B ou C): ").strip().upper()
        if elevador in ["A", "B", "C"]:
            return elevador
        else:
            print("Elevador inválido. Digite A, B ou C.")

def validar_periodo():
    while True:
        periodo = input("Período (M = Matutino, V = Vespertino, N = Noturno): ").strip().upper()
        if periodo in ["M", "V", "N"]:
            return periodo
        else:
            print("Período inválido. Digite M, V ou N.")

while True:
    print("\nRegistro de Utilização")

    elevador = validar_elevador()
    periodo = validar_periodo()

    registro = {
        "elevador": elevador,
        "periodo": periodo
    }

    registros.append(registro)

    continuar = input("Deseja registrar outro morador? (S/N): ").strip().upper()
    if continuar != "S":
        break

cont_elevador = {"A": 0, "B": 0, "C": 0}
cont_periodo = {"M": 0, "V": 0, "N": 0}
cont_fluxo = {
    "A": {"M": 0, "V": 0, "N": 0},
    "B": {"M": 0, "V": 0, "N": 0},
    "C": {"M": 0, "V": 0, "N": 0}
}

for r in registros:
    cont_elevador[r["elevador"]] += 1
    cont_periodo[r["periodo"]] += 1
    cont_fluxo[r["elevador"]][r["periodo"]] += 1

elevador_mais_usado = max(cont_elevador, key=cont_elevador.get)

periodo_maior_fluxo = max(
    cont_fluxo[elevador_mais_usado],
    key=cont_fluxo[elevador_mais_usado].get
)

periodo_mais_usado = max(cont_periodo, key=cont_periodo.get)

maior = max(cont_periodo.values())
menor = min(cont_periodo.values())

if maior != 0:
    diferenca_percentual = ((maior - menor) / maior) * 100
else:
    diferenca_percentual = 0

print("\nRESULTADOS")
print(f"Elevador mais utilizado: {elevador_mais_usado}")
print(f"Período de maior fluxo nesse elevador: {periodo_maior_fluxo}")
print(f"Período mais utilizado no geral: {periodo_mais_usado}")
print(f"Diferença percentual entre o horário mais usado e o menos usado: {diferenca_percentual:.2f}%")
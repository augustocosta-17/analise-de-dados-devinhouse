from calculos import calcular_total, calcular_media, avaliar_consumo
import relatorio

def main():
    consumos = []
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    print("Digite o consumo de água (em litros) para cada dia da semana:")

    for dia in dias:
        while True:
            try:
                valor = float(input(f"Consumo de {dia}: "))
                if valor < 0:
                    print("Valor inválido. Por favor, insira um número não negativo.")
                else:
                    consumos.append(valor)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    total = calcular_total(consumos)
    media = calcular_media(consumos)
    avaliacao = avaliar_consumo(media)

    texto_relatorio = relatorio.gerar_relatorio(total, media, avaliacao)
    print(texto_relatorio)

if __name__ == "__main__":
    main()

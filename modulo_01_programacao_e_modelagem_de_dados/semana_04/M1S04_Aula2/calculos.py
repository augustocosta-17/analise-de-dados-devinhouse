def calcular_total(consumos: list) -> float:
    return sum(consumos)

def calcular_media(consumos: list) -> float:
    if len(consumos) == 0:
        return 0
    return sum(consumos) / len(consumos)

def avaliar_consumo(media: float) -> str:
    media_sustentavel = 150
    if media > media_sustentavel:
        return "Acima da média sustentável"
    elif media < media_sustentavel:
        return "Abaixo da média sustentável"
    else:
        return "Na média sustentável"
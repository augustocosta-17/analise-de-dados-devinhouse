def gerar_relatorio(total: float, media: float, avaliacao: str) -> str:
    relatorio = (
        f"Relatório de consumo de água em litros por dia.\n"
        f"-------------------------------\n"
        f"Total de Consumo: {total:.2f} litros\n"
        f"Média de Consumo: {media:.2f} litros\n"
        f"Avaliação: {avaliacao}\n"
    )
    return relatorio
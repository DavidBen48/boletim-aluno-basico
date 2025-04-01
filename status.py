def status(media: float) -> str:
  if media >= 7:
    return "APROVADO";
  else:
    return "REPROVADO" if media < 6 else "RECUPERAÇÃO"
from status import status;

def mediaDoAluno(notas_do_aluno: list[float]) -> str:
  media = sum(notas_do_aluno) / len(notas_do_aluno)
  print(f"\nMédia do aluno: {media}")
  return f'Status: {status(media)}';

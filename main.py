from mediaDoAluno import mediaDoAluno;
from tabulate import tabulate;

def Main(notas: list[int] = None) -> None:
  if notas == None:
    notas = []
    
  while True:
    n1 = input("Digite a nota do 1º Bimestre: ")
    try:
      n1 = float(n1)
    except ValueError:
      print("\nPor Favor. Digite apenas números")
      continue
      
    n2 = input("Digite a nota do 2º Bimestre: ")
    try:
      n2 = float(n2)
    except ValueError:
      print("\nPor Favor. Digite apenas números")
      continue
      
    n3 = input("Digite a nota do 3º Bimestre: ")
    try:
      n3 = float(n3)
    except ValueError:
      print("\nPor Favor. Digite apenas números")
      continue
      
    n4 = input("Digite a nota do 4º Bimestre: ")
    try:
      n4 = float(n4)
    except ValueError:
      print("\nPor Favor. Digite apenas números")
      continue
    
    if ((n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10) or (n3 < 0 or n3 > 10) or (n4 < 0 or n4 > 10)):
      print("\nUma das notas ficou abaixo de zero ou acima de dez. Por favor, corrija e tente novamente.")
      continue
    
    for nota in [n1, n2, n3, n4]:
      notas.append(nota);
    
    visualizarTodasAsNotas = [
      ["Nota do 1º Bimestre", n1],
      ["Nota do 2º Bimestre", n2],
      ["Nota do 3º Bimestre", n3],
      ["Nota do 4º Bimestre", n4]
    ];
    
    print(f"\n{tabulate(visualizarTodasAsNotas, headers=["Bimestre", "Nota"], tablefmt="grid")}")
    print(mediaDoAluno(notas))
    
    # fim inevitável
    break;
    
if __name__ == "__main__":
  Main()
"""Desafio Aninhado: Você tem a seguinte estrutura de dados aninhada:
alunos = {"programacao": [{"nome": "Lucas", "notas": [9.0, 8.5]}, {"nome":
"Sofia", "notas": [7.0, 9.5]}], "design": [{"nome": "Camila", "notas": [10.0,
8.0]}]}
o Escreva um programa que calcule e imprima a média de notas de
cada aluno, separando por disciplina (programacao e design). A saída deve ser algo 
como: "Média de Adriel (programacao): 8.75"."""

alunos = {
    
    "programacao": [
        {"nome": "Lucas", "notas": [9.0, 8.5]}, 
        {"nome": "Sofia", "notas": [7.0, 9.5]}
        
    ], 
        
    "design": [
        
        {"nome": "Camila", "notas": [10.0, 8.0]}
    ]
}

for curso, inf_alunos in alunos.items():

    """print(curso)
    print(inf_alunos)
    print("\n")"""
    
    for aluno in inf_alunos:

        nt = aluno["notas"]
        nome = aluno["nome"]
        media_aluno = sum(nt) / len(nt)

        print(f"A Média do {nome}({curso}) é {media_aluno:.2f}")

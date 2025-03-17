## Joana é gerente de projetos e precisa consolidar as listas de tarefas de duas equipes distintas. 
## Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário. 
## Sua tarefa é criar um programa que realize essa operação.

## Exemplo de entrada:

# equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
# equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"} 

## Saída esperada:

# Tarefas finais: {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'}

equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

consolidado = set(equipe_a.union(equipe_b))
consolidado.discard(input(f'Qual tarefa deseja remover? ').lower())

print(f'Tarefas finais: {consolidado}')
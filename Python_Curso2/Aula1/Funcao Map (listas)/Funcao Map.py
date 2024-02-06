
# Map Function
    # Muito Utilizado com listas
    # Aplicar uma função a um Iterable, por item. (List, tuple, dic, etc.)


list1 = [1, 2, 3, 4]
def mult(x):
    return x * 2


list2 = map(mult, list1)

print(list(list2))
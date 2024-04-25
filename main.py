# Función para agregar palabras al árbol sin repetirlas
from binary_search_tree import BinarySearchTree


def add_words_to_tree(sentence: str, bst: BinarySearchTree[str]):
    words = sentence.split()
    for word in words:
        bst.insert(word)


# Crear un árbol binario de búsqueda
bst = BinarySearchTree[str]()


def main():
    while True:
        print('Menú de Opciones: \n'
              '1. Ingresar texto.\n'
              '2. Mostrar el arbol. \n'
              '3. Cargar archivo. \n'
              '4. Salir del programa.\n')

        op = int(input('Opción a realizar: '))

        if op == 1:
            try:
                numero = int(input('Ingrese el numero de oraciones a ingresar: '))
                # Pedir al usuario que ingrese una oración
                for i in range(numero):
                    sentence = input("Ingresa una oración: ")
                    # Agregar las palabras al árbol sin repetirlas
                    add_words_to_tree(sentence, bst)
            except ValueError:
                print("Error: Dato incorrecto. Se esperaba un número.\n")

                    # Mostrar el árbol resultante en orden de preorden
        elif op == 2:
            print("Árbol resultante en orden de preorden:")
            print(bst.preorder())
        elif op == 3:
            print('En proceso.')
        elif op == 4:
            break
        else:
            return 'Opción incorrecta.'


if __name__ == '__main__':
    main()

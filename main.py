from random import randint


def attack(char_name, char_class):
    if char_class == 'guerrero':
        return (f'{char_name} causó {5 + randint(3, 5)} de daño al enemigo')
    if char_class == 'mago':
        return (f'{char_name} causó {5 + randint(5, 10)} de daño al enemigo')
    if char_class == 'sanador':
        return (f'{char_name} causó {5 + randint(-3, -1)} de daño al enemigo')
def defense(char_name, char_class):
    if char_class == 'guerrero':
        return (f'{char_name} bloqueó {10 + randint(5, 10)} de daño')
    if char_class == 'mago':
        return (f'{char_name} bloqueó {10 + randint(-2, 2)} de daño')
    if char_class == 'sanador':
        return (f'{char_name} bloqueó {10 + randint(2, 5)} de daño')
def special(char_name, char_class):
    if char_class == 'guerrero': 
        return (f'{char_name} usó una habilidad especial "Aguante {80 + 25}"')
    if char_class == 'mago':
        return (f'{char_name} usó una habilidad especial "Ataque {5 + 40}"')
    if char_class == 'sanador':
        return (f'{char_name} usó una habilidad especial "Defensa {10 + 30}"')




def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, eres un Guerrero, experto en combate cuerpo a cuerpo.')
    if char_class == 'magician':
        print(f'{char_name}, eres un Mago, dominando magistralmente los elementos.')
    if char_class == 'healer':
        print(f'{char_name}, eres un Sanador, un hechicero que cura heridas.')
    print('Entrena tus habilidades.')
    print('Introduce uno de estos comandos: atacar, para atacar un enemigo; defender, para bloquear un ataque enemigo; o especial, para usar tu poder especial.')
    print('Si no quieres entrenar, presiona saltar (skip).')
    cmd = None
    while cmd != 'skip':
        cmd = input('Introduce un comando: ')
        if cmd == 'ataque':
            print(attack(char_name, char_class))
        if cmd == 'defensa':
            print(defense(char_name, char_class))
        if cmd == 'especial':
            print(special(char_name, char_class))
    return 'El entrenamiento ha terminado.'

def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Introduce la clase de tu personajes: Guerrero, guerrero; Mago, mago; Sanador, sanador: ')
        if char_class == 'warrior':
            print('Guerrero: un feroz luchador cuerpo a cuerpo. Fuerte, resiliente y valiente.')
        if char_class == 'magician':
            print('Mago: un brillante luchador de largo alcance. Maestro de poderes mágicos.')
        if char_class == 'healer':
            print('Sanador: un poderoso chamán. Extrae fuerza de la naturaleza, la fe y los espíritus.')
        approve_choice = input('Presiona (Y) para confirmar o cualquier otro botón para seleccionar cualquier otra clase').lower()
    return char_class

def main():
    print('¡Saludos, aventurero!')
    print('Antes de comenzar a jugar...')
    char_name = input('... indica tu nombre: ')
    print(f'¡Bienvenido, {char_name}! '
          'Tienes 80 puntos de aguante, 5 puntos de ataque, y 10 puntos de defensa.')
    print('Puedes elegir una de las tres maneras de la Fuerza:')
    print('Guerrero, Mago, Sanador')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
    

main()

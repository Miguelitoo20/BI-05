import argparse

def main():
    parser = argparse.ArgumentParser(description='Un ejemplo simple de argparse.')
    parser.add_argument('nombre', type=str, help='Nombre de la persona')
    parser.add_argument('--edad', type=int, help='Edad de la persona')
    parser.add_argument('--saludar', action='store_true', help='Saludar a la persona')

    args = parser.parse_args()

    if args.saludar:
        print(f"Hola, {args.nombre}!")
    
    if args.edad:
        print(f"{args.nombre} tiene {args.edad} años.")
    else:
        print(f"No sé la edad de {args.nombre}.")

if __name__ == "__main__":
    main()
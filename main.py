from utils import load_library_items, checkout_items, count_items, find_by_title

def main():
    items = load_library_items("library.csv")  #!agregar la ruta al archivo del library o explota!!!!

    print("=== ITEMS CARGADOS ===")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.__class__.__name__}: {item.title}")

    print("\n=== PRESTAMOS REALIZADOS ===")
    for msg in checkout_items(items, "Tomas"):
        print(msg)

    print("\n=== CANTIDAD DE ITEMS POR TIPO ===")
    print(count_items(items))

    print("\n=== BUSQUEDA DE 'Python' ===")
    for item in find_by_title(items, "python"):
        print(f"- {item.title} ({item.__class__.__name__})")

if __name__ == "__main__":
    main()

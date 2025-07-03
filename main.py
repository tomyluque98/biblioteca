from utils import load_library_items, checkout_items, count_items, find_by_title

def main():
    items = load_library_items("library.csv")

    print("=== ÍTEMS CARGADOS ===")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.__class__.__name__}: {item.title}")

    print("\n=== CHECKOUT ===")
    for msg in checkout_items(items, "Juan"):
        print(msg)

    print("\n=== CONTEO ===")
    print(count_items(items))

    print("\n=== BÚSQUEDA DE 'Python' ===")
    for item in find_by_title(items, "python"):
        print(f"- {item.title} ({item.__class__.__name__})")

if __name__ == "__main__":
    main()

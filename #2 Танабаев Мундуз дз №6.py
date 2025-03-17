import os

def add_data(data_list):
    while True:
        item = input("Введите элемент списка (или 'стоп' для завершения): ").strip()
        if item.lower() == 'стоп':
            break
        data_list.append(item)

def show_data(data_list):
    print("\nВаш список данных:")
    for i, item in enumerate(data_list, start=1):
        print(f"{i}. {item}")

def main():
    data_list = []
    add_data(data_list)
    show_data(data_list)

if __name__ == "__main__":
    main()

from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime


class Product(object):
    def __init__(self, prod_date, prod_name, prod_category, prod_count, prod_price):
        self.prod_date = prod_date
        self.prod_category = prod_category
        self.prod_name = prod_name
        self.prod_count = prod_count
        self.prod_price = prod_price


class Main(object):
    def __init__(self, total):
        self.total = total


def add_new_product():
    try:
        int(price_entry.get())
        int(count_entry.get())
    except ValueError:
        try:
            float(price_entry.get())
            float(count_entry.get())
        except ValueError:
            messagebox.showinfo("Wallet", "Цена или кол-во не цифра")

    product = Product(strftime("%Y-%m-%d %H:%M:%S", gmtime()), surname_entry.get(), name_entry.get(),
                      int(count_entry.get()), int(price_entry.get()))
    length = len(main.total) + 1
    main.total[length] = product
    messagebox.showinfo("Wallet", "Товар добавлен")
    clear_all_inputs()


def save_file():
    file = open('text.txt', 'w')
    file.write('a')
    file.close()
    messagebox.showinfo("Wallet", "Файл сохранен")


def clear_all_inputs():
    surname_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    count_entry.delete(0, 'end')
    price_entry.delete(0, 'end')


root = Tk()
root.title("Wallet")

main = Main({})
name = StringVar()
surname = StringVar()
count = StringVar()
price = StringVar()

name_label = Label(text="Введите название товара:")
surname_label = Label(text="Введите категорию:")
count_label = Label(text="Введите кол-во:")
price_label = Label(text="Введите стоимость:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
count_label.grid(row=2, column=0, sticky="w")
price_label.grid(row=3, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
count_entry = Entry(textvariable=count)
price_entry = Entry(textvariable=price)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
count_entry.grid(row=2, column=1, padx=5, pady=5)
price_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = Button(text="Добавить", command=add_new_product)
add_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

save_button = Button(text="Сохранить в файл", command=save_file)
save_button.grid(row=4, column=4, padx=5, pady=5, sticky="w")

root.mainloop()

# TODO Найдите количество книг, которое можно разместить на дискете
floppy_size = 1.44
pages = 100
strings = 50
symbols = 25
symbol_size = 4

floppy_size_bytes = floppy_size * 1024 ** 2
book_size = pages * strings * symbols * symbol_size

books = floppy_size_bytes // book_size

print("Количество книг, помещающихся на дискету:", int(books))

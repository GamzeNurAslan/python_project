list_methods = []
for method in dir(list):
    if method.startswith("__"):
        continue
    list_methods.append(method)


set_methods = []
for method in dir(set):
    if method.startswith("__"):
        continue
    set_methods.append(method)


string_methods = []
for method in dir(str): #string methodunun sınıfı str dir.
    if method.startswith("__"):
        continue
    string_methods.append(method)


tuple_methods = []
for method in dir(tuple):
    if method.startswith("__"):
        continue
    tuple_methods.append(method)


dict_methods = []
for method in dir(dict):
    if method.startswith("__"):
        continue
    dict_methods.append(method)


basliklar = ["list_methods", "set_methods", "string_methods", "tuple_methods", "dict_methods"]
classes = [list_methods, set_methods, string_methods, tuple_methods, dict_methods]

max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)

with open("Methods.txt", "w") as f:
     for baslik in basliklar:
         print(baslik,end="")
         print(" " * (30 - len(baslik)),end="")
         f.write(baslik)
         f.write(" " * (30 - len(baslik)))
     for i in range(max_len):
         print()
         f.write("\n")
         for class_ in classes:
             if i >= len(class_):
                print("-------", end="")
                print(" " * 23, end="")
                f.write("-------")
                f.write(" " * 23)
             else:
                print(class_[i], end="")
                print(" " * (30 - len(class_[i])), end="")
                f.write(class_[i])

                f.write(" " * (30 - len(class_[i])))

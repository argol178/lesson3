with open("referat.txt", "r", encoding = "utf-8") as ref:
    content = ref.read()
    print("Длина строки {}".format(len(content)))
    print("Количество слов в тексте равно {}".format(len(content.split())))
    ref_repl = content.replace(".","!")

with open("referat_2.txt", "w", encoding = "utf-8") as ref_2:
    ref_2 = ref_2.write(ref_repl)

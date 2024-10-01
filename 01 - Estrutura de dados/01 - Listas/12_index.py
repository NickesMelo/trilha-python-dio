linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0


def funcao(*args, **kw):
    funcao("python", 2022, curso="dio")
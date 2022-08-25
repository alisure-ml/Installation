"""
用于检查英语语法时移除引用和符号，需一段一段来。
"""

while True:
    s = input()

    arr = s.split("\cite{")
    result = [arr[0].strip()]
    for one in arr[1:]:
        a = one.split("}", 1)[1].strip()
        result.append(a)
        pass
    result = "".join(result)
    print()
    print()
    print(result)
    print()
    print()
    while "$" in result:
        arr = result.split("$", 1)
        result = arr[0] + "m" + arr[1].split("$", 1)[1]
    print(result)
    print()
    print()

    pass

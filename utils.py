def read_req():
    with open("requirements.txt", "r", encoding="utf16") as f:
        a = f.read()
        return a


print(read_req())



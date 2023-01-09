def read_req():
    with open("requirements.txt", "r", encoding="utf16") as f:
        data = f.readlines()
        string = "<br>"
        data_ready = [x + string for x in data]

    return " ".join(data_ready)

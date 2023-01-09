with open("hw.csv", "r") as file:
    data = file.readlines()

del data[:1], data[-1:]
dict_data = dict(map(lambda x: (float("".join(x.split(",")[1:-1])), float("".join(x.split(",")[-1:]))), data))


def weight():
    avr_weight = round((sum(dict_data.values()) / len(dict_data)) * 0.453592)
    return avr_weight


def height():
    avr_height = round((sum(dict_data.keys()) / len(dict_data)) * 2.54)
    return avr_height

# weight = round((sum(dict_data.values()) / len(dict_data)) * 0.453592) #Рішення без використання функцій
# height = round((sum(dict_data.keys()) / len(dict_data)) * 2.54)


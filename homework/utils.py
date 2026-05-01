def lectura_datos():
    with open("files/input/data.csv", "r") as file:
        data=file.readlines()
    return data
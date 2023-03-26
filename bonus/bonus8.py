def get_average():
    with open("../files/data.txt", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    local_average = sum(values) / len(values)
    return local_average


average = get_average()
print(average)

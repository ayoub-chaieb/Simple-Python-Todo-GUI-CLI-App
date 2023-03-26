contents = ["The true meaning of",
            "obscurity lies underneath the most delicate structures of viscosity",
            "The idea of changing that balance is obscure by itself"]

files = ["../files/doc.txt", "../files/report.txt", "../files/log.txt"]

for c, f in zip(contents, files):
    file = open(f"files/{f}", 'w')
    file.write(c)

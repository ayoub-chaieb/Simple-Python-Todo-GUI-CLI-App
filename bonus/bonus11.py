from bonus.converters11 import convert
from bonus.parsers11 import parse

feet_inches = input("Enter feet and inches :")

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} meter")


if result < 1:
    print("Kid so small")
else:
    print("Kid can use the slide")
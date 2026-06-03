# reminder - here is an integer than has been multiplied by 3
number = 5
print(number * 3)

# here is a string that has been multiplied by 3
# (note the speech marks and text colour)
num_string = "5"
print(num_string * 3)

# An example showing what the len(foo) method does
example_text = "hello world"
text_length = len(example_text)

print(f"'{example_text}' is {text_length} characters long")

# list exploration / experiment

fruit_list = ['apple', 'banana', 'cherry', 'dragon fruit']

for item in fruit_list:

    print()

    # print the whole word...
    print("Fruit Name: ", item)

    # print the first letter...
    print("First letter", item[0])

    # challenge = print the first TWO letters
    print(f"First two letters {item[:2]}")

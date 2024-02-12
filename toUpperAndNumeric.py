def to_uppercase(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        text_uppercase = text.upper()

    with open(output_file, 'w') as file:
        file.write(text_uppercase)


def replace_numbers_with_words(input_file, output_file):
    digit_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    with open(input_file, 'r') as file:
        text = file.read()

    for digit, word in digit_words.items():
        text = text.replace(digit, word)

    with open(output_file, 'w') as file:
        file.write(text)


input_file = "sample.txt"
output_file1 = "Sample_Upper.txt"
output_file2 = "Sample_numeric.txt"
to_uppercase(input_file, output_file1)
replace_numbers_with_words(input_file,output_file2)
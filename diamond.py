import string


def print_diamond(input_letter):
    if input_letter == "A":
        return "A"
    output = ["A"]
    for i, letter in enumerate(string.ascii_uppercase[1:]):
        output = [" " + line+ " " for line in output]
        output.append(letter+ (2*i + 1)*" " + letter)
        if letter == input_letter:
            output.extend(output[-2::-1])
            return "\n".join(output)
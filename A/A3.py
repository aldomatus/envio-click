def vowel_counter(my_string):
    counter = 0
    for letter in my_string:
        if letter in 'aeiouAEIOU':
            counter += 1
    return counter


def change_vowels(my_string):
    new_string = ''
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for letter in my_string:
        if letter in vowels:
            index = 0
            for vowel in vowels:
                if vowel == letter:
                    break
                index += 1
            new_string += vowels[index + 1]

        else:
            new_string += letter
    return new_string


if __name__ == '__main__':
    my_string = input("Enter your string: ")
    print(f'Your string has {vowel_counter(my_string)} vowels')

    my_new_string = (change_vowels(my_string))
    print(f'Your changed string: {my_new_string}')

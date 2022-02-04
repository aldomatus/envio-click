from data import dictionary, dictionary_of_levels

def show(dictionary):
    for key in dictionary.keys():
        dictionary[key]['Level'] = dictionary_of_levels[dictionary[key]['Level']]
        dictionary[key]['name']

    print(dictionary)
            

if __name__ == '__main__':
    show(dictionary)
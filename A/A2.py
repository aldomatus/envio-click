from data import dictionary, dictionary_of_levels, dictionary_of_levels2
import ast

def show(dictionary):
    sort_names = {}
    names_first_layer = []
    names_second_layer = []
    names_third_layer = []
    
    for key in dictionary.keys():
        for number_layer_1 in range(len(dictionary)):
            if number_layer_1+1 == dictionary_of_levels.get(dictionary[key]['Level'], 0) and type(dictionary[key]['Level']) != int:
                dictionary[key]['Level'] = number_layer_1+1
                names_first_layer.append(dictionary[key]['name'])
                sort_names[1] = names_first_layer


        subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary[key].values())

        for key2 in dictionary[key].keys():
            if type(dictionary[key][key2]) == dict:
                #print('name: ', dictionary[key][key2]['name'])
                for number_layer_2 in range(subdata_number):
                    if number_layer_2+1 == dictionary_of_levels.get(dictionary[key][key2]['Level'], 0) and type(dictionary[key][key2]['Level']) != int:
                        dictionary[key][key2]['Level'] = number_layer_2+1
                        names_second_layer.append(dictionary[key][key2]['name'])
                        sort_names[2] = names_second_layer

        subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary[key].values())

        for key3 in dictionary[key][key2].keys():
            if type(dictionary[key][key2][key3]) == dict:
                #print('name: ', dictionary[key][key2][key3]['name'])
                for number_layer_3 in range(subdata_number):
                    if number_layer_3+1 == dictionary_of_levels.get(dictionary[key][key2][key3]['Level'], 0) and type(dictionary[key][key2][key3]['Level']) != int:
                        dictionary[key][key2][key3]['Level'] = number_layer_3+1
                        names_third_layer.append(dictionary[key][key2][key3]['name'])
                        sort_names[3] = names_third_layer
    f = open("/home/aldo/Documents/envio_click/A/A2_1.txt","w+")
    f2 = open("/home/aldo/Documents/envio_click/A/A2_2.txt","w+")
    f.write(str(sort_names))
    f2.write(str(dictionary))
    f.close()
    f2.close()

    counter = 1
    for sort_name in sort_names.values():
        for name in sort_name:
            print("\t"*counter + str(name))
        print('\n')
        counter+=2


def addData(levels, name):
    f = open("A2_1.txt","w+")
    with open('/home/aldo/Documents/envio_click/A/A2_2.txt', 'r+') as dictionary:
        contents = dictionary.read()
        dictionary = ast.literal_eval(contents)

    # for level in levels:
    #     for 


    
if __name__ == '__main__':
    show(dictionary)
    # levels = []
    # last_level = int(input("Enter your last level: "))
    # for level_number in range(last_level):
    #     level_num = int(input(f"Enter your category of level{level_number}: (example: enter 1 to select DataA or enter 2 to select DataB): "))
    #     levels.append(level_num)

    
    # name = str(input("Enter your name: "))
    # addData(levels, name)
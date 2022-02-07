from data import dictionary, dictionary_of_levels
import ast

def show2(dictionary):
    for key in dictionary.keys():
        ak = '[key]' 
        k = '[key]'
        counter = 1
        for number_layer_1 in range(len(dictionary)):
            if number_layer_1+1 == dictionary_of_levels.get(dictionary[key]['Level'], 0) and type(dictionary[key]['Level']) != int:
                dictionary[key]['Level'] = number_layer_1+1
                print('\t'*counter + str(dictionary[key]['name']))

        for num in range(2,10):
            subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary[key].values())
            counter+=1
            if num >= 2:
                ak += f'[key{num}]'
            if num > 2:
                k += f'[key{num-1}]'
            # for key2 in dictionary[key].keys():
            code = f"""for key{num} in dictionary{k}.keys():
                            if type(dictionary{ak}) == dict:
                                print('\t'*counter + str(dictionary{ak}['name']))
                                for number_layer_2 in range({subdata_number}):
                                    if number_layer_2+1 == dictionary_of_levels.get(dictionary{ak}['Level'], 0) and type(dictionary{ak}['Level']) != int:
                                        dictionary{ak}['Level'] = number_layer_2+1
                        """
            try:            
                exec(code)
            except Exception as e:
                break


    f = open("/home/aldo/Documents/envio_click/A/A2_1.txt","w+")
    f2 = open("/home/aldo/Documents/envio_click/A/A2_2.txt","w+")
    f2.write(str(dictionary))
    f.close()
    f2.close()


def addData(levels, name):
    f = open("A2_1.txt","w+")
    with open('/home/aldo/Documents/envio_click/A/A2_2.txt', 'r+') as dictionary:
        contents = dictionary.read()
        dictionary = ast.literal_eval(contents)

    
if __name__ == '__main__':
    show2(dictionary)
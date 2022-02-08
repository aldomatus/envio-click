from data import dictionary3, dictionary_of_levels
import ast

def show2(dictionary):
    for key in dictionary.keys():
        print(key)
        ak = '[key]' 
        k = '[key]'
        counter = 1
        for number_layer_1 in range(len(dictionary)):
            print()
            
            if number_layer_1+1 == dictionary_of_levels.get(dictionary[key]['Level'], 0) and type(dictionary[key]['Level']) != int:
                dictionary[key]['Level'] = number_layer_1+1
                print('\t'*counter + str(dictionary[key]['name']))
            elif dictionary[key].get('Level', 0) == number_layer_1 + 1:
                print('\t'*counter + str(dictionary[key]['name']))


        for num in range(2,10):
            subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary[key].values())
            counter+=1
            if num >= 2:
                ak += f'[key{num}]'
            if num > 2:
                k += f'[key{num-1}]'

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


def addData(key_name, value, route):
    f = open("A2_1.txt", "w+")
    with open('/home/aldo/Documents/envio_click/A/A2_2.txt', 'r+') as dictionary_read:
        contents = dictionary_read.read()
        dictionary_read = ast.literal_eval(contents)
        route_length = len(route)

        dictionary = dictionary3

        key_counter = 1
        for key in dictionary.keys():
            ak = '[key]' 
            k = '[key]'
            save_route = str(f'dictionary[{key}]')
            counter = 1
            for number_layer_1 in range(0, len(dictionary)-1):
                if dictionary[key].get('Level', 0) == route[number_layer_1] if number_layer_1 < len(route) else -1 and route_length == 1:
                    if route_length == 1:
                        dictionary[key][key_name] = value

            for num in range(route_length):
                
                counter+=1
                if num+1 >= 2:
                    ak += f'[key{num}]'
                if num+1 > 2:
                    k += f'[key{num-1}]'

                code = f"""for key{num} in dictionary{k}.keys():
                            subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary{k}.values())
                            if type(dictionary{ak}) == dict:

                                for number_layer_2 in range(subdata_number):
                                    print('number_layer_2', number_layer_2)
                                    if route[number_layer_2] == dictionary{ak}['Level'] and key_counter == number_layer_2:
                                        save_route += str(f'[{{key{num}}}]')
                                        print(save_route)
                                        # dictionary{ak}['{key_name}'] = '{value}'
                                        route[number_layer_2] = 0
                                        break
                            """
                try:  
                    print('\n\n\n\n')          
                    exec(code)
                except Exception as e:
                    print(e)
                    break
            key_counter += 1
        print(dictionary)
        print('Sending show2')
        show2(dictionary)

    
    
if __name__ == '__main__':
    show2(dictionary3)
    key = str(input("Enter your key name: "))
    value = str(input("Enter your value: "))
    level = int(input("Enter your level: "))
    route = []

    print('\nEnter your route: ')
    for num in range(1,level+1):
        number_of_layer = int(input(f"Enter the number of layer[{num}]:"))
        route.append(number_of_layer)
    addData(key, value, route)

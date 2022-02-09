from data import dictionary_of_levels, print_menu
import ast
import os

def show(function):
    with open(f'{os.getcwd()}/A/A2_2.txt', 'r+') as dictionary_read:
        contents = dictionary_read.read()
        dictionary = ast.literal_eval(contents)
    print("""\n█████ █████ █████ █████ █████ █████ █████""")
    for key in dictionary.keys():
        print(key)
        ak = '[key]' 
        k = '[key]'
        counter = 1

        for number_layer_1 in range(len(dictionary)):
            
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

    if function == 'main':
        f = open(f'{os.getcwd()}/A/A2_2.txt', "w")
        f.write(str(dictionary))
        f.close()
        dictionary_read.close()
    else:
        dictionary_read.close()
    print("""█████ █████ █████ █████ █████ █████ █████ \n""")
    input("\n\nPress enter to continue operations...")


def addData(key_name, value, route):
    with open(f'{os.getcwd()}/A/A2_2.txt', 'r+') as dictionary_read:
        contents = dictionary_read.read()
        dictionary = ast.literal_eval(contents)
        route_length = len(route)

        key_counter = 0
        save_route = str(f'dictionary')
        for key in dictionary.keys():
            ak = '[key]' 
            k = '[key]'

            break_out_flag_route_1 = False
            pass_flag_key_not_found = False
            break_out_flag_key1 = False
            break_out_flag_route_nested = False

            if dictionary[key].get('Level', 0) == route[0]:
                if route_length == 1:
                    dictionary[key][key_name] = value
                    break_out_flag_route_1 = True
                else:
                    break_out_flag_key1 = True
                    save_route += str(f'["{key}"]')
            else:
                pass_flag_key_not_found = True

            if break_out_flag_route_1 == True:
                break
            if pass_flag_key_not_found == True:
                continue


            for num in range(1, route_length):
                
                if num+1 >= 2:
                    ak += f'[key{num}]'
                if num+1 > 2:
                    k += f'[key{num-1}]'
                names = []
                code = f"""for key{num} in dictionary{k}.keys():
                            subdata_number = sum(1 if type(x) == dict else 0 for x in dictionary{k}.values())
                            if type(dictionary{ak}) == dict:
                                if route[{num}] == dictionary{ak}['Level']:
                                    names.append(str(f'["{{key{num}}}"]'))
                                    break  
                            else:
                                 break_out_flag_route_nested = True                                     
                            """
                try:           
                    exec(code)
                    for i in names:
                        save_route += i
                except Exception as e:
                    print(e)
                    break
                if break_out_flag_route_nested:
                    continue

            key_counter += 1
            if break_out_flag_key1 == True:
                break
        addData1 = f'{save_route}["name"] = "{value}"'
        exec(addData1)
        f = open(f'{os.getcwd()}/A/A2_2.txt', "w")
        f.write(str(dictionary))
        f.close()
        dictionary_read.close()
        print('Sending show2')
        show('addData')

    
if __name__ == '__main__':
    while True:
        option = print_menu()

        if option == 1:
            show('main')    
        elif option == 2:
            show('main')
            key = str(input("\nEnter your key name: "))
            value = str(input("Enter your value: "))
            level = int(input("Enter your level: "))
            route = []

            print('\nEnter your route: ')
            for num in range(1,level+1):
                number_of_layer = int(input(f"Enter the number of layer[{num}]:"))
                route.append(number_of_layer)
            addData(key, value, route)

        elif option == 3:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
        os.system ("clear")


import os
dictionary3 = {
    "DataA": {
                "name": "One nameA",
                "Level": "One",
                "Priority": "Highest",

                "SubdataA": {
                            "name": "One nameSubdataA",
                            "Level": "One",
                            "Priority": "Highest",
                            },

                "SubdataA2": {
                            "name": "One nameSubdataA2",
                            "Level": "Two",
                            "Priority": "High",
                            "SubdataAA": {
                                        "name": "One nameSubdataAA",
                                        "Level": "One",
                                        "Priority": "Highest",
                                        
                                        "SubdataAAA": {
                                                        "name": "One nameSubdataAAA",
                                                        "Level": "One",
                                                        "Priority": "Highest",
                                                        
                                                     }
                                        }
                             }
    },

    "DataB": {
            "name": "One nameB",
            "Level": "Two",
            "Priority": "Highest",
            "SubdataB":
                    {
                        "name": "One nameSubdataB",
                        "Level": "One",
                        "Priority": "Highest",
                    }
        },

    "DataC": {
            "name": "One nameC",
            "Level": "Three",
            "Priority": "Highest",
            "SubdataC":
                    {
                        "name": "One nameSubdataC",
                        "Level": "One",
                        "Priority": "Highest",
                    }
        }
}

dictionary2 = {
        "DataA": {
                "name": "One nameA", 
                "Level": 1, 
                "Priority": "Highest", 
                
                "SubdataA": {"name": "One nameSubdataA", 
                             "Level": 1, 
                             "Priority": "Highest"
                            }, 
                
                "SubdataA2": {"name": "One nameSubdataA2", 
                              "Level": 2, 
                              "Priority": "High", 
                              
                              "SubdataAA": {
                                            "name": "One nameSubdataAA", 
                                            "Level": 1, 
                                            "Priority": "Highest"
                                            }
                             }
                }, 
        "DataB": {
                "name": "One nameB", 
                "Level": 2, 
                "Priority": "Highest", 
                
                "SubdataB": {"name": "One nameSubdataB", 
                             "Level": 1, 
                             "Priority": "Highest"
                             }
                }
              }

dictionary_of_levels = {
        "Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8,
        "Nine": 9, "Ten": 10, "Eleven": 11, "Twelve": 12, "Thirteen": 13, "Fourteen": 14, "Fifteen": 15,
        "Sixteen": 16, "Seventeen": 17, "Eighteen": 18, "Nineteen": 19,
      }


dictionary_of_levels2 = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 
        14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
                        }


dictionary_of_priority = {
        "Lowest": 0, "Low": 1, "Medium": 2, "High": 3, "Highest": 4,
      }


menu_options = {
    1: 'Show dictionary',
    2: 'Add a name',
    3: 'Exit',
}

def print_menu():

    print("""__________             _____      __________________      ______  
___  ____/_________   ____(_)_______  ____/__  /__(_)________  /__
__  __/  __  __ \_ | / /_  /_  __ \  /    __  /__  /_  ___/_  //_/
_  /___  _  / / /_ |/ /_  / / /_/ / /___  _  / _  / / /__ _  ,<   
/_____/  /_/ /_/_____/ /_/  \____/\____/  /_/  /_/  \___/ /_/|_|                       
\n""")
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

    while(True):
        option = ''
        try:
            option = int(input('Enter your choice: '))
            print('\n')
        except:
            print('Wrong input. Please enter a number ...')
        return option
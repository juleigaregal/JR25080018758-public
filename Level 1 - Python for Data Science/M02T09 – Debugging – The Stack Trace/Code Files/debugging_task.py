# Function to print dictionary values given the keys

records = []
def print_values_of(dictionary, *keys): #changed key to *keys in order to input multiple keys
    for key in keys:
        print(dictionary[key])          #fixed k to key
        
        
        

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": 'd''oh!',  # had missing qoutations mark
                         "maggie": "(Pacifier Suck)"
                         }
# now with the *keys change on line 4, can pass multiple arguments
print_values_of(simpson_catch_phrases,'lisa', 'bart', 'homer')


'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

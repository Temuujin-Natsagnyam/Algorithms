#    A simple linear search algorithm
#   Temuujin Natsagnyam  19/05/2018
#--------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------Variables_Declarations------------------------------------------------------
__alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

#-----------------------------------------------------Procedures-----------------------------------------------------------------
def remove_leading_spaces(string_input):
    for x in range(len(string_input)):
        if string_input[x].isspace() is False:
            string_input = string_input[x:]
            break
    return string_input

def remove_trailing_spaces(string_input):
        for x in range(len(string_input)-1, -1, -1):
            if string_input[x].isspace() is False:
                string_input = string_input[:x+1]
                break
        return string_input
 
def linear_search(target, a_list):
    target = remove_leading_spaces(remove_trailing_spaces(target))
    for x in range(len(a_list)):
        if a_list[x] == target:
            return x
    return False    
#----------------------------------------------------User_Interface------------------------------------------------------------
while True:
    user_input = str(input("\nEnter letter to be (linear) searched for in alphabet \n\n\t>>")).lower()
    search_result = linear_search(user_input, __alphabet) 
    if  search_result is False:
        print("\nError! Please enter single item to be searched which is within list\n")
    else:
        print("\nFound at position "+ str(search_result) + ". \n")
    
    
    

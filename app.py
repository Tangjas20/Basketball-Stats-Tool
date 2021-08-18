from constants import TEAMS
from constants import PLAYERS


def change_height():        #Changes the string to int values
    teams_to_clean = TEAMS      #Initialises the constant data that will be used
    players_to_clean = PLAYERS      #Assigning variables makes sure that the original data is not modified

    for x in range(0, len(players_to_clean)):   #For loop to iterate through entire list-nested dictionary
            str_height = players_to_clean[x]["height"] 
            str_height_cut = str_height[0:2]    #Takes the first 2 values of the string
            int_height = int(str_height_cut)    #Coverts string into int
            players_to_clean[x]["height"] = int_height      #The int is assigned back into the dictionary

    return players_to_clean

def change_experience(): #Changes the YEs and NO to boolean values
        players_to_clean = change_height()      #Recursion principle is used here to keep the now changed dictionary

        for x in range(0, len(players_to_clean)):       #Similar to above
            str_experience = players_to_clean[x]["experience"]
            if str_experience.lower() == 'yes':     #If the YES or yes string is given, then the dictionary entry is changed to True
                players_to_clean[x]["experience"] = True
            elif str_experience.lower() == 'no':        #Likewise, changed to False
                players_to_clean[x]["experience"] = False
            else:
                str_experience = ""     #Nothing happens if there is no YES or NO

        return players_to_clean     #Returns value to be used as a recursive step for the next function

def players_list_creator():    #This returns a list which contains all of the players
    players_to_clean = change_experience()   #Calls on the previous function for data
    players_list = []    #Empty list

    for x in range(0, len(players_to_clean)): #Iterates through the listed dictionaries
        name = players_to_clean[x]['name']  #Takes the value of 'name' in the dictionary
        players_list.append(name)   #Adds it to the empty list

    return players_list 

def balance_teams(): #Assigns 1/3 of the players to each team
    team_1 = TEAMS[0] #This assigns the team name to team_1 which will be called upon later
    team_1_list = [] #Empty list for the team players

    team_2 = TEAMS[1]
    team_2_list = []

    team_3 = TEAMS[2]
    team_3_list = []

    players_list = players_list_creator() #Calls the previous function for the players list
    players_list_indexer = 0 #This will be used to iterate through the list
    
    players_per_team = len(PLAYERS)/3  #Sets the max amount of players per team
    while players_list_indexer <= len(PLAYERS)-1:
        player = players_list[players_list_indexer]
        if len(team_1_list) < players_per_team: #If number of players less than max, adds another
            team_1_list.append(player)
            players_list_indexer += 1 #Indexer moves to track players in list
        
        elif len(team_2_list) < players_per_team:
            team_2_list.append(player)
            players_list_indexer += 1

        elif len(team_3_list) < players_per_team:
            team_3_list.append(player)
            players_list_indexer += 1
    
    return team_1_list, team_2_list, team_3_list #Function returns the players in each team as 3 separate tuples


def team_stats(n):
    player_list_string = "" #Initialise string to use to add team players
    if n == 'a': #When a parameter value is given, these sets of conditions apply
        a = 0
        len_team = len(team_1_list)
        which_team = TEAMS[0]
        for players in team_1_list: #Adds players in the list to the string
            player_list_string += players + ", "

        player_list_string = player_list_string[:-2] #Removes the last ', ' from the list
        user_input_2_valid = True #Stops the loop in the main function

    elif n == 'b':
        a = 1
        len_team = len(team_2_list)
        which_team = TEAMS[1]
        for players in team_2_list:
            player_list_string += players + ", "
        player_list_string = player_list_string[:-2]
        user_input_2_valid = True

    elif n == 'c':
        a = 1
        len_team = len(team_3_list)
        which_team = TEAMS[2]
        for players in team_3_list:
            player_list_string += players + ", "
        player_list_string = player_list_string[:-2]
        user_input_2_valid = True
    
    else: #Catches exceptions/corner cases
        print("Invalid please try again")

    print("Team: {} Stats".format(which_team)) #prints out team stats
    print("--------------------")
    print("Total players: {}\n".format(len_team))
    print("Players on team: ")
    print("  " + player_list_string)

if __name__ == '__main__':
    team_1_list, team_2_list, team_3_list = balance_teams() #assigns tuples to each variable
    user_input_valid = False #Looping variable for the while loop

    print("#######################################")
    print("Welcome to Basketball Team Stats Tool!")
    print("#######################################\n\n")

    while user_input_valid == False: #This doesnt have to be set to True since the program
#                                       Exits with the Exit() function
        print("---- MENU ----")
        print("Here are your choices:")
        print("  A) Display Team Stats")
        print("  B) Quit\n\n")
        user_input_1 = input("Enter an option: ") #Takes user input

        if user_input_1.lower() == 'a':
            user_input_2_valid = False

            while user_input_2_valid == False:
                print("  A) Panthers")
                print("  B) Bandits")
                print("  C) Warriors")
                print("  D) Quit")

                userInput_2 = input("Enter an option: ")
                print("")
                if len(userInput_2) < 1: #Catches exceptions where there is no input
                    print("Please input correct commands!\n")

                elif userInput_2 == 'd': #Adds a new funtionality where people can quit on the 2nd page
                    exit("Shutting down as requested...")

                else:  
                    try:
                        team_stats(userInput_2.lower()) #Calls upon the team stats function
                        print("\n")
                    except: #Exceptions are caught and the loop continues
                        print("Please try again!\n\n")

        elif user_input_1.lower() == 'b': #Quits if the 1st page of the menu is answered with B
            exit("Shutting down as requested...\n")

        else: #If the user doesn't input a or b, then it is invalid and will loop
            print("Please input correct commands!\n\n")


        



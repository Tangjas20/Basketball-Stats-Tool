#Hi! Thanks for looking at my code. Please let me know if there are any things that I can improve on.
#I try to keep every line I write have purpose, so I will comment a lot of it

from constants import TEAMS  #Imports data file
from constants import PLAYERS 
import copy

def change_height(): #This will take the first 2 indexes of the string and change it to int. Its limitations are that if the height is over 99 inches. It won't work very well..
    for x in range(0, len(players_dictionary_list)): #Iterates through the list
        str_height = players_dictionary_list[x]['height'] #Stored as a variable for indexing/operations
        str_height_cut = str_height[0:2] #First 2 indexes taken
        int_height = int(str_height_cut) #Convert to int, exception handling isn't required unless the datafile is wrong
        players_dictionary_list[x]["height"] = int_height #Adds value back to dictionary


def height_list(): #This creates a dictionary which encompasses the player name as the key, and height (int) as value
    player_height_list = [] #Initiate list 1 for dictionary, this is used as the values
    player_list = [] #List 2 for keys
    for x in range(0, len(players_dictionary_list)): #Iterates
        player_height_list.append(players_dictionary_list[x]["height"]) #Appends all heights in datafile into list 1
        player_list.append(players_dictionary_list[x]['name']) #Appends all names into list 2
    zip_iterator = zip(player_list, player_height_list) #Zips into a tuple
    player_height_dict = dict(zip_iterator) #Creates a dictionary

    return player_height_dict #This will be called upon for later use


def change_experience(): #Changes experience into boolean
    for x in range(0, len(players_dictionary_list)):
        str_experience = players_dictionary_list[x]["experience"] #Assigns variable to indexed item
        if str_experience.lower() == 'yes': 
            players_dictionary_list[x]["experience"] = True #If yes or YES, then changes to True
        elif str_experience.lower() == 'no':
            players_dictionary_list[x]["experience"] = False #Same as above, but False


def experience_list_by_name(): #Creates two lists separating the experienced and non-experienced players
    true_experience_list = []
    false_experience_list = []
    for x in range(0, len(players_dictionary_list)):
        if players_dictionary_list[x]['experience'] == True:
            true_experience_list.append(players_dictionary_list[x]['name']) #if experienced, append to true_exp list
        elif players_dictionary_list[x]['experience'] == False:
            false_experience_list.append(players_dictionary_list[x]['name']) #Converse of above

    return true_experience_list, false_experience_list #Will be called upon later


def change_guardian_to_string(): #This function splits the guardian item into a list and then string, then returns a dictionary of name:guardian 
    guardians_list = [] #Initialise two lists for dictionary creation
    player_list = []

    for x in range(0, len(players_dictionary_list)):
        guardian_string = '' #Initialise string to replace the guardian item
        str_guardian = players_dictionary_list[x]["guardians"]

        if " and " in str_guardian:       #Looks for ' and ' in the dictionary entry
            str_guardian = str_guardian.split(" and ")

            for i in str_guardian: 
                guardian_string += i + ", " #When it is split, it is a list with 2+ items. To make it into a string I need to iterate through it
            guardian_string = guardian_string[:-2] #Removes the last two indexes which is junk
            players_dictionary_list[x]["guardians"] = guardian_string #Replaces the old guardian item
            guardians_list.append(players_dictionary_list[x]["guardians"]) #Adds to the guardian_list for creating a new name:guardian dictionary

        else:
            guardians_list.append(players_dictionary_list[x]['guardians']) #If there is no and, the name is simply added to the guardian_list

        player_list.append(players_dictionary_list[x]['name']) #Adds name to the player_list for dictionary creation

    zip_iterator = zip(player_list, guardians_list) #Combines two values into a tuple
    player_guardian_dict = dict(zip_iterator) #Creates dictionary from the tuple

    return player_guardian_dict #Will be called upon in team_stats


def guardian_per_team(n): #This will separate the previously made guardian dictionary into the respective teams. 
    guardian_string_per_team = "" #Initialise string for guardian
    guardian_dict = change_guardian_to_string() #Calls upon the previous function
    team_1_players, team_2_players, team_3_players, team_1_experienced, team_2_experienced, team_3_experienced = balance_team() #Calls another function for values

    if n == 'a': #If the parameter given is a/b/c assigns value to be passed into the guardian dictionary
        team = team_1_players
    elif n == 'b':
        team = team_2_players
    elif n == "c":
        team = team_3_players
    else:
        pass
    
    for x in team:
        guardian_string_per_team += guardian_dict[x] + ", "
    guardian_string_per_team = guardian_string_per_team[:-2] #For each person in the team, their guardian is added to the string

    return guardian_string_per_team #Value called upon later


def balance_team(): #This will take all the experienced/non-experienced players and organise them into equally fair teams.
    true_list_indexer = 0 #Initialising indexers for loops
    false_list_indexer = 0
    loop_indexer = 0 
    true_list, false_list = experience_list_by_name() #Calls previous function for values
    player_number_team = len(PLAYERS) / len(TEAMS) #number of players per team

    team1 = TEAMS[0] #Assigns teams, team lists and amount of experienced players
    team_1_players = []
    team_1_experienced_count = 0

    team2 = TEAMS[1]
    team_2_players = []
    team_2_experienced_count = 0

    team3 = TEAMS[2]
    team_3_players = []
    team_3_experienced_count = 0

    while true_list_indexer < len(true_list): #Loop keeps running until the players in the experienced list are all assigned
        if team_1_experienced_count < len(true_list)/3: #If team 1's experienced player count is less than 1/3 of all experienced players, then more will be added
            team_1_players.append(true_list[true_list_indexer])
            true_list_indexer += 1 #Position of index in the true_list for record keeping
            loop_indexer += 1 #Records position of index for total players 
            team_1_experienced_count += 1 #Increases team 1's experiened count by 1
        
        elif team_2_experienced_count < len(true_list)/3:
            team_2_players.append(true_list[true_list_indexer])
            true_list_indexer += 1
            loop_indexer += 1
            team_2_experienced_count += 1

        elif team_3_experienced_count < len(true_list)/3:
            team_3_players.append(true_list[true_list_indexer])
            true_list_indexer += 1
            loop_indexer += 1
            team_3_experienced_count += 1

    while loop_indexer < len(PLAYERS): #Now that there are no more experienced players to be added. The non-experienced are added
        if len(team_1_players) < player_number_team: #If team 1 has less players than max capacity, more will be added
            team_1_players.append(false_list[false_list_indexer]) #Added from the false_list
            false_list_indexer += 1 #Indexer for false list +1
            loop_indexer += 1 #Overall players loop +1
        
        elif len(team_2_players) < player_number_team:
            team_2_players.append(false_list[false_list_indexer])
            false_list_indexer += 1
            loop_indexer += 1
        
        elif len(team_3_players) < player_number_team:
            team_3_players.append(false_list[false_list_indexer])
            false_list_indexer += 1
            loop_indexer += 1

    return team_1_players, team_2_players, team_3_players, team_1_experienced_count, team_2_experienced_count, team_3_experienced_count


def team_average_height(n): #This will take a input and return the average height of the team
    total_height = 0
    player_height_dict = height_list() #Calls the name:height dictionary made earlier
 
    for key in player_height_dict: #For each name in the dictionary, 
        if key in n:               #If the name is a part of the team inputted, the height is taken and summed into the total
            total_height += player_height_dict[key]

    average_height = total_height/len(n) #Sum up and divide by players in team

    return round(average_height, 2) #Round to 2dp


def team_stats(n): #This will print the stats part of the menu after a team has been selected
    player_list_string = ''
    average_height = team_average_height(n)
    team_1_players, team_2_players, team_3_players, team_1_experienced, team_2_experienced, team_3_experienced = balance_team()

    if n == 'a': #If the parameter is a, then the set of conditions will occur
        team = TEAMS[0]

        for players in team_1_players:  #These just call upon the previous functions
            player_list_string += players + ", "
        player_list_string = player_list_string[:-2]
        user_input_2_valid = True
        experienced_true = team_1_experienced
        experienced_false = len(team_1_players) - team_1_experienced
        team_height = team_average_height(team_1_players)
        guardian_list = guardian_per_team(n)
        total_players = len(team_1_players)

    elif n =='b':
        team = TEAMS[1]

        for players in team_2_players:
            player_list_string += players + ", "
        player_list_string = player_list_string[:-2]
        user_input_2_valid = True
        experienced_true = team_2_experienced
        experienced_false = len(team_2_players) - team_2_experienced
        team_height = team_average_height(team_1_players)
        guardian_list = guardian_per_team(n) 
        total_players = len(team_2_players)

    elif n == 'c':
        team = TEAMS[2]

        for players in team_3_players:
            player_list_string += players + ", "
        player_list_string = player_list_string[:-2]
        user_input_2_valid = True
        experienced_true = team_3_experienced
        experienced_false = len(team_3_players) - team_3_experienced
        team_height = team_average_height(team_3_players)
        guardian_list = guardian_per_team(n)
        total_players = len(team_3_players)

    else:
        print("Invalid please try again") 

    print("Team: {} Stats".format(team)) #prints out team stats
    print("--------------------")
    print("Total players: {}\n".format(total_players))
    print("Players on team: ")
    print("  " + player_list_string)
    print("Experienced players: {}".format(experienced_true))
    print("No experience players: {}".format(experienced_false))
    print("Guardians list: {}".format(guardian_list))
    print("Average team height: {} ".format(team_height))


if __name__ == "__main__": #These functions will run when the mainfile is run
    players_dictionary_list = copy.deepcopy(PLAYERS)  #Global variables
    change_height()
    height_list()
    change_experience()
    change_guardian_to_string()
    team_1_players, team_2_players, team_3_players, team_1_experienced, team_2_experienced, team_3_experienced = balance_team()
    player_guardian_dict = change_guardian_to_string()
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
    

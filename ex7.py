"""******************************
*Student name: Daniel Saraf
*Student ID: 311312045
*Exercise name: ex7
******************************"""
# Imports
import sys
import os

def findByMovie(moviesDB):
    """
    The function gets a string from the user with 2 movies and operator and
    print the appropriate actors:
    operator & - All the actors that played in both of the movies
    operator | - All the actors that played in some of the movies
    operator ^ - All the actors that played in exactly one of the movies
    Keyword arguments: An access to the DataBase
    Return: -
    """
    print("Please select two movies and an operator(&,|,^) separated with ',':")
    # Input the user string into MoviesStr
    moviesStr = input()
    # Send the string to stringChecker to check if there is valid number of movies
    if stringChecker(moviesStr) is False:
        print("Error")
        return
    # Separate The string to movie 1 , movie 2 and the operator
    movie1 = moviesStr.split(",")[0].strip()
    movie2 = moviesStr.split(",")[1].strip()
    operator = moviesStr.split(",")[2].strip()
    # Check if the movies include in the DataBase
    if movie1 not in moviesDB or movie2 not in moviesDB:
        # If not - return
        print("Error")
        return
    # Check the operator and move to the appropriate function
    if operator is "&":
        printCommon(moviesDB, movie1, movie2)
    elif operator is "|":
        printUnion(moviesDB, movie1, movie2)
    elif operator is "^":
        printXor(moviesDB, movie1, movie2)
    else:
        # The operator is not valid
        print("error")
        return
def printCommon(moviesDB, movie1, movie2):
    """
    The function gets two movies and print all the actors that played in
    both of them
    Keyword arguments: An access to the DataBase and names of 2 movies
    Return: -
    """
    # Create the group of the common actors, sort in a lexicographic order
    commonActors = sorted(moviesDB[movie1] & moviesDB[movie2])
    # Check if the group of the common players in an empty group
    if len(commonActors) is 0:
        # in case of empty group - print an appropriate message and return
        print("There are no actors in this group")
        return
    # Print all the actors in the commonActors group
    for i in range(0, len(commonActors)):
        # If this current actor is not the last one
        if i is not len(commonActors) - 1:
            # Write "," after is name without new line
            print(commonActors[i], end=", ")
        else:
            # Put new line after the last actor name
            print(commonActors[i])
    return
def printUnion(moviesDB, movie1, movie2):
    """
    The function gets two movies and print all the actors that played in
    one of them
    Keyword arguments: An access to the DataBase and names of 2 movies
    Return: -
    """
    # Create a group of the actors who played in at least one of the movies
    # sort it in a lexicographic order
    unionActors = sorted(moviesDB[movie1] | moviesDB[movie2])
    # Check if the group is empty of actors
    if len(unionActors) is 0:
        # In case of empty group - print an appropriate message and return
        print("There are no actors in this group")
        return
    # Print all the actors in the unionActors group
    for i in range(0, len(unionActors)):
        # If this current actor is not the last one
        if i is not len(unionActors)-1:
            # Write "," after is name without new line
            print(unionActors[i], end=", ")
        else:
            # Put new line after the last actor name
            print(unionActors[i])
    return
def printXor(moviesDB, movie1, movie2):
    """
    The function gets two movies and print all the actors that played in
    exactly one of them
    Keyword arguments: An access to the DataBase and names of 2 movies
    Return: -
    """
    # Create a group of the actors who played in at exactly one of the movies
    # sort it in a lexicographic order
    xorActors = sorted(moviesDB[movie1] ^ moviesDB[movie2])
    # Check if the group is an empty group
    if len(xorActors) is 0:
        # In Case of empty group, Print appropriate massage and return
        print("There are no actors in this group")
        return
    # Print all the actors in the commonActors group
    for i in range(0, len(xorActors)):
        # If this current actor is not the last one
        if i is not len(xorActors)-1:
            # Write "," after is name without new line
            print(xorActors[i], end=", ")
        else:
            # Put new line after the last actor name
            print(xorActors[i])
    return
def stringChecker(moviesStr):
    """
    The function gets a string and count the "," characters in it
    if it appear twice - The string is valid,
    in and other case the string is not valid
    Keyword arguments: a string
    Return: True - in case of valid string, False - in case of bad string
    """
    if moviesStr.count(",") != 2:
        return False
    else:
        return True
def findByActor(moviesDB, moviesList, actorsList):
    """
    The function ask for a name of a actor from the user and print
    all the actors that ever played with him
    Keyword arguments: access to the DataBase, list of movies and list of actors
    Return: -
    """
    print("Please select an actor:")
    actor = input()
    # Check if the actor is in the DataBase
    if actor not in actorsList:
        # In case the actor dont exists, print appropriate message and return
        print("Error")
        return
    # 'subPlayers' will be the group with all the sub players
    subPlayers = set()
    # Scan all the movies in the DataBase
    for i in range(0, len(moviesList)):
        # If you find the actor in some Movie
        if actor in moviesDB[moviesList[i]]:
            # Combine the subPlayers group with all the actors in this movie
            subPlayers = subPlayers | moviesDB[moviesList[i]]
    # Remove the actor itself
    subPlayers.remove(actor)
    # Check if there is no sub players
    if len(subPlayers) is 0:
        print("There are no actors in this group")
        return
    # Sort subPlayer group in a lexicographic order
    subPlayers = sorted(subPlayers)
    # Print all the actors in the subPlayers group
    for i in range(0, len(subPlayers)):
        # If this current actor is not the last one
        if i is not len(subPlayers)-1:
            # Write "," after is name without new line
            print(subPlayers[i], end=", ")
        else:
            # Put new line after the last actor name
            print(subPlayers[i])
    return
def insertMovie(moviesDB, moviesList, actorsList):
    """
    The function ask from the user a new/ existing movie it players
    in case of new movie it create new key in the DataBase dictionary.
    in case of existing movie it add the players to the existing group
    Keyword arguments: access to the DataBase, list of movies and list of actors
    Return: -
    """
    print("Please insert a new movie:")
    movieString = input()
    # Check the input string
    if "," not in movieString:
        # In case of no actors (no ',' character) - return
        print("Error")
        return
    """ 
    
    split movieString into part after every "," character. 'newMovie' will be a
    array when its first index is the name of the movie and his other cells 
    is the actors played on this movie
    
    """
    newMovie = movieString.split(",")
    # 'actors' will fill with all the actors who's played in the movie
    actors = set()
    # Fill 'actor' set with all the actors
    for i in range(1, len(newMovie)):
        actors.add(newMovie[i].strip())
    # Check if the movie is already in the DataBase
    if newMovie[0].strip() in moviesDB:
        # If it is, update its actors with the new actors
        moviesDB[newMovie[0].strip()].update(actors)
    else:
        # If its a new movie, make new key and enter all the actors to it
        moviesDB[newMovie[0].strip()] = actors
        # Also update the movies list
        moviesList.append(newMovie[0].strip())
    # Update the actors list with all the new actors
    actorsList.update(actors)
    return
def exportData(moviesDB, moviesList, actorsList):
    """
    The function write all the DataBase to a file in a specific format
    of ActorName, Movie1, Movie2 ...
    The name of the file is given as a argument to the program
    Keyword arguments: access to the DataBase, list of movies and list of actors
    Return: -
    """
    # Change file promotions so it can be writable
    os.chmod(sys.argv[2], 0o777)
    # Open the file, sys.argv[2] hold the name of it
    moviesFile = open(sys.argv[2], "w")
    # Change the type of actorsList from Set to List so it can be use with index
    actorsList = list(actorsList)
    # print all the actors and their movies in each line
    for i in range(0, len(actorsList)):
        # Do only if it is not the first actor name
        if i != 0:
            # This command use to rewrite the ',' character in the end of the line with new line ('\n')
            moviesFile.seek(moviesFile.tell() - 2, os.SEEK_SET)
            print("", file=moviesFile)
        # Print the name if the actor to the file, dont print new line
        print(actorsList[i]+", ", end="", file=moviesFile)
        # Aftre the name print all the movies he played in
        for j in range(0, len(moviesList)):
            if actorsList[i] in moviesDB[moviesList[j]]:
                # Print the movie, put ',' in the end, Dont print new line
                print(moviesList[j]+", ", end="", file=moviesFile)
    # This command use to delete the ',' character in the end of the file
    moviesFile.truncate(moviesFile.seek(moviesFile.tell() - 2, os.SEEK_SET))
    # Close the file
    moviesFile.close()
    return
def memoryInt():
    """
    The program declare on a dictionary that will be use as a DataBase
    it read all the information from the file (the name of the file come as a
    argument to the program) and order it in a way that the name of the movies
    will use as a keys and the actors will be the value
    the program also creat a list of all the movies and a list of all the actors
    exist in the DataBase
    Keyword arguments: -
    Return: access to the DataBase, list of movies and list of actors
    """
    print("Processing...")
    # Declaration of the dictionary and the movies&actors set
    moviesDB = {}
    # This sets will be convert to a list
    moviesList = set()
    actorsList = set()
    # Open the file, sys.argv[1]) holds his name
    moviesFile = open(sys.argv[1])
    # 'linesArr' is an array that every cell in it is a line in the file
    linesArr = moviesFile.readlines()
    # Make a List of all Movies and Actors, check each line
    for i in range(len(linesArr)):
        # Add to actorList the name of the actor appear in the first word of the line, ignore left $ right spaces
        actorsList.add(linesArr[i].split(",")[0].strip())
        # Read all the other words in the line
        for k in range(1, len(linesArr[i].split(","))):
            # Add the movies to 'movieList' set
            moviesList.add(linesArr[i].split(",")[k].strip())
    # ---------------------------- Fill The DataBase  ---------------------------------------------
    # Convert movieList the a list so it will support indexing
    moviesList = sorted(list(moviesList))
    # Scan all the movies in moviesList
    for i in range(0, len(moviesList)):
        # Create an empty set in every key
        moviesDB[moviesList[i]] = set()
        # Scan all lines in the file (Same number as actorList size)
        for j in range(0, len(actorsList)):
            # Scan all the movies in the specific line
            for k in range(1, len(linesArr[j].split(","))):
                # Check if the current movie is a word in the line
                if moviesList[i] == linesArr[j].split(",")[k].strip():
                    # If it is, add the actor that played in the movie to the values of this movie key
                    moviesDB[moviesList[i]].add(linesArr[j].split(",")[0].strip())
    # Close the file
    moviesFile.close()
    # Return the DataBase and list of movies and actors
    return moviesDB, moviesList, actorsList
def mainMenu(moviesDB, moviesList, actorsList):
    """
    This function is the main menu of the program, Here the user start and
    chose what he/she want to do. It contain a menu with 5 different options
    Keyword arguments: access to the DataBase, list of movies and list of actors
    Return: -
    """
    while 1:
        print("Please select an option:\n1) Query by movies")
        print("2) Query by actor\n3) Insert a new movie\n4) Save and Exit\n5) Exit")
        key = input()
        # Go to the chosen path
        if key is "1":
            findByMovie(moviesDB)
        elif key is "2":
            findByActor(moviesDB, moviesList, actorsList)
        elif key is "3":
            insertMovie(moviesDB, moviesList, actorsList)
        elif key is "4":
            exportData(moviesDB, moviesList, actorsList)
            return
        elif key is "5":
            return
def main():
    """
    This is The main function, It call to memoryInt function to
    initialize the DataBase and than send the returning accesses to
    the main menu to start the user Intervention part
    """
    moviesDB, moviesList, actorsList = memoryInt()
    mainMenu(moviesDB, moviesList, actorsList)
    exit(0)

# Call to main
if __name__ == "__main__":
    main()

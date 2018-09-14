import os


def searchDir(targetDir, name):
    result = []
    for root, dirs, files in os.walk(targetDir, topdown=True):
        if name in dirs:
            result = os.path.join(root, name)
            break
    return result


def rePrompt():
    yes = 'y'
    no = 'n'
    searchAgain = 0
    print()
    print('Would you like to search again? Please enter \'y\' or \'n\'')
    searchPrompt = input()
    for i in range(10):
        if searchPrompt == yes:
            searchAgain = 1
        elif searchPrompt == no:
            break
        elif searchPrompt != no & i < 5:
            print('Please enter only \'y\' or \'n\'')
            continue
        elif i == 10:
            print('Too many invalid inputs.')
            print('Exiting Program')
            quit()
    return searchAgain


def searchPrompt():
    cwDir = os.getcwd()
    yes = 'y'
    no = 'n'
    print('This will search the current working directory and its subdirectories.')
    print(cwDir)
    print()
    print('Would you like to search a different directory? y or n')
    searchDif = input()
    if searchDif == yes:
        print('Please enter the directory you would like to search.')
        print('Be sure to use a double slash \\\\ instead of a single slash \\')
        newDir = input()
        newDirNice = os.path.abspath(newDir)
        os.chdir(newDirNice)
        cwDir = os.getcwd()
        print('Now searching in ' + cwDir)
        print()

    print('Please enter target directory name:')
    search4 = input()
    return search4


while (1):
    try:
        wantItem = searchPrompt()
        cwDir = os.getcwd()
        searchResult = searchDir(cwDir, wantItem)
        print(searchResult)
        reRun = rePrompt()
        if reRun == 1:
            continue
        else:
            print('Exiting Program')
            break
    except:
        print('Unexpected Error')
        break

import itertools


def main():
    logo = """
     _     ___   ____  ___  
    | |   / _ \ / ___|/ _ \ 
    | |  | | | | |  _| | | |
    | |__| |_| | |_| | |_| |
    |_____\___/ \____|\___/ """
    user_input = "!"
    keywords = []
    print(logo)
    print("Welcome to password generator")
    print("Enter some keywords")
    print("Possible keywords:")
    print("Name/Surname/Lastname")
    print("Nickname")
    print("Names of friends, children, family")
    print("Date of birth")
    print("\"Lucky\" numbers")
    print("Some another keywords: words from famous book, etc.")
    print("Leave blank to finish")
    while user_input != "":
        user_input = input(">>>")
        if len(user_input) == 0:
            break
        keywords.append(user_input)

    print("Enter output filename")

    user_input = input(">>>")

    while user_input == "":
        print("Enter valid filename!")
        user_input = input(">>>")

    outFilename = user_input

    max_keywords = 3

    print("Enter maximum count of keywords in password")
    print("Leave blank for default (3)")
    try:
        user_input = input(">>>")
        max_keywords = int(user_input)
    except:
        print("Default")


    count_of_combinations = len(keywords) ** max_keywords

    print(str(count_of_combinations) + " passwords will be generated")

    outputFile = open(outFilename, "w")

    for combination in itertools.combinations(keywords, max_keywords):
        outputFile.write("".join(combination))
        outputFile.write("\n")

    outputFile.close()

    print("Finished")


if __name__ == "__main__":
    main()

import itertools
import os


def main():
    logo = r"""
     ____                ____            
    |  _ \ __ _ ___ ___ / ___| ___ _ __  
    | |_) / _` / __/ __| |  _ / _ \ '_ \ 
    |  __/ (_| \__ \__ \ |_| |  __/ | | |
    |_|   \__,_|___/___/\____|\___|_| |_|
    """
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


    if not os.path.exists("dictionaries"):
        os.mkdir("dictionaries")
        

    outputFile = open(os.path.join("dictionaries", outFilename), "w")
    for count_of_keywords in range(1, max_keywords):
        for combination in itertools.combinations(keywords, count_of_keywords):
            outputFile.write("".join(combination))
            outputFile.write("\n")

    outputFile.close()

    print("Finished")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        print("Detected Ctrl-C, stopping...")

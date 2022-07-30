
patterns = ["***", "*  ", " * ", "  *", "* *"]

num_2 = """
***
*
***
  *
***
"""


def enter_digit():
    disnumber= str(input("please enter a postive number: "))
    if int(disnumber) <= -1:
        return enter_digit()
    else:
        return disnumber
  

def display_digit(st_num):
    for ch in st_num:
        if ch == "0":
            print("", patterns[0], "\n", patterns[4], "\n", patterns[4], "\n", patterns[4],"\n", patterns[0], end=" ")
        elif ch == "1":
            print("", patterns[2], "\n", patterns[2], "\n", patterns[2], "\n", patterns[2],"\n", patterns[2], end=" ")
        elif ch == "2":
            print("", patterns[0], "\n", patterns[3], "\n", patterns[0], "\n", patterns[1],"\n", patterns[0], end=" ")
        elif ch == "3":
            print("", patterns[0], "\n", patterns[3], "\n", patterns[0], "\n", patterns[3],"\n", patterns[0], end=" ")
        elif ch == "4":
            print("", patterns[4], "\n", patterns[4], "\n", patterns[0], "\n", patterns[3],"\n", patterns[3], end=" ")
        elif ch == "5":
            print("", patterns[0], "\n", patterns[1], "\n", patterns[0], "\n", patterns[3],"\n", patterns[0], end=" ")
        elif ch == "6":
            print("", patterns[0], "\n", patterns[1], "\n", patterns[3], "\n", patterns[4],"\n", patterns[0], end=" ")
        elif ch == "7":
            print("", patterns[0], "\n", patterns[3], "\n", patterns[3], "\n", patterns[3],"\n", patterns[3], end=" ")
        elif ch == "8":
            print("", patterns[0], "\n", patterns[4], "\n", patterns[0], "\n", patterns[4],"\n", patterns[0], end=" ")
        elif ch == "9":
            print("", patterns[0], "\n", patterns[4], "\n", patterns[0], "\n", patterns[3],"\n", patterns[3], end=" ")

    
disnumber = enter_digit()
display_digit(disnumber)


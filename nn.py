import datetime

def fun():
    f = open("guvi.txt", "w")
    print(f.name)
    if f.name == "guvi.txt":
        x = datetime.datetime.now()
        f.write(f'Current date and time: " + {x}')
        f.close()  # Don't forget to close the file after writing
        print("Current date and time written to the file.")
    else:
        print("Error")

fun()

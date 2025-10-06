with open("output.txt", "w") as file:
    file.write(input("encode your message: ")+ "\n" + "message is successfully written\n")
with open("output.txt", "a") as file:
    file.write(input("encode your message to append: ")+ "\n" + "message is successfully appended\n")
with open("output.txt", "r") as file:
    print("final content:\n" + file.read())
print("=" * 40)
print("        X AI Assistant")
print("=" * 40)

print("Status : Ready")
print("Voice  : Waiting...")
print("Mode   : Beginner Version")

while True:

    command = input("You : ")

    if command.lower() == "exit":
        print("X : Goodbye!")
        break

    elif command.lower() == "hello":
        print("X : Hello! Nice to meet you.")

    elif command.lower() == "who are you":
        print("X : I am X, your AI Assistant.")

    else:
        print("X : I heard ->", command)

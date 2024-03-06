# user_input.py

def main():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    location = input("Please enter your location: ")

    print("Hello", name + ",", "you are", age, "years old and live in", location + ".")

if __name__ == "__main__":
    main()

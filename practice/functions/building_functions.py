

# definfing function with "def"
def hello_world():
    print("hello world")

# call/invoke of function
hello_world()

# defining a funtion with parameters

def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else: 
        print("hello")

# calling funtion by passing argument
greet("es")
class Destructor:
    def __init__(self):
        self.greet = "Good Morning"
    def display(self):
        print("Greeting message:", self.greet)
    def __del__(self):
        print("Object is destroyed")
s = Destructor()
s.display()
print(s)
del s


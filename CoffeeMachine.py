class CoffeeMachine:
    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.action = ""
        self.w = 0
        self.mi = 0
        self.b = 0
        self.mo = 0
    
    def log_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money,"of money")

    def check(self):
        if self.water < self.w:
            print("Sorry, not enough water!")
        if self.milk < self.mi:
            print("Sorry, not enough milk!")
        if self.beans < self.b:
            print("Sorry, not enough beans!")
        if self.cups < 1:
            print("Sorry, not enough cups!")
        if not (self.water < self.w or self.milk < self.mi or self.beans < self.b or self.cups < 1):
            print("I have enough resources, making you a coffee!")
            self.cook()
    
    def cook(self):
        self.cups -= 1
        self.water -= self.w
        self.milk -= self.mi
        self.beans -= self.b
        self.money += self.mo
          
    def buy(self):
        self.number = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.number == "1":
            self.w = 250
            self.mi = 0
            self.b = 16
            self.mo = 4
            self.check()
        if self.number == "2":
            self.w = 350
            self.mi = 75
            self.b = 20
            self.mo = 7
            self.check()
        if self.number == "3":
            self.w = 200
            self.mi = 100
            self.b = 12
            self.mo = 6
            self.check()

    
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
    
    def work(self):
        while self.action != "exit":
            self.action = input("Write an action (buy, fill, take, remaining, exit):")
            if self.action == "buy":
                self.buy()
            if self.action == "fill":
                self.fill()
            if self.action == "take":
                self.take()
            if self.action == "remaining":
                self.log_state()

masha = CoffeeMachine(550, 400, 540, 120, 9)
masha.work()

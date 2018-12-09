import random

# Gathers basic player information with input statements
print("Welcome to IB Trial! The trial that will lead you to your IB Diploma!")
print("\n")
user_name = input("What is your name?: ")
print("\n")
print("Nice to meet you", user_name,"!")
print("it is time to choose your classes ")

# Creats a class inorder to set up the starting stats of a Character
class Character():
   def __init__(self, name, sanity, ib, money):
       self.sanity = sanity
       self.ib = ib
       self.name = user_name
       self.money = money
# by user input, the user selects there classes
   def courses(self):
       pick_classes = input('English SL or HL?:')
       pick_classes2 = input("History SL or HL?:")
       pick_classes3 = input("Do you take an HL science, SL science, or ESS?:")
       pick_classes4 = input("Do you take Art, Compsci, Business, or Music?:")
       pick_classes5 = input("Do you take Stat, Studies, SL, or HL?:")
       pick_classes6 = input("Do you take an Abinicio, SL, or HL language?:")
       print("\n")
# through if statement it gives the starting IB and sanity Points
# Each class is assigned an amout of points and adds or subtracts from the chacters value
       if pick_classes == "SL":
           self.sanity = self.sanity + 1
       if pick_classes == "HL":
           self.ib = self.ib + 2
           self.sanity = self.sanity - 2
       if pick_classes2 == "SL":
           self.sanity = self.sanity + 1
       if pick_classes2 == "HL":
           self.ib = self.ib + 2
           self.sanity = self.sanity - 2
       if pick_classes3 == "HL":
           self.ib = self.ib + 4
           self.sanity = self.sanity - 3
       if pick_classes3 == "SL":
           self.ib = self.ib +1
           self.sanity = self.sanity - 1
       if pick_classes3 == "ESS":
           self.ib = self.ib -3
           self.sanity = self.sanity + 2
       if pick_classes4 == "HL":
           self.ib = self.ib + 4
           self.sanity = self.sanity - 3
       if pick_classes4 == "SL":
           self.ib = self.ib + 2
           self.sanity = self.sanity - 2
       if pick_classes4 == "Compsci":
           self.sanity = self.sanity - 1
           self.ib = self.ib + 1
       if pick_classes4 == "Theater" or "Art" or "Bussiness":
           self.sanity = self.sanity + 1
           self.ib = self.ib - 1
       if pick_classes5 == "Studies":
           self.ib = self.ib - 3
           self.sanity = self.sanity + 2
       if pick_classes5 == "SL":
           self.ib = self.ib + 1
           self.sanity = self.sanity -1
       if pick_classes5 == "HL":
           self.ib = self.ib + 4
           self.sanity = self.sanity -3
       if pick_classes6 == "Abinicio":
           self.ib = self.ib - 2
           self.sanity = self.sanity + 2
       if pick_classes6 == "SL":
           self.sanity = self.sanity + 1
       if pick_classes6 == "HL":
           self.ib = self.ib + 2
           self.sanity = self.sanity + 2
       if self.sanity < 0:
           print("this is too difficult")
       if self.sanity >= 0:
           self.sanity = (1 - (1/self.sanity)) * 100
           print("You start with", self.ib, "IB points" )
           print("You are",round(self.sanity,2), "% sane" )
           print("\n")
# charcters starting attibutes
name = Character('name', 10, 5, 300)
name.courses()

# The next step is the store
class Store():
   def __init__(self, name, price, money):
       self.name = user_name
       self.price = price
       self.money = money
# creats a process for buying where it subtracts the cost of the iteam from the toal money
   def buy(self):
       item = input('You have 300$. Would you like to buy a test ($80), adderall ($50), or a bribe ($210)')
       items = []
       if item == 'adderall':
           item = adderall
           self.money = self.money - adderall.price
           if self.money == 0:
               print("You're broke")
           if self.money > 0:
               print("You have $", self.money, "left")
               items.append(adderall)
       if item == 'bribe':
           item = bribe
           self.money = self.money - bribe.price
           if self.money == 0:
               print("You're broke")
           if self.money > 0:
               print("You have $", self.money, "left")
               items.append(bribe)
       if item == 'buy a test':
           item = buy_test
           self.money = self.money - buy_test.price
           if self.money == 0:
               print("You're broke")
           if self.money > 0:
               print("You have $", self.money, "left")
               items.append(buy_test)

# differnt iteams you can buy
bribe = Store('bribe', 210, 300)
adderall = Store('adderall', 50, 300)
buy_test = Store('buy a test', 80, 300)
bribe.buy()

class Risk(Character):
   #    self.sanity = sanity, self.ib = ib, self.name = user_name
   # def __init__(self):
   #    super(). __init__()
   #     self.name = user_name
   #     self.sanity = sanity
   #     self.ib = ib
   def cheating(self):
       pick_attack = input('Good morning, it is test day, are you using the supply? yes or no')
       if pick_attack == 'yes':
           risk = random.randint(0,2)
           if risk == 0:
               self.ib = self.ib + 1
               print("Congratulations! You aced the test without having to study!")
               print("You get +1 IB points")
           elif risk != 0:
               print("Uh-oh!! You just committed an infraction! -2 point of your IB score!")
               self.ib = self.ib - 2
       else:
           risk = random.randint(0,1)
           if risk == 0:
               self.ib = self.ib - 1
               print("Aw...but at least you did the right thing!")
               print("-1 IB points")
           if risk != 0:
               self.ib = self.ib + 1
               print("Congratulations!!! You passed the test")
               print("+1 IB Points")
               print("It's good to do the right thing!")
       print(self.name, 'has', self.ib, 'IB points left\n')
name = Risk('bob', 100, 20, 100)
name.cheating()

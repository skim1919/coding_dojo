class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0


# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print("========================")
        print(f"First name: {self.first_name}")
        print(f"Last_name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_memeber}")
        print(f"Current Points: {self.gold_card_points}")
        print("========================")

# Have this method change the user's member status to True and set their gold card points to 200.
# =====================
    def enroll(self):
        if self.is_rewards_memeber:
            print("User already a member.")
            return False

        self.is_rewards_memeber = True
        self.gold_card_points = 200

# have this method decrease the user's points by the amount specified.
#Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            "You don't have enough points."
            return # exit function
        self.gold_card_points -= amount




my_user = User("Sarang", "Kim", "sarangk1919@gmail.com", 10)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(50)
my_user.display_info()
my_user2 = User("Hyunwook", "Baek", "hyunwookbaek@gmail.com", 20)
my_user2.display_info()
my_user2.enroll()
my_user2.spend_points(80)
my_user2.display_info()
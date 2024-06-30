class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name +  "says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight you")
        return True 

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
        else:
            print(self.name + "swallows you, little wimp.")
            return False
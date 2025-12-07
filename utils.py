DISTANCE_BETWEEN_STATIONS = 500
RANDOM_PASSENGER_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah",
    "Ian", "Jenna", "Kevin", "Luna", "Mason", "Nina", "Owen", "Paula",
    "Quinn", "Riley", "Sam", "Tara", "Uma", "Victor", "Wendy", "Xavier",
    "Yara", "Zane", "Aiden", "Bella", "Caleb", "Delia", "Elias", "Freya",
    "Gavin", "Hazel", "Isaac", "Jade", "Kai", "Leah", "Miles", "Nora",
    "Olivia", "Parker", "Quincy", "Rosie", "Silas", "Tessa", "Uri", "Vera",
    "Wade", "Xena", "Yuri", "Zara", "Abel", "Brielle", "Cody", "Daphne",
    "Emmett", "Faith", "Griffin", "Harper", "Ivy", "Jonah", "Kira", "Liam",
    "Mila", "Noah", "Opal", "Paige", "Ronan", "Sage", "Talon", "Ulysses",
    "Valerie", "Wren", "Xander", "Yvonne", "Zack", "Amelia", "Brandon",
    "Carmen", "Derek", "Evelyn", "Felix", "Georgia", "Holden", "Isla",
    "Jasper", "Kelsey", "Logan", "Molly", "Nate", "Odette", "Preston",
    "Raina", "Sawyer", "Toby", "Unity", "Van", "Whitney", "Ximena", "Yasmin",
    "Zion", "Asher", "Bianca", "Cassidy", "Damian", "Elsa", "Finley",
    "Giselle", "Hugo", "Ines", "Jeremiah", "Keira", "Leon", "Maeve",
    "Nolan", "Oriana", "Paxton", "Raquel", "Soren", "Tracy", "Ulric",
    "Violet", "Winston", "Xia", "Yosef", "Zuri", "Ariana", "Bennett",
    "Clara", "Damon", "Esther", "Frank", "Gemma", "Heidi", "Imani", "Jordan",
    "Kendall", "Lara", "Mitchell", "Nadia", "Orion", "Phoebe", "Reed",
    "Serena", "Titus", "Umar", "Vivian", "Willa", "Xolani", "Yami", "Zander",
    "Adrian", "Brittany", "Chase", "Dalia", "Everett", "Frida", "Gage",
    "Helena", "Iker", "Jamie", "Kamila", "Luca", "Mira", "Neal", "Odis",
    "Piper", "Rhett", "Selena", "Thane", "Ulani", "Vince", "Wylie", "Xavi",
    "Yanis", "Zelda", "Aria", "Boris", "Coral", "Dante", "Elise", "Faye",
    "Gwen", "Harlan", "Irina", "Jace"
]

def title(statement):
    """ 
    Takes in a string argument
    return a string with ascii decos
    """

    textLength = len(statement)

    result = ""
    result = result + "+--" + "-" * textLength + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * textLength + "--+\n"
    
    return result;

def getMetersPerSecond(kmh):
    """
    Converts km/h to m/s
    """
    return kmh * (1000/3600)
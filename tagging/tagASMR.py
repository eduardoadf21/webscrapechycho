
from pymongo_get_database import get_database

chychoVault = get_database()
posts = chychoVault["posts3"]

asmr = ("Soft-Spoken Reading of WikiLeaks",
    "Jarring Dried Mint",
    "Let's Make Some Power Food",
    "Net Neutrality: My Perspective of Both Sides of the Debate, Pros and Cons.",
    "How to Play Street Dice: A Simplified Craps Game",
    "How to Play Monopoly: Variant Rules: Fast Rapid Games, Multiple Games per Gaming Sessions",
    "Thank You for Your Recommendations",
    "Comics Code Authority",
    "War Is A Racket by Major General Smedley Butler",
    "Science Fiction and Fantasy Book Recommendations: Let Me Show You My Collection",
    "Whispering WikiLeaks",
    "The Do's and Don'ts of Cliff Jumping: Advice on How to Stay Alive to Jump Another Day and Some Jumping Stories",
    "Playing Chess by the Fire: Let Me Show You My Marble Chess Set and a 4 and 5 Move Checkmate Sequence, Scholar's Mate",
    "Let Me Show You My Board Game Collection",
    """Reading: Whispering Max Ehrmann's "Desiderata" """,
    "How to Make Crab Apple Butter, Crabapple Spread",
    "Let Me Show You Our Plant Collection",
    "Intro to Q&A: In Conversation with Chycho: What Would You like to Know?",
    "Setting up, Settling in, Sleeping in Our New Space",
    "Let's Take a Look at a Crystal and Mineral Collection",
    "Beards and Food, How It Works: The Beauty of Beards, Enhancing the Eating Experience",
    "Watching a Baby Hummingbird in Its Nest in a Tree for 38 Minutes",
    "Jarring 20 Pounds of Honey",
    "Trimming Facial Hair: Managing My Goatee",
    "Taking Down the Numbers, Pulling Off the Tape",
    "Let's Take a Look at Some Art",
    "ASMR Math: Introduction and Table of Contents",
    "Best Shaving Cream in the World, Coconut Oil",
    "All About Comic Books: Readings, Reviews and Recommendations, Framings, Collections and Articles",
    "ASMR Math: Two Hand Tricks to Learn Your Multiplication Table",
    "Eating Autumn Olives",
    "Let Me Show You My Grandmother's Backgammon Board: Me and Grandma Playing Backgammon",
    "The Pomegranate ASMR Video Page",
    "For the ASMR Community: Extended Cuts of Picking My Beard ",
    "Let's Make Some Power Food: Dates, Eggs, Tomatoes, Tahini, Feta, How to Recipe (Twitch Live Stream).",
    "Net Neutrality: My Perspective of Both Sides of the Debate, Pros and Cons.",
    "How to Play Street Dice: A Simplified Craps Game",
    "How to Play Monopoly: Variant Rules: Fast Rapid Games, Multiple Games per Gaming Sessions",
    "Thank You for Your Recommendations: Feist’s Magician (The Riftwar Saga), The Walking Dead, Johnny Got His Gun, Darker than Black, Redline, and More",
    "Reading: Comics Code Authority (CCA): SOTI Comics and the 1954 Code Criteria for Censoring Comic Books",
    "Reading: War Is A Racket by Major General Smedley Butler",
    "Science Fiction and Fantasy Book Recommendations: Let Me Show You My Collection",
    """Reading: Whispering WikiLeaks' Vault 7 "Year Zero": CIA Hacking Tools Revealed""",
    "Advice on How to Stay Alive to Jump Another Day and Some Jumping Stories",
    "Playing Chess by the Fire: Let Me Show You My Marble Chess Set and a 4 and 5 Move Checkmate Sequence, Scholar's Mate",
    "Let Me Show You My Board Game Collection",
    """Whispering Max Ehrmann's "Desiderata" """,
    "How to Make and Eat Crab Apple Butter, Crabapple Spread",
    "Let Me Show You Our Plant Collection",
    "Intro to Q&A: In Conversation with Chycho: What Would You like to Know?",
    "Setting up, Settling in, Sleeping in Our New Space",
    "Let's Take a Look at a Crystal and Mineral Collection",
    "Beards and Food, How It Works: The Beauty of Beards, Enhancing the Eating Experience",
    "Watching a Baby Hummingbird in Its Nest in a Tree for 38 Minutes",
    "Jarring 20 Pounds of Honey",
    "Trimming Facial Hair: Managing My Goatee",
    "Taking Down the Numbers, Pulling Off the Tape",
    "Let's Take a Look at Some Art",
    "ASMR Math: Introduction and Table of Contents",
    "Best Shaving Cream in the World, Coconut Oil",
    "All About Comic Books: Readings, Reviews and Recommendations, Framings, Collections and Articles",
    "ASMR Math: Two Hand Tricks to Learn Your Multiplication Table",
    "Eating Autumn Olives",
    "The Pomegranate Video Page",
    "Let Me Show You My Grandmother's Backgammon Board: Me and Grandma Playing Backgammon",
    "For the ASMR Community: Extended Cuts of Picking My Beard",
    "Eating a Big Bowl of Pomegranate Seeds with a Spoon")


for title in asmr:
    posts.find_one_and_update({'title': {"$regex": title,"$options":'i'}},{'$push':{'tag':'asmr'}})
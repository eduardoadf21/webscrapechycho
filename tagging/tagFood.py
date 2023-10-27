from pymongo_get_database import get_database

chychoVault = get_database()
posts = chychoVault["posts3"]

food = (
    "Yearly Liqueur Cabinet Cleaning & Sampling, Let's Relax [ASMR, Male, Soft-Spoken, Drinking, Recipe]",
    "Grape Harvest From Our Patio Garden Today",
    "Making Blackberry Jam, Cooking Live Stream [How to Recipe, ASMR, Soft-Spoken Male in the Kitchen]",
    "Cooking Live Stream: Let's Make Some Plum Jam [ASMR, Recipe, How to Make, Canning, Jarring]",
    "Cooking Live Stream: Beef Pork Ribs, Armenian Persian Funeral Halva [How To Make, Food Recipe, ASMR]",
    "Making Cornelian Cherry and Quince Liqueur [How to Recipe, ASMR]",
    "Harvesting Hops, Three Short Video Clips [ASMR]",
    "Let's Make Some Homemade Liqueur: Grape, Plum and Blackberry - Easy How to Recipe [ASMR]",
    "Making Blackberry Jam Live Stream [How to, Recipe, Relaxing Cooking ASMR, Soft-Spoken, Male, 2022]",
    "Trimming Cannabis Plants in Our Patio Garden & Talking about Life [ASMR, Male, Soft-Spoken]",
    "Harvesting Cannabis from Our Patio Garden [ASMR, Growing Plants]",
    "Two Short Video Segments: Harvesting Tobacco & Hops",
    "Chilling & Sampling Liqueurs in Our Patio Garden [ASMR, Drinking, Open Discussion, Recipes, Relax]",
    "Live Stream Open Discussion Held on March 16 on Exercise, Fitness, Food, Diet, Health and Comic Books [ASMR Advice]",
    "Cooking Live Stream: Beef Stroganoff with Fries [Family Recipe, Armenian/Persian, How to ASMR]",
    "Jarring 70 Pounds of Honey [ASMR]",
    "Cooking Live Stream: Chicken Curry and Persian Barberry Rice Dish/Casserole [ASMR, Iranian Recipe]",
    "Cooking Live Stream: Making Hamburgers & Fries, Talking about Books & Life [ASMR, Armenian Recipe]",
    "Cooking Live Stream: Persian Lentil Rice Dish with Lamb & Tahdig/Tadeek [ASMR, Recipe, How to Make]",
    "Liqueur Cabinet Cleaning & Sampling, Homemade Recipe, Taste Test [ASMR, How to Make, Relax, Chill]",
    "Cooking Live Stream: Making Armenian/Persian Kuku (Kookoo) & Talking about Nostalgia [ASMR, Recipe]",
    "Making Strawberry Liqueur in our Patio Garden [ASMR, Soft-Spoken, How to, Recipe, Nature, Homestead]",
    "Morning in Our Patio Garden Cleaning Strawberries for Making Jam & Prepping Unripened Grapes [ASMR]",
    "Morning Harvest from our Patio Garden: Suckering Tomato Plants & Harvesting Unripe Grapes [ASMR]",
    "Let's Harvest Grapes, Greens & Herbs from Our Patio Garden [ASMR]",
    "Let’s Make Some Fruit Liqueur (Begins at 28:01) & Top-up Older Bottles (Begins at 15:36) [ASMR, How to, Recipe]",
    "Let's Have Breakfast Together on Our Garden Patio [ASMR, Male, Soft-Spoken, Eating, Food]",
    "Cooking Live Stream: Armenian/Persian Dolma Recipe, Mixed & Grape Vine Leaves, How to, Dolmeh [ASMR]",
    "Harvesting Greens & Herbs from the Garden Patio: Mint, Parsley, Basil, Lettuce, Arugula [ASMR Food]",
    "Transplanting Seedlings for Our Garden Patio [ASMR, How to]",
    "Harvesting Grape Leaves from Our Patio Garden: Making Dolmas, P1 [ASMR, Birds Singing, Soft-spoken]",
    "Cooking Live Stream: Persian Eggplant Stew, Khoresh Bademjan & Rice, Family Recipe [How to Make]",
    "Liqueur Cabinet Spring Cleaning, Maintaining, Sampling & Making - ASMR, How to, Recipe [See Note]",
    "Cooking Live Stream: chycho Burgers, Chicken Broth, Rice Dish, Family Hamburger Recipe [How to Make]",
    "Let’s Make Some Lamb Stew: Cooking Live Stream and Open Discussion [Recipe, How to ASMR]",
    "Let's Wrap the Presents We're Giving Our Loved Ones for the Holidays [ASMR]",
    "How to Make Cornelian Cherry Liqueur, and Topping-Up the Lemon Liqueur [ASMR]",
    "Making Blackberry & Pineapple Liqueur, & Topping-Up the Rest of the Bottles [ASMR, Collection]",
    "Making 18.25 Liters of Crab Apple Butter During a 6.5 Hour Cooking Live Stream [How to ASMR]",
    "Let's Make Some Apple Sauce, Applesauce Recipe: How to Cooking Live Stream [ASMR]",
    "Let's Make Blackberry Jam: How to Cooking Live Stream, Recipe [ASMR]",
    "Making Homemade Blackberry & Pineapple Liqueur (Intro Begins at 22:35, Making Begins at 50:00) - How to, Recipe, Show & Tell, ASMR",
    "Let's Make Some Plum Jam, Lots of Plum Jam, Recipe, How to Cooking Live Stream [ASMR]",
    "Let's Harvest Some Black Currants and Talk about Censorship [ASMR]",
    "Jarring Dried Spring Mint [ASMR]",
    "Hanging Mint to Dry [ASMR]",
    "Gluten Free Persian Kuku (Kookoo): Recipe, How to Cooking Live Stream, Vegetarian",
    "Let's Make Gluten Free Pancakes and Talk about Life (Recipe, How To, Live Stream)",
    "Mom's Borscht Recipe: Let's Make Some Power Food, a Cooking Live Stream (Homemade Soup, How to)",
    "Cooking Live Stream: Persian Cherry Rice Chicken Casserole, Kuku, Cranberry Sauce (Recipe, How to)",
    "Let's Make Some Pomegranate Liqueur: Tasting Homemade Liqueurs, How to Make, Recipe [ASMR]",
    "Eating Fruit Salad: Pomegranate Seeds, Kiwi, Persimmons, Hemp Hearts, Mulberries & Cacao Nibs [ASMR]",
    "Cooking Live Stream: How to Use Dried Mint in Food & Drink, Multiple Dishes Recipe, Eating Persimmon",
    "Jarring 38 Pounds of Honey: ASMR Math",
    "How to Make Homemade Liqueur: Let Me Show You My Liqueur Collection",
    "Jarring Dried Mint",
    "Philosophy and Armenian Donuts: Let's Make Deep Fried Pancakes and Talk about Life (How to, Recipe)",
    "Let’s Make Some Food: Maple Syrup Brussels Sprouts Dish and Coconut Chocolate Chip Macaroon Cookies",
    "Let’s Make Some Food: Liver and Onions, Lamb Loin Chops, and Pan Fried Potatoes (How to, Recipe)",
    "Philosophy and Pancakes: Let's Make Pancakes and Talk about Life",
    "How to Make Persian Kookoo (Kuku) and a Sweet Rice Dish - Vegetarian Recipe",
    "Let's Make Some Power Food",
    "Let's Make Some Honey Chocolate Chip Cookies",
    "ASMR Math: How to Make Tea: 5 Ingredients, 31 Blends, Two Systems, Binary String, Pascal's Triangle, Binomial Theorem, Combinatorics, 5 Choose 1 to 5",
    "How to Make and Eat Crab Apple Butter, Crabapple Spread")

for title in food:
    posts.find_one_and_update({'title': title},{'$push':{'tag':'food'}})
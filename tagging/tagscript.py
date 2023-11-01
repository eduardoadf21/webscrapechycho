from pymongo_get_database import get_database

chychoVault = get_database()
posts = chychoVault["posts6"]

posts.find_one_and_update({'title': 'About Page'},{'$push': {'tag': 'about'}})
posts.find_one_and_update({'title': 'Mathematics: Finding What You Need'},{'$push': {'tag': 'finding_math'}})
posts.find_one_and_update({'title': "Math in Real Life: Table of Contents"},{'$push': {'tag':'real_math'}})
posts.find_one_and_update({'title': "ASMR Math: Introduction and Table of Contents "},{'$push': {'tag':'asmr_math'}})
posts.find_one_and_update({'title': "All About Comic Books: Readings, Reviews and Recommendations, Comic Book Hauls, Framings, Collections and Articles"},{'$push': {'tag':'all_about_comics'}})
posts.find_one_and_update({'title': {"$regex": "Support chycho","$options":'i'}},{'$push':{'tag':'support'}})
posts.find_one_and_update({'title': {"$regex": "the mathematics of economics","$options":'i'}},{'$push':{'tag':'economics_math'}})

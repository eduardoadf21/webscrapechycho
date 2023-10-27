from pymongo_get_database import get_database

chychoVault = get_database()
posts = chychoVault["posts3"]

book_club = ("Four Video Segments: Reading 21 Books, God's Equation, Tao of I Ching and The Complete Golden Dawn [ASMR]",
"Reading Book Excerpts, Part 3: The Real Anthony Fauci, Beyond the Green Zone, Mere Christianity [ASMR]",
"Reading Book Excerpts, Part 2: Dragon Wing, Perpetual War for Perpetual Peace, Wilhelm Reich in Hell [ASMR]",
"Reading Book Excerpts, Part 1: God's Equation, The Tao of I Ching, The Complete Golden Dawn [ASMR]",
"Two Video Segments: Book Haul and Reading: The Essential Psychedelic Guide by D.M. Turner [ASMR]",
"""Ketamine from "The Essential Psychedelic Guide" by D.M. Turner: Table of Contents & Reading Excerpt""",
"""ASMR Book Club: Reading Excerpts from Terence McKenna's “Food of the Gods" - Full Live Stream""",
"""Ten Excerpts from Our Live Stream Reading of Terence McKenna's “Food of the Gods": First Four and Last Six""",
"""ASMR Book Reading: "Salvinorin: The Psychedelic Essence of Salvia Divinorum" by D.M. Turner (Part 3)""",
"""ASMR Book Reading: "Salvinorin: The Psychedelic Essence of Salvia Divinorum" by D.M. Turner (Part 2)""",
"""ASMR Book Reading: "Salvinorin: The Psychedelic Essence of Salvia Divinorum" by D.M. Turner (Part 1)""",
"Physics Textbook Recommendations: How to Study and Learn Physics [ASMR]",
"What to Do When Packing Books for Storage: How to Prevent Damage from Humidity (LPT)",
"Imagination Enhancement Is One of the Main Appeals of Science-fiction and Fantasy: Explore the Limits of Human Understanding and Creativity",
"Book Club: Reading Excerpts from 'The Mass Psychology of Fascism' by Wilhelm Reich [ASMR]",
"ASMR Show & Tell: Math, Physics & Construction Book Collection, Music, Movies, Games, Toys, Unboxing",
"Ron Paul, a Roman among Greeks: The Meaning of Nassim Nicholas Taleb's Book Dedication for Skin in the Game [Political ASMR]",
"Ralph Nader, a Greco-Phoenician Saint: The Meaning of Nassim Nicholas Taleb's Book Dedication for Skin in the Game [Political ASMR]",
"Regarding Bankers and Decentralization: Decentralization Reduces Structural Asymmetries: Excerpts from Nassim Nicholas Taleb’s Skin in the Game",
"Interventionistas, Transferring Risk, War and Libya: Excerpts from Nassim Nicholas Taleb’s Skin in the Game [ASMR]",
"Censorship and The Constitution of the United States, Free Speech: Excerpts from Nassim Nicholas Taleb’s Skin in the Game [ASMR]",
"Silver Rule vs. Golden Rule: How to Treat Others, The Essence of Morality [ASMR]",
"The Hardest Thing I've Had to Do as a Math Tutor: Learning, Schools, Centralized Education [ASMR]",
"""Book Club: "Skin in the Game: Hidden Asymmetries in Daily Life" - Nassim Nicholas Taleb [ASMR]""",
"Reading Raymond Feist's The Riftwar Saga, Darkness At Sethanon, Creation [ASMR]",
"Reading Excerpts from Krishnamurti's 'Education and the Significance of Life' [ASMR]",
"Review of Raymond Feist's Magician: Apprentice and Master, The Riftwar Saga [Happy ASMR]",
"ive Books That Have Influenced My Political Perspective over the Years [ASMR]",
"ar Is A Racket by Major General Smedley Butler [ASMR]",
"cience Fiction and Fantasy Book Recommendations: Let Me Show You My Collection [ASMR]",
"et Me Show You My Math Book Collection [ASMR]",
" Book Recommendations: Some of My Most Influential Reads [ASMR, Best of]",
"ow to Study: Tip #5: 20 Steps to Reading a Textbook (Language of Math #161 - ASMR)",
"SMR Math: How to Study: Tip #5: How to Read a Textbook",
"anguage of Mathematics II (58): Book Recommendations (Part 2 of 2)")

for title in book_club:
    posts.find_one_and_update({'title': {"$regex": title}},{'$push':{'tag':'book_club'}})
    #posts.find_one_and_update({'title': title},{'$push':{'tag':'book_club'}})
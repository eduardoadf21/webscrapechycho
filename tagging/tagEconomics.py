from pymongo_get_database import get_database

chychoVault = get_database()
posts = chychoVault["posts3"]


economics = ("The Mathematics of Economics",
            "The Next Phase of the Economic Collapse Has Begun, Be Prepared: I’m Short the Market, Here Is Why",
            "the mantra",
            "Fragmentation of Bitcoin Community Begins after the Collapse of Mt. Gox and Secondmarket’s Wall Street Exchange Proposal",
            "bitcoin bubble",
            "Government Shutdown and Appointment of Janet Yellen Guarantees Flow of Funds to Wall Street: They are reducing “two-thirds of this country to subsistence level”, Chris Hedges",
            "An example of how the surveillance state is hurting the U.S. economy: Ladar Levison confirms that he will be forced to move his business overseas",
            "The Surveillance State Killed BlackBerry, and the Same Fate Awaits Other Tech Giants",
            "The 2005 Bankruptcy Bill: Knowing a Financial Crisis Was Imminent, Banks Lobbied Government to Pass Laws to Preserve Their Wealth",
            "Why Stocks Have Risen: Stimulus, Stimulus, and Indefinite-Stimulus, i.e., Transfer of Wealth from Main Street to Wall Street",
            "three game changers",
            "Recolonization of Africa, a Symptom of Our Addiction to Growth: Differential Accumulation, Why GDP Growth Rates Influence Foreign Policy",
            "precedent set")

for title in economics:
    posts.find_one_and_update({'title': {"$regex":title,"$options":'i'}},{'$push':{'tag':'economics'}})
from itertools import permutations

unkown_badge_types = [ "Speaker", "Artist", "Creator", "Press"]
jenny = {'8': "Vendor", '6': "", '7': "", '5': "", '3': "Human", '0': "", '9': "Goon"}
url = "http://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/"
badge_perms = list(permutations(unkown_badge_types, len(unkown_badge_types)))
for x in badge_perms:
    test = jenny["8"] + x[0] + x[1] + x[2] + jenny["3"] + x[3] + jenny["9"]
    print(url+test)

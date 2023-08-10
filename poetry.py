from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over",
"within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def makePoem():
    n1 = choice(nouns)
    n2 = choice(nouns)
    while n2 == n1:
        n2 = choice(nouns)
    n3 = choice(nouns)
    while n3 == n1 or n3 == n2:
        n3 = choice(nouns)
    
    v1 = choice(verbs)
    v2 = choice(verbs)
    while v2 == v1:
        v2 = choice(verbs)
    v3 = choice(verbs)
    while v3 == v1 or v3 == v2:
        v3 = choice(verbs)

    adj1 = choice(adjectives)
    adj2 = choice(adjectives)
    while adj2 == adj1:
        adj2 = choice(adjectives)
    adj3 = choice(adjectives)
    while adj3 == adj1 or adj3 == adj2:
        adj3 = choice(adjectives)

    adv = choice(adverbs)

    prep1 = choice(prepositions)
    prep2 = choice(prepositions)
    while prep2 == prep1:
        prep2.choice(prepositions)

    if "aeiou".find(adj1[:1]) != -1:
        article = "An"
    else:
        article = "A"


    poem = "{} {} {}\n\n".format(article, adj1, n1)
    poem = poem + "{} {} {} {} {} the {} {}\n".format(article, adj1, n1, v1, prep1, adj2, n2)
    poem = poem + "{}, the {} {}\n".format(adv, n1, v2)
    poem = poem + "the {} {} {} a {} {}".format(n2, v3, prep2, adj3, n3)
    return poem

print(makePoem())
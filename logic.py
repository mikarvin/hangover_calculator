def get_hangover(drinks):
    if drinks >= 10:
        verdict = "Was it worth it? Even for me thats rough."
        recc = ["Go to church."]
    elif drinks >= 6:
        verdict = "Did she text you back?"
        recc = ["A Döner", "2L water", "nap and... also a painkiller... 500mg painkiller if the headache is there."]
    elif drinks >= 3:
        verdict = "Little saturday or what?"
        recc = ["200mg Ibuprofen", "glass of water", "and a BigMac."]
    elif drinks >= 1:
        verdict = "Low tolerance huh?"
        recc = ["Have some water", "do some pushups."]
    else:
        verdict = "Why are you even here?"
        recc = ["Go find a bar."]
    return verdict, recc

v, r = get_hangover(5)
print(v)
print(r)

    
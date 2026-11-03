def get_hangover(drinks):
    if drinks >= 30:
        verdict = "You are a legend."
        recc = ["However, youre either lying or need a hospital."]
    elif drinks >= 10:
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
    elif drinks == 0:
        verdict = "You are a good person."
        recc = ["Go find a bar or something."]
    else:
        verdict = "Hows that possibe?"
        recc = ["Man works at the place."]
    return verdict, recc


    
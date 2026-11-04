def calculate_score(beers, shots, cocktails, wines):
    score = beers * 0.3 + shots * 1.1 + cocktails * 0.8 + wines * 0.5
    return round(score, 1)


def get_hangover(score):
    if score >= 15:
        verdict = "You are a legend."
        recc = ["However, youre either lying or need a hospital."]
    elif score >= 6:
        verdict = "Was it worth it? Even for me thats rough."
        recc = ["Go to church."]
    elif score >= 4:
        verdict = "Did she text you back?"
        recc = ["A Döner", "2L water", "nap and... also a painkiller... 500mg painkiller if the headache is there."]
    elif score >= 2.5:
        verdict = "Little saturday or what?"
        recc = ["200mg Ibuprofen", "glass of water", "and a BigMac."]
    elif score > 0:
        verdict = "Low tolerance huh?"
        recc = ["Have some water", "do some pushups."]
    elif score == 0:
        verdict = "You are a good person."
        recc = ["Go find a bar or something."]
    else:
        verdict = "Hows that possibe?"
        recc = ["Man works at the place."]
    return verdict, recc

    
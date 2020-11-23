def word_score(alpha_chars):
    list_alpha_classification = [["aeilnorstu", 1], ["dg",2], ["bcmp",3], ["fhvwy",4], ["k",5], ["jx",8], ["qz",10]]
    chars_mapper = {}
    for classes in list_alpha_classification:
        for alpha in classes[0]:
            chars_mapper[alpha] = classes[1]
    score = 0
    for chars in alpha_chars:
        score += chars_mapper[chars.lower()]
    return score


if __name__ == "__main__":
    score_counted = word_score("fortune")
    print(score_counted)


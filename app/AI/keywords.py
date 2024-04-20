import spacy


def search_keywords(keywords, text):
    nlp = spacy.load('en_core_web_lg')
    tokens = nlp(text)
    tokenized_keywords = []

    for word in keywords:
        tokenized_keywords.append(nlp(word))

    length_of_keywords = len(tokenized_keywords)
    found_keywords = 0

    for token in tokens:
        for index, word in enumerate(tokenized_keywords):
            sim = word.similarity(token)
            if sim > 0.8:
                print(token, word, word.similarity(token))
                found_keywords += 1
                tokenized_keywords.pop(index)

    return found_keywords / length_of_keywords


print(search_keywords(keywords=["Machine Learning", "Computer Vision", "Reinforcement Learning"], text="This is a bird. Machine Learning is my passion. I made a project using Computer Vision."))

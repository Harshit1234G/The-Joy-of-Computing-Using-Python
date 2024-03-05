import nltk
import os

os.chdir("E:\Python\joy of computing using python\dataset_estilometria\dados")

def read_files(num: list) -> str:
    strings = ""
    for n in num:
        with open(f"federal_{n}.txt", encoding='utf-8') as f:
            strings += f.read()

    return strings

papers = {
    "branco": [0, 2, 3],
    "chagas": [1,6,7],
    "castilho": [4,8,14],
    "alencar": [5,9,10],
    "assis": [11,12,13]
}

federalist_by_author = {author: read_files(num) for author, num in papers.items()}

for author in papers.keys():
    tokens = nltk.word_tokenize(federalist_by_author[author])

    tokens = [i for i in tokens if i.isalpha()]

    length_dist = nltk.FreqDist(map(len, tokens))

    length_dist.plot(15, title=author)
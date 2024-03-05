import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

xl = pd.ExcelFile('data.xlsx')
df = xl.parse(xl.sheet_names[0])['Sentences']

sid = SentimentIntensityAnalyzer()
for data in df:
    ss = sid.polarity_scores(data)
    print(data)
    for key, value in ss.items():
        print(f"{key} = {value}")
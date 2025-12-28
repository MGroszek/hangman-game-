# Aufgabe 1
"""
a = str(input())
b = str(input())

if a < b:
    print(a, " < ", b)
else:
    print(a, " > ", b)
"""  # Shift + Option + A

# Aufgabe 2
from textblob import TextBlob


reviews = [
    "This product exceeded my expectations and is truly outstanding!",
    "Unfortunately, the quality was disappointing and not worth the price.",
    "An average experience, nothing particularly special but it gets the job done.",
    "Fantastic service and a product that lives up to its promises!",
    "I wouldn't recommend this to anyone; it fell apart after one use.",
    "The functionality is severely lacking; I'm not satisfied at all.",
    "A solid purchase overall, with minor issues that are easily overlooked.",
    "Terrible, the whole thing feels like a cheap knock-off.",
    "I'm delighted with the results; it's exactly what I needed!"
]

for review in reviews:
    print("REVIEW:", review)          # prosty test
    blob = TextBlob(review)
    print("SENTIMENT:", blob.sentiment)
    print("POLARITY:", blob.sentiment.polarity)
    print("----")

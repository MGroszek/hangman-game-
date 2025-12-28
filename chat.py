from textblob import TextBlob
reviews = ["This product exceeded my expectations and is truly outstanding!",
           "Unfortunately, the quality was disappointing and not worth the price.",
           "An average experience, nothing particularly special but it gets the job done.",
           "Fantastic service and a product that lives up to its promises!",
           "I wouldn't recommend this to anyone; it fell apart after one use.",
           "The functionality is severely lacking; I'm not satisfied at all.",
           "A solid purchase overall, with minor issues that are easily overlooked.",
           "Terrible, the whole thing feels like a cheap knock-off.",
           "I'm delighted with the results; it's exactly what I needed!"
           ]


negative_reviews = (
    review
    for review in reviews
    if TextBlob(review).sentiment.polarity < 0
)

for r in negative_reviews:
    print(r)

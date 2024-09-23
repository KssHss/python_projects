import string 

# to define the function
def analyze_reviews(reviews):

  total_rating = 0
  word_count = {}
  monthly_reviews = {}
  STOPWORDS = set(["the", "and", "a", "to", "of", "in", "but", "some", "is", "it", "i", "for", "on", "with", "was"])
  num_reviews = len(reviews)

  for review in reviews:

    # to calculate the average rating 
    total_rating += review["rating"]
    average_rating = round(total_rating / num_reviews, 2)  

    # to extract the most common word
    words = review["review"].lower().split()
    for word in words:
      if word not in STOPWORDS:
        word_count[word] = word_count.get(word, 0) + 1
   
    # Month with most review submitted
    month = review["date"][-5:-3] 
    monthly_reviews[month] = monthly_reviews.get(month, 0) + 1

  month_name = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July"}   # to create a dictionary to extract the month name from the month number
  most_reviews_month = month_name[max(monthly_reviews, key=monthly_reviews.get)]
  
  max_word_count = max(word_count.values()) 
  most_common_words = sorted([word for word, count in word_count.items() if count == max_word_count])
  most_common_words_str = ", ".join(most_common_words)

  # to print the outputs: 
  print(f"Average Rating: {average_rating}")
  print(f"Most Common Words: {most_common_words_str}")
  print(f"Month with Most Reviews: {most_reviews_month}")
  

reviews = [
  {"id": 1, "rating": 5, "review": "The coffee was fantastic.", "date": "2022-05-01"},
  {"id": 2, "rating": 4, "review": "Excellent atmosphere. Love the modern design!", "date": "2022-05-15"},
  {"id": 3, "rating": 3, "review": "The menu was limited.", "date": "2022-05-20"},
  {"id": 4, "rating": 4, "review": "Highly recommend the caramel latte.", "date": "2022-05-22"},
  {"id": 5, "rating": 4, "review": "The seating outside is a nice touch.", "date": "2022-06-01"},
  {"id": 6, "rating": 5, "review": "It's my go-to coffee place!", "date": "2022-06-07"},
  {"id": 7, "rating": 3, "review": "I found the Wi-Fi to be quite slow.", "date": "2022-06-10"},
  {"id": 8, "rating": 3, "review": "Menu could use more vegan options.", "date": "2022-06-15"},
  {"id": 9, "rating": 4, "review": "Service was slow but the coffee was worth the wait.", "date": "2022-06-20"},
  {"id": 10, "rating": 5, "review": "Their pastries are the best.", "date": "2022-06-28"},
  {"id": 11, "rating": 2, "review": "Very noisy during the weekends.", "date": "2022-07-05"},
  {"id": 12, "rating": 5, "review": "Baristas are friendly and skilled.", "date": "2022-07-12"},
  {"id": 13, "rating": 3, "review": "It's a bit pricier than other places in the area.", "date": "2022-07-18"},
  {"id": 14, "rating": 4, "review": "Love their rewards program.", "date": "2022-07-25"},
]

# to call the function 
analyze_reviews(reviews)
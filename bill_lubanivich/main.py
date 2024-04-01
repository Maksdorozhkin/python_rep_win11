# оператор присваивания (морж) :=

tweet_limit = 280
tweet_string = "Blah" * 50
dif = tweet_limit - len(tweet_string)
if dif >= 0:
    print("Bla bla bla")


# то же самое но с оператором присваивания

tweet_limit = 280
tweet_string = "Blah" * 50
if dif := tweet_limit - len(tweet_string) >= 0:
    print("Bla bla bla")

"""Restaurant rating lister."""
score_rate = open("scores.txt")
restaurant_rating = {}
def make_dict_restaurant_ratings (score_rate):
    
    for line in score_rate:
        line = line.rstrip()
        restaurant, rating= line.split(":")
        restaurant_rating[restaurant] = int(rating)
        # for score in rating: 
            # restaurant_rating[score] = restaurant_rating.get(score,0) + 1
    return restaurant_rating 

def add_restaurant_rating(restaurant_rating):
    restaurant= input("Please input a Restaurant Name: ")
    rating = input("Please input a rating: ")

    restaurant_rating[restaurant] = float(rating) 

print(add_restaurant_rating(restaurant_rating)) 

restaurant_rating = make_dict_restaurant_ratings(score_rate)

for restaurant, rating in sorted(restaurant_rating.items()):

    print(f'{restaurant}:{rating}')


# print(add_restaurant_rating(restaurant_rating)) 



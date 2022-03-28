#Converting the dataset into an implicit feedback dataset
# As discussed earlier, we will train a recommender system using implicit feedback.
# However, the MovieLens dataset that we are using is based on explicit feedback. 
# To convert this dataset into an implicit feedback dataset, we’ll simply binarize the ratings
# and convert them to ‘1’ (i.e. positive class). The value of ‘1’ represents that the user has interacted with the item
train_ratings.loc[:, 'rating'] = 1

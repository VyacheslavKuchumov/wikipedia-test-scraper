from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.Movies

wiki_money_collection = db.movieMoneys
wiki_review_collection = db.movieReviews

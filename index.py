from pymongo import MongoClient

client = MongoClient('mongodb+srv://jbuitron:6RJ975n5zin!HE4@clustertest.x4v3gze.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest&connectTimeoutMS=300000')

db = client['ClusterTest']
collection = db['movies']

movie = {'title':'Matrix', 'year': 2003, 'category': 'action'}

insert_movie = collection.insert_one(movie)
print('!!!!!!!!!!', insert_movie.inserted_id)
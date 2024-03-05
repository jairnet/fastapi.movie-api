from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

from models import Movie

# MongoDB connection URL
username = 'jbuitron'
password = 'zabduq-ruqcy1-Kekduj'
# uri = 'mongodb+srv://' + username + ':' + password + '@clustertest.x4v3gze.mongodb.net/?retryWrites=true&w=majority'
uri = 'mongodb+srv://jbuitron:zabduq-ruqcy1-Kekduj@clustertest.x4v3gze.mongodb.net/'


async def conection_mongo():
    try:
        client = AsyncIOMotorClient(uri)
        database = client['ClusterTest']
        collection = database['movies']
        return collection
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")

async def get_all_movies():
    collection = await conection_mongo()
    movies = []
    cursor = collection.find({})
    async for document in cursor:
        movies.append(Movie(**document))
    return movies

async def test_connection():
    collection = await conection_mongo()
    cursor = collection.find({})
    async for document in cursor:
        tmp = Movie(**document)
        print(">>>>>>>>",tmp)
    # insert_movie = await collection.insert_one(movie)
    # print ("insert:::::", insert_movie.inserted_id)

async def create_movie(movie):
    collection = await conection_mongo()
    new_movie = await collection.insert_one(movie)
    created_movie = await collection.find_one({"_id": new_movie.inserted_id})
    return created_movie

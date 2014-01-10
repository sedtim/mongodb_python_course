
import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
database = connection.exam

albums = database.albums
images = database.images

print('# of albums: {}'.format(albums.count()))
print('# of images: {}'.format(images.count()))

image_id_set = []

for albumJSON in albums.find():
    image_id_set += albumJSON['images']
image_id_set = set(image_id_set)

orphan_count = 0
for imageJSON in images.find():
    image_id = imageJSON['_id']
    if image_id not in image_id_set:
        orphan_count += 1

print(images.count() - orphan_count) 

num_kittens_0 = 0   # before dropping
num_kittens_1 = 0   # after dropping
for imageJSON in images.find():
    if "kittens" in imageJSON["tags"]:
        num_kittens_0 += 1
        
        image_id = imageJSON['_id']
        if image_id in image_id_set:
            num_kittens_1 += 1

print('num_kittens_0: {}'.format(num_kittens_0))
print('num_kittens_1: {}'.format(num_kittens_1))
        


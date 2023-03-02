import pymongo as pymongo
from pymongo.server_api import ServerApi

def main():




def insert_to_db(df):
    client = pymongo.MongoClient("mongodb+srv://anardimon:aEAD5Xu6UpVbpQe@cluster0.xh51ljq.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    mng_db = client['ADAI_db']
    collection_name = 'ClothingItems'
    db_cm = mng_db[collection_name]
    data_json = json.loads(df.to_json(orient='records'))

    clothing_items = [{"_id": 1, "item_name": "Black Shirt", "actor":"Chandler", "source": "Ikea", "price": 99, "image_name": "black_buttoned_shirt.jpg"},
                      {"_id": 2, "item_name": "fridge", "actor":"", "price": 1099, "source": "Vintage Refrigirators", "image_name": "retrooriginalfridge-white.jpg"},
                      {"_id": 3, "item_name": "sofa", "actor":"", "price": 2099, "source": "ZARA", "image_name": "Sofa_Rachel_Home.jpg"},
                      {"_id": 4, "item_name": "Black Suit Jacket", "price": 99, "source": "Catro", "actor":"Rachel", "image_name": "RachelSuitJacket.jpg"},
                      {"_id": 5, "item_name": "Sleeveless black shirt", "price": 99, "source": "H&M", "actor":"Julie", "image_name": "Sleeveless_black_shirt.jpg"},
                      {"_id": 6, "item_name": "Sleeveless flower short", "price": 99, "source": "Adika", "actor":"Monika", "image_name": "lina-floral-blouse.jpg"},
                      {"_id": 7, "item_name": "Black sweater", "actor":"Joey", "price": 99, "source": "Castro", "image_name": "black_sweater.jpg"},
                      {"_id": 8, "item_name": "Dinning table", "actor":"Joey", "price": 99, "source": "Ikea", "image_name": "dinning_table.jpg"},
                      {"_id": 9, "item_name": "Day to day shirt", "actor":"Chandler", "price": 99, "source": "Renuar", "image_name": "day_to_day_striped_purple_shirt.jpg"},
                      {"_id": 10, "item_name": "Black sweater", "actor":"Pheobe", "price": 56, "source": "ZARA", "image_name": "vneck_tiedown_shirt.jpg"},
                      {"_id": 11, "item_name": "Red shirt", "actor":"Ross", "price": 69, "source": "Fox", "image_name": "RossShirtRed.jpg"},
                      {"_id": 12, "item_name": "Grey suit", "actor":"Ross", "price": 159, "source": "ZARA", "image_name": "RossSuit.jpg"},
                      {"_id": 13, "item_name": "Summer dress", "actor":"Pheobe", "price": 39, "source": "ZARA", "image_name": "PheobeBlueDress.jpg"},
                      {"_id": 14, "item_name": "Blue buttoned shirt", "actor":"Rachel", "price": 99, "source": "ZARA", "image_name": "Blue_buttoned_shirt.jpg"},
                      {"_id": 15, "item_name": "Black vneck shirt", "actor":"Monika", "price": 45, "source": "Castro", "image_name": "black_vneck_shirt.jpg"},
                      {"_id": 16, "item_name": "Stripped shirt", "actor":"Joey", "price": 49, "source": "Renuar", "image_name": "Horizontal_grey_shirt.jpg"},
                      {"_id": 17, "item_name": "White buttoned shirt", "actor":"Ross", "price": 99, "source": "ZARA", "image_name": "white_shirt.jpg"},
                      {"_id": 18, "item_name": "Black short sleeve buttoned shirt", "actor":"Julie", "price": 199, "source": "Renuar","image_name": "short_black_buttoned_shirt.jpg"},
                      {"_id": 19, "item_name": "Brown Vest", "actor":"Julio", "price": 199, "source": "Fox","image_name": "brown_vest.jpg"},
                      {"_id": 20, "item_name": "Red buttoned shirt", "actor":"Chandler", "price": 299, "source": "H&M","image_name": "red_short_sleeve_buttoned_shirt.jpg"},
                      {"_id": 21, "item_name": "Vneck shirt", "actor":"Pheobe", "price": 99, "source": "Castro","image_name": "light_blue_vneck.jpg"},
                      ]
    x = mycol.insert_many(clothing_items)

if __name__ == '__main__':
    main()
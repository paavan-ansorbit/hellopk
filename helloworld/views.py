from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
from . import models
import json
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId
from hellopk.settings import env

# Create your views here.

# MONGO_URI = env("MONGO_URI")

# client = MongoClient(MONGO_URI)

# dbname = client['django']
# userCollection = dbname['user']

# user_data_input = {
#     "name": "paavan",
#     "email" : "paavan.khunt@ansorbit.com",
#     "address" : "Ahmedabad",
#     "phone" : "1234567890"
# }

# # create user using User model and add to mongodb

# def get_user(request): 
#     users = []
#     user_details = userCollection.find({})
#     for doc in user_details:
#         doc['_id'] = str(doc['_id'])
#         users.append(doc)
#     return JsonResponse( {"data":users})



# @csrf_exempt    
# def get_user_by_id(request, id):
#     if request.method=='GET':
#         userId = ObjectId(id)
#         users = []
#         user_details = userCollection.find({"_id":userId})
#         for doc in user_details:
#             doc['_id'] = str(doc['_id'])
#             users.append(doc)
#         return JsonResponse( {"data":users})

#     else:
#         return HttpResponse("Invalid Request")

# @csrf_exempt 
# def create_user(request):
#     if request.method=='POST':
#         received_json_data=json.loads(request.body)
#         print(received_json_data)
#         user = models.User(
#             name = received_json_data["name"],
#             email = received_json_data["email"],
#             address = received_json_data["address"],
#             phone = received_json_data["phone"]
#         )
#         # user.save()
#         userCollection.insert_one(json.loads(user.__str__()))
#         return JsonResponse(json.loads(user.__str__()))
#     else:
#         return HttpResponse("Invalid Request")
        
# @csrf_exempt
# def update_user(request, id):
#     if request.method=='PUT':
#         users = []
#         try: 
#             userId = ObjectId(id)
#             received_json_data=json.loads(request.body)
#             update = userCollection.update_one({"_id":userId}, {"$set": received_json_data})
#             print(update.raw_result, type(update))

#             user_details = userCollection.find({"_id":userId})
#             for doc in user_details:
#                 doc['_id'] = str(doc['_id'])
#                 users.append(doc)
#             return JsonResponse( { "data":users})
#         except ValueError:
#             return HttpResponse("Invalid Request")

#     else:
#         return HttpResponse("Invalid Request")

# @csrf_exempt 
# def delete_user(request, id):
#     if request.method=='DELETE':
#         users = []
#         try: 
#             userId = ObjectId(id)
#             userCollection.delete_one({"_id":userId})
#             user_details = userCollection.find({})
#             for doc in user_details:
#                 doc['_id'] = str(doc['_id'])
#                 users.append(doc)
#             return JsonResponse( { "data":users})
#         except ValueError:
#             return HttpResponse("Invalid Request")
#     else:
#         return HttpResponse("Invalid Request")
    
# @csrf_exempt
# def delete_all(request):
#     if request.method=='DELETE':
#         users = []
#         try: 
#             delete = userCollection.delete_many({})
#             print(delete.raw_result, type(delete))

#             user_details = userCollection.find({})
#             for doc in user_details:
#                 doc['_id'] = str(doc['_id'])
#                 users.append(doc)
#             return JsonResponse( {"data":users})
#         except ValueError:
#             return HttpResponse("Invalid Request")
#     else:
#         return HttpResponse("Invalid Request")

def index(request):
    return HttpResponse("Hello, world. Django App is working...")

def ping(request):
    return HttpResponse("pong🏓")

def version(request):
    return JsonResponse({"version": "1.0.0", "status": "ok"})

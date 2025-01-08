from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models.tfidf_recommendation import TFIDFRecommender
from ..models.ncf_recommendation import NCFRecommender

@api_view(['GET'])
def recommend_courses(request):
    course_title = request.GET.get('course_title', '')
    tfidf_recommender = TFIDFRecommender('path/to/courses.csv')
    tfidf_recommender.train_model()
    recommendations = tfidf_recommender.recommend_courses(course_title)
    return Response({'recommendations': recommendations})

@api_view(['POST'])
def train_ncf_model(request):
    # Assume data contains user_item interactions
    user_data = request.data.get('user_data')
    item_data = request.data.get('item_data')
    labels = request.data.get('labels')
    ncf_recommender = NCFRecommender(num_users=1000, num_items=500)
    ncf_recommender.train_model(user_data, item_data, labels)
    return Response({'status': 'Model Trained Successfully'})

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Article
from .serialzers import ArticleSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework import generics 
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class ArticleViewSet(viewsets.GenericViewset,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
	serializer_class=ArticleSerializers
	queryset=Article.objects.all()

	# def list(self,request):
	# 	articles=Article.objects.all()
	# 	serializer=ArticleSerializers(articles, many=True)
	# 	return Response(serializer.data)
	# def create(self,request):
	# 	serializer=ArticleSerializers(data=request.data)
	# 	# data['content']=str(data['content'])	 

	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data ,status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	# def retrieve(self,request,pk=None):
	# 	queryset=Article.objects.all()
	# 	article=get_object_or_404(queryset,pk=pk)
	# 	serializer=ArticleSerializers(article)
	# 	return response(serializer.data)
			

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
	serializer_class=ArticleSerializers
	queryset=Article.objects.all()

	lookup_field = 'id'
	# authentication_classes = [SessionAuthentication , BasicAuthentication]
	authentication_classes = [TokenAuthentication] 
	permission_classes = [IsAuthenticated]

	def get(self,request,id=None):
		if id:
			return self.retrieve(request)
		else:	
			return self.list(request)
	def post(self,request):
		return self.create(request)	
	def put(self,request,id=None):
		return self.update(request, id)	
	def delete(self,request,id=None):
		return self.destroy(request, id)	


class ArticleAPIView(APIView):
	def get(self,request):
		articles=Article.objects.all()
		serializer=ArticleSerializers(articles, many=True)
		return Response(serializer.data)
	def post(self,request):
		serializer=ArticleSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data ,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
class Articledetails(APIView):
	def get_object(self, id):
		try:
			return Article.objects.get(id=id)

		except Article.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	def get(self,request,id):
		article=self.get_object(id)
		serializer=ArticleSerializers(article)
		return Response(serializer.data)
	def put(self,request,id):
		article=self.get_object(id)
		serializer=ArticleSerializers(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self,request,id):
		article=self.get_object(id)
		article.delete()	
		return Response(status=status.HTTP_204_NO_CONTENT)	
 

@api_view(['GET','POST'])
def article_list(request):
	if request.method=='GET':
		articles=Article.objects.all()
		serializer=ArticleSerializers(articles, many=True)
		return Response(serializer.data)
	elif request.method=='POST':
		serializer=ArticleSerializers(data=request.data)
		# data['content']=str(data['content'])	 

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data ,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
	try:
		article = Article.objects.get(pk=pk)

	except Article.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)

	if request.method =='GET':
		serializer=ArticleSerializers(article)
		return Response(serializer.data)
 
	elif request.method == 'PUT':
		serializer = ArticleSerializers(article, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
	elif request.method =='DELETE':
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	






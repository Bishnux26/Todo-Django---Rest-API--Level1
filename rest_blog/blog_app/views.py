from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import BlogPost
from .serializers import BlogPostSer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

# Create your views here.

class BlogApi(APIView):

	def get(self, request):
		data=BlogPost.objects.all()
		ser_data=BlogPostSer(data, many=True)

		return Response({'status':200, 'payload':ser_data.data,'messages':'Getting data sucessfully !'})

	def post(self, request):
		ser_data=BlogPostSer(data=request.data)

		if ser_data.is_valid():
			ser_data.save()

			return Response({'status':201, 'payload':ser_data.data, 'messages':'Data Saved Sucessfully !'})

		else:
			return Response({'status':403, 'payload':ser_data.data, 'messages':'something went wrong !'})

	def put(self, request):
		try:
			data=BlogPost.objects.get(id=request.data['id'])
			ser_update=BlogPostSer(data, data=request.data, partial=True)
			if ser_update.is_valid():
				ser_update.save()
				return Response({'status':201, 'payload':ser_update.data, 'messages':'Data Saved Sucessfully !'})

			else:
				return Response({'status':403, 'payload':ser_update.data, 'messages':'something went wrong !'})
		except:
			return Response({'status':403, 'messages':'something went wrong !'})

	def patch(self, request):
		try:
			data=BlogPost.objects.get(id=request.data['id'])
			ser_update=BlogPostSer(data, data=request.data, partial=True)
			if ser_update.is_valid():
				ser_update.save()
				return Response({'status':201, 'payload':ser_update.data, 'messages':'Data Saved Sucessfully !'})

			else:
				return Response({'status':403, 'payload':ser_update.data, 'messages':'something went wrong !'})
		except:
			return Response({'status':403, 'messages':'something went wrong !'})

	def delete(self, request):

		try:
			id=request.GET.get('id')
			blog_delete=BlogPost.objects.get(id=id)
			blog_delete.delete()

			return Response({'status':200, 'messages':"data deleted sucessfully"})
		except:
			return Response({'status':200, 'messages':"Something Went Wrong !"})
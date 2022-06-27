from rest_framework import serializers
from .models import BlogPost

class BlogPostSer(serializers.ModelSerializer):

	class Meta:
		model=BlogPost
		fields='__all__'

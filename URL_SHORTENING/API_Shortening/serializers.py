from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["url"]


class RetrieveOriginalURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ["url", "shortcode", "createdAt", "updatedAt", "accessCount"]



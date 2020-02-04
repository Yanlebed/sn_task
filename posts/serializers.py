from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post
from likes import services as likes_services

User = get_user_model()


class PostDetailSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (

            'title', 'body', 'image', 'total_likes', 'is_fan'
        )

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` пост (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


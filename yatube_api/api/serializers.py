from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['user', 'following']

    def validate_following(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь не найден.')

        following_user = User.objects.get(username=value)

        if following_user == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя.')

        return following_user

    def validate(self, attrs):
        user = self.context['request'].user
        following_user = attrs.get('following')

        if Follow.objects.filter(user=user, following=following_user).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя.')

        return attrs

from rest_framework import serializers

from comments.models import ReplyComment, Comment


class ReplyCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReplyComment
        fields = ('user', 'comment', 'reply', 'likes', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    # reply_comment = ReplyCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'recipe', 'likes', 'created_at')

class GetCommentSerializer(serializers.ModelSerializer):
    reply_comment = ReplyCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'recipe', 'likes', 'reply_comment')


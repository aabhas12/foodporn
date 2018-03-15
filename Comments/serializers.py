from rest_framework import serializers

from Comments.models import ReplyComment, Comment


class ReplyCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReplyComment
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.reply = validated_data['reply']
        instance.save()


class CommentSerializer(serializers.ModelSerializer):
    # reply_comment = ReplyCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'recipe', 'likes')

class GetCommentSerializer(serializers.ModelSerializer):
    reply_comment = ReplyCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'recipe', 'likes', 'reply_comment')


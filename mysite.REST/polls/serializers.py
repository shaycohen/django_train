from rest_framework import serializers
from polls.models import Question

class QuestionSerializer (serializers.Serializer):
    pk = serializers.Field()
    question_text = serializers.CharField(required=True, max_length=200)
    pub_date = serializers.DateTimeField(required=True)
    

    """ Define function to handle create or update """
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.question_text = attrs.get('question_text', instance.question_text)
            instance.pub_date = attrs.get('pub_date', instance.pub_date)
            return instance

        return Question(**attrs)



class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')


from rest_framework import serializers

from courses import models


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = (
            'id',
            'description',
            'current_job',
            'created_at',
            'updated_at',
        )


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ('id', 'description', 'teachers', 'created_at', 'updated_at')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('id', 'provider', 'url')


class MaterialSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)

    class Meta:
        model = models.Material
        fields = ('id', 'title', 'description', 'videos')

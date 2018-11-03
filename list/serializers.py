from rest_framework import serializers
from list.models import Festival, Contest

class FestivalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Festival
		fields = ('ftitle', 'fhelder', 'fparticipate', 'fgenre', 'fdatestart', 'fdateend', 'faward', 'faward1', 'fhomepage', 'fdesc', 'fauthor', 'fimage', 'url', )

		
class ContestSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Contest
		fields = ('ctitle', 'cplace', 'cdesc', 'cdatestart', 'cdateend', 'clocate', 'cimage', 'url')
from django.db import models
from django.utils import timezone


class Festival(models.Model):
	ftitle = models.CharField(max_length=200) #제목
	fhelder = models.CharField(max_length=200, null=True) #주최자
	fparticipate = models.CharField(max_length=100) #참가자격
	fgenre = models.CharField(max_length=200) #장르
	fdatestart = models.DateField(null=True) #시작일
	fdateend = models.DateField(null=True) # 종료일
	faward = models.CharField(max_length=200) # 총 상금
	faward1 = models.CharField(max_length=200) # 1등 상금
	fhomepage = models.TextField(null=True) #홈페이지
	fdesc = models.TextField(null=True) #추가 설명
	fauthor = models.ForeignKey('auth.User', on_delete=models.CASCADE) #아무것도 아닙니다.
	fimage = models.ImageField(upload_to='Images/', default = 'Images/None/No-images.jpg') #이미지
	
	def __str__(self):
		return self.ftitle
	
class Contest(models.Model):
	ctitle = models.CharField(max_length=200) #제목
	cplace = models.CharField(max_length=100) #장소
	cdesc = models.TextField(null=True) #추가설명
	cdatestart = models.DateField(null=True) #시작일
	cdateend = models.DateField(null=True) #종료일
	clocate = models.CharField(max_length=300) #지역
	cimage = models.ImageField(upload_to='Images/', default = 'Images/None/No-images.jpg') #이미지

	def __str__(self):
		return self.ctitle

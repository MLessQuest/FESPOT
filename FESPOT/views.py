from django.views.generic.base import TemplateView

class FestivalView(TemplateView):
	template_name = 'festival.html'

class ContestView(TemplateView):
	template_name = 'contest.html'
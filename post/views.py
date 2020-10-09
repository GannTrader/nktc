from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home-page.html"


class PostListView(TemplateView):
    template_name = "post-page.html"


class RobotsView(TemplateView):
    template_name = "robots.txt"
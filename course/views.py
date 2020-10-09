from django.views.generic import TemplateView


class CourseView(TemplateView):
    template_name = "course-page.html"
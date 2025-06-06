from django.views.generic import TemplateView


class GroupView(TemplateView):
    template_name = "rental/groups.html"

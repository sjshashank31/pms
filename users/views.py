from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Resident, Building
from .forms import ResidentForm


# Create your views here.

class ResidentCreateView(CreateView):
    def get(self, request, *args):
        print(ResidentForm())
        ctx = {"buildings": Building.objects.all()}
        return render(request, 'create_resident_form.html', ctx)


class DashBoardView(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            "name": "Shashank"
        }

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data()
        return render(request, 'index.html',ctx)


class ResidentListView(ListView):
    pass

    # model = UserProfile
    # paginate_by = 100
    # template_name = 'resident_list.html'
    #
    # def get_queryset(self):
    #     return UserProfile.objects.filter(role=UserProfile.RESIDENT)




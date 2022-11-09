from django.shortcuts import render

from .models import Budget

def index(req):
    budget_list = Budget.objects.all()
    context = {
        'budget_list' : budget_list,
    }
    return render(req, 'index.html', context)

def detail(req, budget_id):
    try:
        budget = Budget.objects.get(pk=budget_id)
    except Budget.DoesNotExist:
        raise Http404("Budget does not exist")
    return render(req, 'budget.html', {'budget': budget})
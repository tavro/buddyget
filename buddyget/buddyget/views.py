from django.shortcuts import render

from .models import Budget, BudgetRow

def index(req):
    if req.method == 'POST':
        name = req.POST['name']
        budget = Budget.objects.create(title=name)
        budget.save()

    budget_list = Budget.objects.all()
    context = {
        'budget_list' : budget_list,
    }
    return render(req, 'index.html', context)


def detail(req, budget_id):
    if req.method == 'POST':
        date = req.POST['date']
        place = req.POST['place']
        cost = req.POST['cost']
        budget = Budget.objects.get(pk=budget_id)
        row = BudgetRow.objects.create(date=date, place=place, cost=cost, budget=budget)
        row.save()

    try:
        budget = Budget.objects.get(pk=budget_id)
        rows = budget.rows.all()
        price_sum = 0
        each = 0
        for row in rows:
            price_sum += row.cost
        each = price_sum / 2
    except Budget.DoesNotExist:
        raise Http404("Budget does not exist")
    return render(req, 'budget.html', {'budget': budget, 'rows': rows, 'sum': price_sum, 'each': each})
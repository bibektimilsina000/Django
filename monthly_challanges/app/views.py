from django.shortcuts import render
from django.http import Http404
from .assets.monthly import MonthChallanges


def index(request):

    months = MonthChallanges.challanges.keys

    return render(request, 'app/index.html', {"months": months})


def challanges(request, month):
    

    try:
        challange = MonthChallanges.challanges[month]

        return render(request, 'app/challanges.html', {'challange': challange})
    except:
        raise Http404()


def challanges_by_num(request, month):

    try:

        challange = list(MonthChallanges.challanges.values())[month]
        month = list(MonthChallanges.challanges.keys())[month]

        data = {
            'month': month,
            'challange': challange
        }
        return render(request,'app/challanges.html',data)

    except:
         raise Http404()

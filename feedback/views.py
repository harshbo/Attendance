from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        nfc = int(request.POST['classes_total'])
        nfd = int(request.POST['classes_done'])
        nfa = int(request.POST['classes_attended'])

        if nfc >= nfd and nfd >= nfa:
            k = (nfa * 100) / nfd
            context['current_attendance'] = f"Current attendace {round(k, 2)}%"
            if (k < 75):
                k1 = (75 * nfc) / 100
                r = k1 - nfa
                context[
                    'to_cover_percentage'] = f"You need to attend {round(r)} classes to get 75% attendance"
        else:
            context['current_attendance'] = "Please enter the data correctly"

    return render(request, 'feedback/form.html', context)

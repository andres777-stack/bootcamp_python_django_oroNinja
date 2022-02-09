from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'tesoro' in request.session:
        context = {'tesoroR': request.session['tesoro'], 
        'registroActividadR': request.session['registroActividad']}
        return render(request, 'index2.html', context)
    else:
        request.session['registroActividad'] = []
        request.session['tesoro'] = 0
        return render(request, 'index.html')

def proccess(request):
    if request.method == 'POST':
        if request.POST['building'] == 'farm':
            temp = random.randint(10, 12)
            request.session['tesoro'] += temp
            request.session['registroActividad'].append('Has ganado: ' + str(temp))
            return redirect('/')
        elif request.POST['building'] == 'cave':
            temp = random.randint(5, 10)
            request.session['tesoro'] += temp
            request.session['registroActividad'].append('Has ganado: ' + str(temp))
            return redirect('/')
        elif request.POST['building'] == 'house':
            temp = random.randint(2, 5)
            request.session['tesoro'] += temp
            request.session['registroActividad'].append('Has ganado: ' + str(temp))
            return redirect('/')
        else:
            temp = random.randint(-50, 50)
            if temp == 0:
                request.session['registroActividad'].append('No has ganado ni perdido: ' + str(temp))
                return redirect('/')
            elif temp > 0:
                request.session['tesoro'] += temp
                request.session['registroActividad'].append('Has ganado: ' + str(temp))
                return redirect('/')
            else:
                request.session['tesoro'] -= abs(temp)
                request.session['registroActividad'].append('Has perdido: ' + str(temp))
                return redirect('/')
# Create your views here.

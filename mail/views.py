from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from mail.models import Record,Survey,StreamWaderForm,SurveyForm
from django.contrib.flatpages.views import flatpage

def contact(request):
    if request.POST.items():
        Record.objects.create(
            name = request.POST.get('name',''),
            lake_addr = request.POST.get('lake_addr',''),
            home_addr = request.POST.get('home_addr',''),
            email = request.POST.get('email',''),
            comments = request.POST.get('comments','')
        )
        return HttpResponseRedirect('/thankyou/')
    return flatpage(request,request.path)
    
def streamwader(request):
    if request.method == 'POST':
        form = StreamWaderForm(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/thankyou/')
    else:
        form = StreamWaderForm()
    return render_to_response('streamwaders.html', {
        'form': form,
    }, RequestContext(request))

def survey(request):
    if request.method == 'POST':
	form = SurveyForm(request.POST)
	if form.is_valid():
	    form.save()
	    return HttpResponseRedirect('/surveythanks/')
    else:
	form = SurveyForm()
    return render_to_response('survey.html', {
	'form': form,
    }, RequestContext(request))

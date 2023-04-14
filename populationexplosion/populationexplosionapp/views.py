from django.http import HttpResponse
from django.shortcuts import render

from . models import places
from . models import members

def demo(request):
     objct=places.objects.all()
     var=members.objects.all()
     return render(request,'travelo.html',{'result':objct,'rslt':var})

















# # Create your views here.
# def population(request):
#     return HttpResponse("A population consist of all the individuals of the same species occupying a Particular "
#                         "geographical area at a given time. It ranks subordinate to species. A species may have a "
#                         "single population or many populations confined to distinct area. The present population of "
#                         "our country is 102.7 billions. In the present, the population of our country is increasing. "
#                         "It is very dangerous and when our natural resources are going on decreasing. The main cause "
#                         "of high rate of growth rate is a widening gap between birth rate and death rate. The growing "
#                         "urban population created many problems for urban areas as well as rural areas.")


# def aim(request):
#     return render(request, 'new.html')
#
#
# def dens(request):
#     return HttpResponse("Population density is the number of individuals per unit area or per unit volume at a given time. The distribution of human population is not uniform throughout the world only about one–third of the total land area is inhabited. Of the inhabited areas, some are thickly populated, others sparsely. This depends upon the availability of the requirements of life.")
#
# def factors(request):
#     return render(request,'home.html')

from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from DashboardMonitoring.models import ProductivityPerHour, Chain
import json

def index(request):
    chainNames = Chain.objects.all()
    context = {
        'chainNames': chainNames,
    }
    return render(request, 'index.html', context)


def production(request):
    chainNames = Chain.objects.all()
    productivityPerHours = ProductivityPerHour.objects.all()
    chains = [Chain.objects.get(pk=i.chain.id) for i in productivityPerHours]
    productivityPerHourYield = ["{:.2f}".format((i.hour/j.obj)*100) for i, j in zip(productivityPerHours, chains)]
    productivityPerHourYieldInt = [int(float(i) * 100) for i in productivityPerHourYield]
    productivityPerHoursData = serializers.serialize('json', productivityPerHours)
    chainsData = serializers.serialize('json', chains)
    productivityPerHourYieldData = [{'val': i} for i in productivityPerHourYieldInt]
    productivityPerHourYieldColors = []
    for i in productivityPerHourYieldInt:
        if int(i) > 50:
            productivityPerHourYieldColors.append('bg-success')
        elif int(i) == 50:
            productivityPerHourYieldColors.append('bg-warning')
        else:
            productivityPerHourYieldColors.append('bg-danger')
    productivityPerHourYieldColorsData = [{'name': i} for i in productivityPerHourYieldColors]
    context = {
        'productivityPerHoursData': json.loads(productivityPerHoursData),
        'chainsData': json.loads(chainsData),
        'productivityPerHourYieldData': productivityPerHourYieldData,
        'chainNames': chainNames,
        'data': zip(productivityPerHourYieldData, json.loads(productivityPerHoursData), json.loads(chainsData), productivityPerHourYieldColorsData)
    }
    return render(request, 'production.html', context)


def quality(request):
    chainNames = Chain.objects.all()
    context = {
        'chainNames': chainNames,
    }
    return render(request, 'quality.html', context)

def chainDetail(request, chainId):
    chainNames = Chain.objects.all()
    currentChain = Chain.objects.get(pk=chainId)
    currentChainProductivityPerHourData = ProductivityPerHour.objects.filter(chain=chainId)
    currentChainProductivityPerHourTotalData = currentChainProductivityPerHourData.aggregate(Sum('productivity'))
    currentChainProductivityPerHourRemainingData = int(currentChain.obj) - int(currentChainProductivityPerHourTotalData['productivity__sum'])
    if currentChainProductivityPerHourData.order_by('latest_modification').reverse()[0].hour == 1:
        currentChainProductivityPerHourDataProcessed = currentChainProductivityPerHourData.order_by('latest_modification').reverse()[:1]
    else:
        currentChainProductivityPerHourDataProcessed = currentChainProductivityPerHourData.order_by('latest_modification').reverse()[:2]
    context = {
        'chainNames': chainNames,
        'currentChain': currentChain,
        'currentChainProductivityPerHourData': currentChainProductivityPerHourDataProcessed,
        'currentChainProductivityPerHourTotalData': currentChainProductivityPerHourTotalData,
        'currentChainProductivityPerHourRemainingData': currentChainProductivityPerHourRemainingData,
    }
    return render(request, 'chains.html', context)


def productivityPerHour(request):
    productivityPerHours = ProductivityPerHour.objects.all()
    chains = [Chain.objects.get(pk=i.chain.id) for i in productivityPerHours]
    productivityPerHourYield = ["{:.2f}".format((i.hour/j.obj)*100) for i, j in zip(productivityPerHours, chains)]
    productivityPerHourYieldInt = [int(float(i) * 100) for i in productivityPerHourYield]
    productivityPerHoursData = serializers.serialize('json', productivityPerHours)
    chainsData = serializers.serialize('json', chains)
    productivityPerHourYieldData = [{'val': i} for i in productivityPerHourYieldInt]
    productivityPerHourYieldColors = []
    for i in productivityPerHourYieldInt:
        if int(i) > 50:
            productivityPerHourYieldColors.append('bg-success')
        elif int(i) == 50:
            productivityPerHourYieldColors.append('bg-warning')
        else:
            productivityPerHourYieldColors.append('bg-danger')
    productivityPerHourYieldColorsData = [{'name': i} for i in productivityPerHourYieldColors]

    context = {
        'productivityPerHoursData': json.loads(productivityPerHoursData),
        'chainsData': json.loads(chainsData),
        'productivityPerHourYieldData': productivityPerHourYieldData,
        'productivityPerHourYieldColorsData': productivityPerHourYieldColorsData,
    }
    return JsonResponse(context, content_type="application/json")

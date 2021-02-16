from django.shortcuts import render


def index(request):
    return render(request, 'AI/Home.html')


def example(request):
    return render(request, 'AI/examples.html')


def project(request):
    return render(request, 'AI/project.html')


def citation(request):
    return render(request, 'AI/citations.html')

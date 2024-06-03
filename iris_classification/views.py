from django.shortcuts import render
import joblib

# Create your views here.
def iris(request):
    return render(request, "iris.html")


model = joblib.load('..\\django_workshop\\models\\lgmodel.joblib')
def result(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepalLength'))
        sepal_width = float(request.POST.get('sepalWidth'))
        petal_length = float(request.POST.get('petalLength'))
        petal_width = float(request.POST.get('petalWidth'))

        # Make prediction
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        
        return render(request, "iris.html", {'answer': prediction})

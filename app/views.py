from django.shortcuts import render, HttpResponse

from app.models import Name

# Create your views here.
def home(request):
    if request.method=='POST':
        btn = request.POST['sel']
        if(btn=='insert'):
            id = request.POST['id']
            name = request.POST['name']
            obj = Name()
            obj.id = id
            obj.name = name
            try:
                obj.save()
            except:
                return render(request, 'app/result.html',{'result':"Error! Can't insert into Database"})
            return render(request, 'app/result.html',{'result': "Inserted successfully!"})
        
        elif(btn=='retrive'):
            id = request.POST['id']
            try:
                obj = Name.objects.get(id=id)
            except:
                return render(request,'app/result.html',{'result':"Can't find data in the Database"})
            return render(request, 'base.html',{'obj':obj})
        
        elif(btn=='update'):
            id = request.POST['id']
            obj = Name.objects.get(id=id)
            obj.name = request.POST['name']
            try:
                obj.save()
            except:
                return render(request, 'app/result.html',{"result":"Error! Can't update Database"})
            return render(request, 'app/result.html',{'result': "Successfully updated!"})
        
        elif(btn=='delete'):
            id = request.POST['id']
            try:
                obj = Name.objects.get(id=id)
            except:
                return render(request, 'app/result.html',{'result':"User doesn't exist"})
            try:
                obj.delete()
            except:
                return render(request, 'app/result.html',{'result':"Couldn't delete record at this time!"})
            return render(request, 'app/result.html',{'result':"Record deleted successfully"})
        
    return render(request, 'base.html')
    
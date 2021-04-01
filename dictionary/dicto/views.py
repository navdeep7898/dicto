from django.shortcuts import render , redirect
from dicto.models import Words

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    if request.method =="POST":
        w = request.POST.get("word")
        word = Words.objects.get(eword=w)
        if str(w) == str(word):
            return render(request,'index.html',{"word":word})



def edit(request , eword):
    word = Words.objects.get(eword=eword)
    if request.method == "POST":
        hword = request.POST.get("hword")
        uses = request.POST.get("use")
        rword = request.POST.get("rword")
        word.hword = hword
        word.uses = uses
        word.rword = rword
        word.save()
        return redirect("/" )
    return render(request, 'edit.html' , {"word":word})
    
def add(request):
    if request.method == "POST":
        w = Words()
        w.eword = request.POST.get("word")
        w.hword = request.POST.get("hword")
        w.uses = request.POST.get("use")
        w.rword = request.POST.get("rword")
        w.save()
        msg = "Word Added Succesfully"
        return render(request,'add.html',{"msg":msg})
    return render(request, 'add.html')


def show(request):
    word = Words.objects.all()
    return render(request,'show.html',{"word":word})

def delete(request,eword):
    word = Words.objects.get(eword=eword)
    word.delete()
    return redirect("/")
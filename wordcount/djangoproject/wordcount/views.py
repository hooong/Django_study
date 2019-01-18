from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}
    letter = len([i for i in text if i != ' ' and i != '.' and i != ','])

    for word in words:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1

    return render(request, 'result.html', {'full': text, 'total': len(words),'dic': word_dic.items(),'letter': letter})
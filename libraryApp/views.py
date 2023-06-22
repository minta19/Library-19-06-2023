from django.shortcuts import render
from django.views import View
import requests
import json
# Create your views here.
def home(request):
    return render(request,'libraryApp/home.html')

def book_list(request):
    with open('booklist_1476387407.json','r') as f:
        books=json.load(f)
        context={'books':books}
    return render(request,'libraryApp/book_list.html',context)

def book_details(request,book_id):
    with open('booklist_1476387407.json','r') as f1:
        books=json.load(f1)

    for book in books:
        if book['id']==book_id:
             
            return render(request,'libraryApp/book_details.html',{"Books":book})
       
    return render(request,'libraryApp/Not_found.html')

class AuthorListView(View):
    template_name = 'libraryapp/author_list.html'
    def get(self,request):
        response=requests.get('https://random-data-api.com/api/v2/users?size=10')
        if response.status_code==200:
            authors=response.json()
            context = {'authors': authors}
            return render(request, self.template_name, context)
        else:
            return render(request,'libraryApp/Not_found.html')

        
    
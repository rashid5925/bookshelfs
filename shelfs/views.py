from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Contact, Quote, Book, Favourite

def shelfs(request):
    template = loader.get_template("index.html")
    quotes = Quote.objects.all().values()
    book_obj = Book.objects.all().values()
    context = {
        'page': 'home',
        'current_time': datetime.now().time(),
        'quotes': quotes,
        'books': book_obj
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("about.html")
    context = {
        'page': 'about'
    }
    return HttpResponse(template.render(context, request))

def products(request):
    template = loader.get_template("products.html")
    book_obj = Book.objects.all().values()
    context = {
        'page': 'products',
        'books': book_obj
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    if request.method == 'POST':
        name = request.POST['u_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        template = loader.get_template("contact.html")
        context = {
            'page': 'contact',
            'message': 'Thanks for Contacting Us.'
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("contact.html")
        context = {
            'page': 'contact'
        }
        return HttpResponse(template.render(context, request))

def favourites(request):
    template = loader.get_template("products.html")
    user_id = request.GET.get('id')
    user = User.objects.get(id=user_id)
    books = Favourite.objects.values('book').filter(user=user)
    book_data = []
    for b in books:
        print(b['book'])
        curr = b['book']
        book_data.append(list(Book.objects.values().filter(id=curr))[0])
    context = {
        'page': 'favourites',
        'books': book_data
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            template = loader.get_template("login.html")
            context = {
                'page': 'login',
                'message': 'Incorrect Username or Password.'
            }   
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("login.html")
        context = {
            'page': 'login'
        }
        return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:    
            if User.objects.filter(username=username).exists():
                template = loader.get_template("register.html")
                context = {
                    'page': 'register',
                    'message': 'Username Already taken.'
                }   
                return HttpResponse(template.render(context, request))
            elif User.objects.filter(email=email).exists():
                template = loader.get_template("register.html")
                context = {
                    'page': 'register',
                    'message': 'Email Already exists.'
                }
                return HttpResponse(template.render(context, request))
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=f_name, last_name=l_name)
                user.save()
                return redirect('/login')
        else:
            template = loader.get_template("register.html")
            context = {
                'page': 'register',
                'message': 'Password donot match.'
            }   
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template("register.html")
        context = {
            'page': 'register'
        }
        return HttpResponse(template.render(context, request))

def logout(request):
    auth.logout(request)
    return redirect('/')

def quote(request):
    title = request.POST['title']
    quote = request.POST['quote']
    quoteObj = Quote()
    quoteObj.book_title = title
    quoteObj.quote = quote
    quoteObj.save()
    return redirect('/')

def rate(request):
    rating = float(request.POST['rating'])
    book_title = request.POST['title']
    book_obj = Book.objects.get(title=book_title)
    prev_rating = book_obj.rating
    no_of_ratings = book_obj.no_of_rating
    new_sum = rating + prev_rating
    new_count = no_of_ratings + 1
    new_rating = new_sum / new_count
    book_obj.no_of_rating = new_count
    book_obj.rating = new_rating
    book_obj.save()
    return redirect('/products')

def addToFvrt(request):
    title = request.POST['title']
    username = request.POST['username']
    book_obj = Book.objects.get(title=title)
    user_obj = User.objects.get(username=username)
    favt_obj = Favourite()
    favt_obj.user = user_obj
    favt_obj.book = book_obj
    favt_obj.save()
    return redirect('/favourites/?id=user_obj.id')
    
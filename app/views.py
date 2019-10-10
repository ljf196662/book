from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.models import BookInfo, PersonInfo


def index(request):
    data = PersonInfo.objects.all()
    return render(request, "app/index.html", {"data": data})


def book(request):
    print("=" * 30)
    print(request.method)
    if request.method == "GET":
        return render(request, "app/books.html")
    elif request.method == "POST":
        sea = request.POST.get("search")
        if sea.isdigit():
            data = BookInfo.objects.filter(pk=sea)
            return render(request, "app/books.html", {"data": data})
        else:
            data = BookInfo.objects.filter(btitle__icontains=sea)
            return render(request, "app/books.html", {"data": data})


def insert_book(request):
    if request.method == "GET":
        return render(request, "app/insert_book.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        pub_date = request.POST.get("pub_date")
        read = request.POST.get("read")
        comment = request.POST.get("comment")
        BookInfo.objects.create(btitle=title, bpub_date=pub_date, bread=read, bcomment=comment)
        return redirect("/book/")


def delete_book(request, no):
    BookInfo.objects.get(id=no).delete()
    return redirect("/book/")


def book_id(request, no):
    lis = BookInfo.objects.get(id=no)
    print(lis.id, lis.btitle, lis.bpub_date, lis.bread, lis.bcomment)
    return HttpResponse(lis)


def books_all(request):
    data = BookInfo.objects.all()
    for book in data:
        print(book.id, book.btitle, book.bpub_date, book.bread, book.bcomment)
    return HttpResponse("ok")


def test(request):
    lis = BookInfo.objects.filter(btitle__isnull=False)
    for book in lis:
        print(book.id, book.btitle, book.bpub_date, book.bread, book.bcomment)
    return HttpResponse(lis)
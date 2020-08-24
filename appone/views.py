from django.shortcuts import render, HttpResponse, redirect
from appone import models
# Create your views here.

# 展示出版社列表
def publisher(request):

    ret = models.Publisher.objects.all()
    return  render(request,'index.html', {'publisher':ret})

# 添加出版社
def add(request):
    if request.method == 'POST':
        #获取用户提交的数据
        name = request.POST.get('name')
        res = models.Publisher.objects.filter(name = name)
        if res:
            return render(request, 'add.html', {'error': "出版社名称已存在"})
        models.Publisher.objects.create(name= name) # 新增数据
        return redirect('/publisher_list/')

    return render(request, 'add.html')

# 删除
def publisher_delete(request):
    #获取要删除的数据id
    pk = request.GET.get('pk')
    # models.Publisher.objects.get(id = pk).delete() #查询到一个对象就删除
    models.Publisher.objects.filter(id = pk).delete() #查询到一个对象列表就删除

    return redirect('/publisher_list/')

# 编辑
def publisher_edit(request):
    # get 返回一个页面，页面包含form表单 input 有原始数据
    pk = request.GET.get('pk')
    pub_obj = models.Publisher.objects.get(pk = pk)
    print(pub_obj.name)
    if request.method == 'GET':
        return render(request, 'edit.html', {'obj': pub_obj})
    else:
         pub_obj.name = request.POST.get('name') #只是内存中修改了
         if not pub_obj.name:
             return render(request, 'edit.html', {'error':"输入不可以为空"})
         pub_obj.save() # 修改操作提交到数据库
         return redirect('/publisher_list')



#展示书籍
def book_list(request):
    #查询所有书籍
    books = models.Book.objects.all()
    for i in books:
        print(i.publisher)
        print(i.publisher_id)
    return render(request, 'book_list.html', {"books":books})

# 添加书籍
def book_add(request):

    error = ''
        #返回添加书籍页面
    if request.method == 'POST':
        # 获取书籍
        book_name = request.POST.get('book_name')
        # 获取出版社
        pub = request.POST.get('pub')
        if not book_name: #判断书籍不能为空
            error = '书名不能为空'
        elif models.Book.objects.filter(name= book_name):
            error = '书名已存在'
        else:
            # 插入数据到数据库
            models.Book.objects.create(name= book_name, publisher_id= pub)
            return redirect('/book_list/')
        # 查询所有出版社
    all_publisher = models.Publisher.objects.all()
    return render(request, 'book_add.html', {"pub": all_publisher,'error':error})


# #删除书籍
def book_del(request):

#
#     #获取用户提交要删除的书籍id

    print(request.GET)
    pk = request.GET.get('id')
    print(pk)
    # 获取删除后的书籍
    models.Book.objects.filter(pk = pk).delete()
    #重定向页面
    return redirect('/book_list/')

#编辑书籍
def book_edit(request):
    error = '' #定义错误信息
    #获取要编辑的书籍id
    pk = request.GET.get('id')
    #获取书籍信息
    obj = models.Book.objects.get(pk = pk)

    # 获取所有出版社给模版渲染用
    all_publishers = models.Publisher.objects.all()
    if request.method == 'POST':
        request_book_name = request.POST.get('name')
        all_publishers = request.POST.get('all_publishers')

        if not request_book_name:
            error = '书籍不能为空'
        else:
            obj.name = request_book_name
            obj.publisher_id = all_publishers
            obj.save()
            return redirect('/book_list/')
    return render(request, 'book_edit.html',{'obj':obj,'all_publishers':all_publishers, 'error':error})


#展示作者信息
def author_list(request):
    #查询所有的作者
    all_authors = models.Author.objects.all()
    #返回一个页面包含这些信息
    # for  author in all_authors:
    #     print(author.pk)
    #     print(author.author_name)
    #     print(author.books) #关系管理对象
    #     print(author.books.all()) #所关联的所有对象

    return render(request,'author_list.html', {'authors':all_authors})

#新增作者
def author_add(request):

    #post请求
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_ids = request.POST.getlist('book_ids') #获取多个数据 (列表)
        author_obj = models.Author.objects.create(author_name = author_name) #插入作者名字
        print(author_obj)
        #该作何回头提交的书籍绑定多对多的关系
        author_obj.books.set(book_ids)  #设置多对多的关系
        return redirect('/author_list')

    #获取用户提交的数据
    #向数据库插入数据
    #返回重定向展示作者页面

    # get请求
    #查询所有的书籍
    all_books = models.Book.objects.all()
    # f返回一个页面，让用户输入作者姓名，选择他的作品
    return render(request, 'author_add.html', {"all_books":all_books})

# 删除作者
def author_del(request):
    pass
    # 获取要删除的作者id
    pk = request.GET.get('id')
    print('pk:{}'.format(pk))
    # 删除作者 也删除了和该作者相关的书籍关系
    models.Author.objects.filter(pk = pk).delete()
    # 返回重定向
    return redirect('/author_list/')

#编辑作者
def author_edit(request):
    # 获取要编辑的作者id
    pk = request.GET.get('id')
    author = models.Author.objects.filter(pk = pk).first()
    books = models.Book.objects.all()
    if request.method == 'POST':

        author_name = request.POST.get('author_name')
        books_ids = request.POST.getlist('book')
        # 第一种修改
        # author.author_name = author_name
        # author.save()
        # 第二种修改
        models.Author.objects.filter(pk = pk).update(author_name = author_name)
        # # 修改作者和书的多对多的关系

        author.books.set(books_ids)
        return redirect('/author_list')

    # 修改
    # 返回重定向页面
    return render(request, 'author_edit.html', {"author": author, "books": books})
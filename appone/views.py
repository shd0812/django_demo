from django.shortcuts import render, HttpResponse, redirect
from appone import models
# Create your views here.


def publisher(request):

    ret = models.Publisher.objects.all()
    return  render(request,'index.html', {'publisher':ret})

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
#coding=utf-8
from django.shortcuts import render
from literature.models import Doc
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def index(request):
    content={}
    content.update(csrf(request))
    doc_list = Doc.objects.all()
    return render(request,'index.html',{'doc_list':doc_list,'content':content})


def add_doc(request):
    content={}
    content.update(csrf(request))
    
    if request.POST:
    	if request.POST['title'] != "" and request.POST['author'] != "" and request.POST['date'] != "" and request.POST['source'] != "":
            try:             

                doc=Doc()
                doc.title=request.POST['title']
                doc.author=request.POST['author']
                doc.date=request.POST['date']
                doc.source=request.POST['source']
                doc.save()
                content['title'] = u"文献：《" + request.POST['title'] + u"》添加成功!"
            except:
                content['title'] = u"发生错误，文献信息添加失败!"
        else:
            content['title']=u"录入内容不完整，请重新输入！"

    return render(request,'add_doc.html',content)


def delete_doc(request,id):
    try:
        p = Doc.objects.get(id=id)
        p.delete()
    except:
        print u"删除失败"

    doc_list = Doc.objects.all()
    return render_to_response('index.html',{'doc_list':doc_list})


def edit_doc(request,id):
    content={}
    content.update(csrf(request))
    p = Doc.objects.get(id=id)
    
    if request.POST:
        try:
            p.title=request.POST['title']
            p.author=request.POST['author']
            p.date=request.POST['date'] 
            p.source=request.POST['source']
            p.save()
            content['flag'] = 1
        except:
            print u"修改失败"

    content['title'] = p.title
    content['author'] = p.author
    content['date'] = p.date
    content['source'] = p.source

    return render(request,'edit_doc.html',content)


def search_doc(request):
    content={}
    content.update(csrf(request))
    
    if request.POST:
        search=request.POST['search']
        if request.POST.get('selectType') == 'author':
            doc_list = Doc.objects.filter(author=search)
        elif request.POST.get('selectType') == 'date':
            doc_list = Doc.objects.filter(date=search)
        elif request.POST.get('selectType') == 'title':
            doc_list = Doc.objects.filter(title__contains=search)
        elif request.POST.get('selectType') == 'source':
            doc_list = Doc.objects.filter(source__contains=search)

	return render(request,'search_doc.html',{'doc_list':doc_list,'content':content})
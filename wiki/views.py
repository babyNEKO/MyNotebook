from django.shortcuts import render
from .models import Note
from time import strftime, localtime


# Create your views here.

def index(request):
    now_month = strftime("%m", localtime())
    now_year = strftime('%Y', localtime())
    context = {
        'title': '个人知识库',
        'history': Note.objects.filter(change_time__month=now_month, change_time__year=now_year)[:4],
    }
    return render(request, 'index.html', context)


def create(request):
    # 创建笔记
    try:
        if request.method == 'POST':
            post_title = request.POST.get('title')
            post_note = request.POST.get('note')
            Note.objects.create(note_name=post_title, context=post_note)
    except:
        err_msg = '笔记名重复'
    #     错误消息返回html模板
    return render(request, 'create_new_note.html')


def search(request):
    # 搜索笔记
    query = request.GET.get('query')
    if not query:
        error_msg = '请输入关键词'
        return render(request, 'search.html', {'error': error_msg})

    title_search = Note.objects.filter(note_name__icontains=query)
    context_search = Note.objects.filter(context__icontains=query)
    context = {
        's_list': title_search,
        'ctxt_search': context_search,
    }
    return render(request, 'search.html', context)


def view_note(request, note_id):
    # 查看笔记
    get_note = Note.objects.filter(id=note_id)
    context = {
        'note_id': note_id,
        'view': get_note,
    }
    return render(request, 'view_note.html', context)


def edit_note(request, note_id):
    if request.method == 'POST':
        post_title = request.POST.get('title')
        post_note = request.POST.get('note')
        save_note = Note.objects.get(id=note_id)
        save_note.note_name = post_title
        save_note.context = post_note
        save_note.save()
    # +++++++++++++++++++++++++++++++++++++++ #
    get_note = Note.objects.filter(id=note_id)
    context = {
        'note': get_note
    }
    return render(request, 'edit_note.html', context)

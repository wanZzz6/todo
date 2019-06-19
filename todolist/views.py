from django.shortcuts import render, redirect

# Create your views here.
lst = [
    {'待办事项': '吃饭', '已完成': True},
    {'待办事项': '逛街', '已完成': False},
]


def home(request):
    global lst

    if request.method == "POST":
        content = request.POST.get('待办事项')
        if not content or content.strip() == '':
            return render(request, 'todolist/home.html',
                          {'清单': lst, '警告': '请输入内容'})
        else:
            lst.append({'待办事项': content, '已完成': False})
            return render(request, 'todolist/home.html', {'清单': lst})
    else:
        return render(request, 'todolist/home.html', {'清单': lst})


def edit(request, forloop_counter):
    if request.method == "POST":
        content = request.POST['已修改事项']
        if not content or content.strip() == '':
            return render(request, 'todolist/edit.html',
                          {'警告': '请输入内容'})
        else:
            lst[forloop_counter - 1]['待办事项'] = content
            return redirect('todolist:主页')
    else:
        content = lst[forloop_counter - 1]['待办事项']
        return render(request, 'todolist/edit.html', {'待修改事项': content})


def about(request):
    return render(request, 'todolist/about.html')


def delete(request, forloop_counter):
    if request.method == "POST":
        forloop_counter = int(forloop_counter) - 1
        print(forloop_counter)
        lst.pop(forloop_counter)

    return redirect('todolist:主页')

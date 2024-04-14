from django.shortcuts import render, redirect
from .forms import NoticeBoardPostForm, CommentForm
from .models import *
from django.http import HttpResponse

    
def board(request):
    if request.method == 'POST':
        #print(1)
        #print(request.POST)
        title = request.POST['title']
        content = request.POST['content']
        
        board = NoticeBoardPost(
            title=title,
            content=content,
        )
        #print(title, content)
        #print(board)
        board.save()
        
        
        return redirect('/board/board_list') # Redirect to a success page or wherever you want
    else:
        form = NoticeBoardPostForm()
    return render(request, 'board/create_board.html', {'form': form})
   


def read(request, board_id):
    
    board_detail = NoticeBoardPost.objects.get(id = board_id)
    # article = Comment.objects.get(pk = board_id)
    # print(article)
    #댓글 조회, 생성
    comment_form = CommentForm()
    context = {
        "board_detail" : board_detail,
        'comments': board_detail.comment_set.all(),
        'comment_form' : comment_form,
    }

    
    #print(request.POST['text'])
    #return HttpResponse(f"{board_detail.id} = id <br> {board_detail.title} = title <br> {board_detail.content} = content")
    return render(request, 'board/board_detail.html', context)


def comment_create(request, pk):
    
    board_detail = NoticeBoardPost.objects.get(pk = pk)  
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.commentId  = board_detail
        comment.save()
    return redirect(f'/board/board_detail/{pk}')

def comment_delete(request, board_pk, comment_pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect(f'/board/board_detail/{board_pk}')

def boardList(request):
    if request.method == "GET":
        lists = NoticeBoardPost.objects.all()
        list1 = NoticeBoardPost.objects.get(id = 1)
        #print(list1)
        #lists = NoticeBoardPost.objects.values('content').all()
        #print(lists)
        context = {
            "list1" : list1,
            "lists" : lists,
        }
        return render(request, 'board/board_list.html', context)
    else:
        return HttpResponse("Invalid request method", status=405)
    #return HttpResponse('working!')


def boardEdit(request, pk):
    board = NoticeBoardPost.objects.get(id=pk)
    if request.method == "POST":
        #print(1)
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.save()
        form = NoticeBoardPostForm(request.POST, instance=board)

        if form.is_valid():
            form.save()
            return redirect(f'/board/board_detail/{pk}')

    else:
        boardForm = NoticeBoardPostForm(instance=board)
       # print(2)
        return render(request, 'board/update_board.html', {'boardForm':boardForm})
    

def boardDelete(request, pk):
    board = NoticeBoardPost.objects.get(id=pk)
    print(board)
    board.delete()
    return redirect('/board/board_list')



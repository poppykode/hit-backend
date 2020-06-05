from django.shortcuts import render,redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import messages
from pyfcm import FCMNotification
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,QueryForm
from .models import Query ,Comment
from accounts.models import User

# Create your views here.
@login_required
def all_queries(request):
    template_name = 'queries/query_list.html'
    query_list = Query.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(query_list,5)
    qs = paginator.get_page(page)
    context ={
        'obj':qs
    }
    return render(request,template_name,context)

@login_required
def get_query_by_id(request,pk):
    template_name ='queries/query_details.html'
    qs = get_object_or_404(Query,pk=pk)
    ps = Comment.objects.filter(query=pk)
    qs.comment_set.update( 
        read= True,
    )
    context ={
        'obj':qs,
        'form': CommentForm(),
        'comments':ps
    }
    return render(request,template_name,context)

@login_required
def add_comment(request,pk):
    push_service = FCMNotification(api_key="AAAAKq2O4e8:APA91bHjUnM7TTTqsb5F1xMz-H35oyjBTvaBQGRY5nYO58EVFEFmA0Z2yOlZSyIsfpAXBlsrRDNQwTUDNWKPGD2lquvDHijWOCXAtKlN7w2C-lf8smBZsy5saW7oejtT8u5sZvlLZU8-")
    qs = get_object_or_404(Query, pk=pk)
    current_user = get_object_or_404(User,pk=request.user.id)
    reply_message = request.POST.get('reply_message')
    if not reply_message:
        messages.error(request, 'Message box can not be empty.')
        return redirect('queries:get_query_by_id',pk=pk)
    qs.comment_set.create( 
        commentator= current_user,
        reply_message = reply_message,
    )
 

    registration_id = "c0PyQNL4BZA:APA91bE0RvKO9PtHPWYtlAuG5SbjqmamBN0HBPYTw5SZ-NTsA6GC-Mm_UxMkiFjOZtIUoXq-jrm3BTiNcomLDhrSSps9vDQRGi-Wd4W5OZPLqE2sNMoyJcZADtiQio4mLU-LgQ554V2X"
    message_title = qs.title
    message_body = reply_message
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    # Send to multiple devices by passing a list of ids.
    # registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
    # message_title = "Uber update"
    # message_body = "Hope you're having fun this weekend, don't forget to check today's news"
    # result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
    messages.success(request, 'Comment successfully added' +' '+ str(result))
    return redirect('queries:get_query_by_id',pk=pk)



@login_required
def add_query(request):
    template_name = 'queries/query_create.html'
    if request.method == 'POST':
        form = QueryForm(request.POST)   
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created_by = request.user
            form.save()
            messages.success(request, 'Message successfully send.')
            return redirect(reverse('queries:all_queries'))
    else:
        form = QueryForm()
    return render(request, template_name, {'form': form})

@login_required
def delete_comment(request,pk):
    qs = get_object_or_404(Comment, pk=pk)
    query_id =qs.query.pk
    template_name ='queries/comment_delete.html'
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Comment successfully deleted.') 
        return redirect('queries:get_query_by_id',pk=query_id)
    return render(request,template_name,{'obj':qs})

@login_required
def delete_query(request,pk):
    qs = get_object_or_404(Query, pk=pk)
    template_name ='queries/query_delete.html'
    if request.method=='POST':
        qs.delete()
        messages.success(request, 'Query successfully deleted.') 
        return redirect('queries:all_queries')
    return render(request,template_name,{'obj':qs})

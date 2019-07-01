from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html', {'posts1':posts})

def post_detail(request,pk):
    #post = get_object_or_404(Post, pk=pk)
    post=Post.objects.get(pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('list', pk=post.pk)
            #return redirect('')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

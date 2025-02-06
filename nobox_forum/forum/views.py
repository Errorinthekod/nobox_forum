from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like



def post_list(request):
    posts = Post.objects.all()
    print("Текущий путь к шаблону: 'forum/post_list.html'")
    return render(request, 'forum/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'forum/post_detail.html', {'post': post})

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(user=request.user, post=post, content=content)
    return redirect('post_detail', post_id=post_id)

@login_required
def toggle_like(request, post_id=None, comment_id=None):
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
    elif comment_id:
        comment = get_object_or_404(Comment, id=comment_id)
        like, created = Like.objects.get_or_create(user=request.user, comment=comment)
        if not created:
            like.delete()
    return redirect('post-detail', post_id=post_id)


def toggle_like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    existing_like = Like.objects.filter(user=user, comment=comment).first()

    if existing_like:

        existing_like.delete()
    else:

        Like.objects.create(user=user, comment=comment)


    return redirect('post_detail', post_id=comment.post.id)

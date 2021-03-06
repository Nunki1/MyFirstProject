from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm


def MyFirstProject_index(request):
    post = Post.objects.all().order_by("-created_on")
    context = {
        'posts': post,
    }
    return render(request, 'MyFirstProject_main.html', context)


def MyFirstProject_category(request, category):
    posts = Post.objects.filter(
        categories_name_contains=category
    ).order_by(
        "-created_on"
    )
    context = {
        'category': category,
        'posts':posts
    }
    return render(request, 'blog_category.html', context)


def MyFirstProject_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form':form
        }
    return render(request, 'blog_detail.html', context)









from django.db import transaction
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from post.models import Post


class PostWriteView(View):

    def get(self, request):
        # 이떄 post앞에 /가 안붙는건 setting 에 이미 templete url 이있기 떄문에
        # redirect의 경우에는 붙여서 초기화 해주어야함
        return render(request, 'post/write.html')

    @transaction.atomic
    def post(self, request):
        data = request.POST
        member = Member(**request.session['member'])

        data = {
            'post_title': data['post-title'],
            'post_content': data['post-content'],
            'member': member
        }

        post = Post.objects.create(**data)

        return redirect(post.get_absolute_url())


class PostDetailView(View):
    # urls에 선언한 변수는 request 에 담기지 않음
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)

        post.post_view_count += 1
        post.save(update_fields=['post_view_count'])

        context = {
            'post': post
        }
        return render(request, 'post/detail.html', context)


class PostUpdateView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        context = {
            'post': post
        }
        return render(request, 'post/update.html', context)

    def post(self, request, post_id):
        data = request.POST

        post = Post.objects.get(id=post_id)
        post.post_title = data['post-title']
        post.post_content = data['post-content']
        post.save()
        return redirect(post.get_absolute_url())


class PostDeleteView(View):
    def get(self, request):
        Post.objects.filter(id=request.GET['id']).update(status=False)
        # post = Post.objects.get(id=request.GET['id'])
        # post.status = False
        # post.save(update_fields=['status'])
        return redirect('/post/list/')


class PostListView(View):
    def get(self, request):
        # 한 페이지에 보여줄 컨텐츠 개수 row_count
        row_count = 5
        page = request.GET['page']
        if page is None:
            page = 1
        offset = (page - 1) * row_count
        limit = page * row_count

        posts = Post.enabled_objects.all()[offset:limit]
        return render(request, 'post/list.html', {'posts': posts})

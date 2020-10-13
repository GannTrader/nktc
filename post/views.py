from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from post.models import Post, Comment, Reply


class HomeView(ListView):
    model = Post
    template_name = "home-page.html"


class PostListView(ListView):
    paginate_by = 1
    model = Post
    template_name = "post/blog.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "post/detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        _slug = self.kwargs['slug']
        _post = Post.objects.get(slug=_slug)
        context['comments'] = Comment.objects.filter(post=_post, status="active").order_by("-pk")
        context['related_post'] = Post.objects.filter(category=_post.category).exclude(slug=_slug)
        return context

class RobotsView(TemplateView):
    template_name = "robots.txt"


class CommentView(View):
    def post(self, request, **kwargs):
        _slug = self.kwargs["slug"]
        _post = Post.objects.get(slug=_slug)
        cmt = request.POST["comment"]
        Comment.objects.create(
            post = _post,
            user = request.user,
            comment = cmt
        )
        messages.info(request, "Chúng tôi đã nhận được comment của bạn và đang ở trạng thái chờ duyệt...")
        return redirect(reverse_lazy("detail", kwargs={'slug': _slug}))


class ReplyView(View):
    def post(self, request, **kwargs):
        _pk = self.kwargs['pk']
        _cmt = Comment.objects.get(pk=_pk)
        _post = Post.objects.get(tagPost__comment=_cmt)
        reply = request.POST['replyCmt']

        Reply.objects.create(
            comment = _cmt,
            user = request.user,
            reply = reply
        )
        messages.warning(request, "Chúng tôi đã nhận được trả lời của bạn và đang ở trạng thái chờ duyệt...")
        return redirect(reverse_lazy("detail", kwargs={'slug': _post.slug}))


from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Category, ArticleTags
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import ArticleUpdateCreateForm, CommentCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ArticleView(View):
    template_name = 'article/article.html'

    def get(self, request, category_slug=None, tag_slug=None):
        articles = Article.objects.filter(status=True)
        paginator = Paginator(articles, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        categories = Category.objects.all()
        tags = ArticleTags.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            articles = articles.filter(category=category)
        if tag_slug:
            tag = ArticleTags.objects.get(slug=tag_slug)
            articles = articles.filter(tag=tag)
        return render(request, self.template_name, {'articles': page_obj, 'categories': categories, 'tags': tags})


class ArticleDetailView(View):
    form_class = CommentCreateForm

    def setup(self, request, *args, **kwargs):
        self.article_instance = get_object_or_404(Article, slug=kwargs['article_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, article_slug=None):
        comments = self.article_instance.articlecomments.filter(is_reply=False)
        return render(request, 'article/detail.html', {'article': self.article_instance, 'comments': comments,
                                                       'form': self.form_class})

    # for checking login
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.article = self.article_instance
            new_comment.save()
            messages.success(request, 'your comment submitted successfully', 'success')
            return redirect('article:article detail', self.article_instance.slug)


class ArticleDeleteView(LoginRequiredMixin, View):
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        if article.author.id == request.user.id:
            article.delete()
            messages.success(request, 'Article deleted successfully', 'success')
            return redirect('account:user profile', request.user.id)
        else:
            messages.error(request, 'You can not delete this article', 'danger')
        return redirect('home:home')


class ArticleUpdateView(LoginRequiredMixin, View):
    form_class = ArticleUpdateCreateForm
    template_name = 'article/update.html'

    def setup(self, request, *args, **kwargs):
        self.article_instance = Article.objects.get(pk=kwargs['article_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        article = self.article_instance
        if not article.author.id == request.user.id:
            messages.error(request, 'you can not update this article', 'danger')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, article_id):
        article = self.article_instance
        form = self.form_class(instance=article)

        return render(request, self.template_name, {'form': form})

    def post(self, request, article_id):
        article = self.article_instance
        form = self.form_class(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'your article updated successfully', 'success')
            return redirect('article:article detail', article.slug)


class ArticleCreateView(LoginRequiredMixin, View):
    form_class = ArticleUpdateCreateForm
    template_name = 'article/create.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.slug = form.cleaned_data['title']
            new_article.author = request.user
            new_article.save()
            messages.success(request, 'your article created successfully', 'success')
            return redirect('account:user profile')

from django.shortcuts import render
from.forms import ArticleForm

# Create your views here.
def create(request):
  if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect("article_detail", article.id)
  else:
      form = ArticleForm()

  return render(request, "create.html", {"form": form})
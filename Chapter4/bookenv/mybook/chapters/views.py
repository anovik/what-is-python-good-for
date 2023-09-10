from django.http import HttpResponse
from django.template import loader
from .models import Chapter

def chapters(request):
  allchapters = Chapter.objects.all().values()
  template = loader.get_template('all_chapters.html')
  context = {
    'allchapters': allchapters,
  }
  return HttpResponse(template.render(context, request))
  
def chapter(request, id):
  currentchapter = Chapter.objects.get(id=id)
  template = loader.get_template('chapter.html')
  context = {
    'currentchapter': currentchapter,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
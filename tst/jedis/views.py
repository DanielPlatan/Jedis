from django.shortcuts import render
from jedis.forms import CandidateForm, AuthForm
from jedis.models import Results, Questions, Candidate, Auth, Jedi
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('test')
    else:
        form = CandidateForm()

    return render(request, 'candidate.html', {'form': form, 'header':'Карта кандидата', 'button': 'Далее' })

def test(request):
    questions = Questions.objects.all()
    i = 0
    if request.method == 'POST':
        i = i + 1
        for q in questions:
            if 'choice'+str(q.id) in request.POST:
                obj = Results.objects.create(question=q.text, candidate=Candidate.objects.last(), result=request.POST['choice'+str(q.id)])
                obj.save()
        return HttpResponseRedirect('index')
    return render(request, 'test.html', {'list': questions, 'header':'Выбери варианты ответов.', 'button': 'Отправить' })

def jedi(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('view')
    else:
        form = AuthForm()
    return render(request, 'jedi.html', {'form': form,'header':'Выберите себя из списка.', 'button': 'Войти' })

def view(request):
    clist = Candidate.objects.all().exclude(master__isnull=False)
    plist = Candidate.objects.filter(master=Jedi.objects.get(id=Auth.objects.last().jedi_id))
    header = 'Здравствуйте, '+Jedi.objects.get(id=Auth.objects.last().jedi_id).name+'! Выберите кандидата для просмотра.'
    return render(request, 'view.html', {'candidate_list': clist, 'padavan_list':plist, 'header': header, 'button': 'Выход'})

def card(request):
  if request.method == 'POST':
      if 'approve' in request.POST:
          padavanLimit = 3
          if (Candidate.objects.filter(master=Jedi.objects.get(id=Auth.objects.last().jedi_id)).count()==padavanLimit):
              return HttpResponseRedirect('view')
          candidate = Candidate.objects.get(id=request.GET['pdid'])
          candidate.master = Jedi.objects.get(id=Auth.objects.last().jedi_id)
          candidate.save()
          ##################Отправка мэйла, закомментировать, если не настроена почта
          send_mail(
              'Успех',
              'Здравствуйте, уважаемый кандидат. Вы зачислены в падаваны',
              'shagind@gmail.com',
              ['shagind@gmail.com'],
              fail_silently=False,
          )
          #############################################################################
      return HttpResponseRedirect('view')
  else:
    candidate = Candidate.objects.get(id=request.GET['id'])
    results = Results.objects.filter(candidate_id=candidate.id)
  return render(request, 'card.html', {'results':results, 'candidate': candidate, 'results':results, 'button': 'Выход'})

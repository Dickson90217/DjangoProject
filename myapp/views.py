import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from myapp.forms import ProfileForm
from myapp.models import Dreamreal, Adoptreal,Helpreal


def hello(request):
    # text = '<h1> %s <h1>' % request.GET.get('name')
    today = datetime.datetime.now().date()
    return render(request, 'hello.html', {'today': today})
def howard(request):
    dreamreal = Dreamreal(
        website='howard',
        mail='howard@gmail.com',
        name='asd51775',
        phonenumber='0983458100')
    dreamreal.save()


def login(request):
    return render(request, 'loginTemolates.html')
#忘記密碼
def loginfg(request):
    fg = request.POST.get('loginfg')
    return render(request, 'loginfg.html')
def loginfgssue(request):
    account = request.POST.get('user')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    sorex3 = Dreamreal.objects.get(website=account)

    return render(request, 'seccuseeforloginfg.html',{'today': sorex3.name})
#註冊
def loginus(request):
    us = request.POST.get('loginus')
    return render(request, 'loginus.html')
def loginussue(request):
    account = request.POST.get('user')
    passwd = request.POST.get('passwd')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    dreamreal = Dreamreal(
        website=account,
        mail=email,
        name=passwd,
        phonenumber=phone)
    dreamreal.save()
    #驗證
    # sorex = Dreamreal.objects.get(website=account)
    # sorex1= Dreamreal.objects.get(mail=email)
    # sorex2= Dreamreal.objects.get(phonenumber=phonenumber)
    # if sorex.count()>=2:
    #     return HttpResponse('%d is been used'%account)
    # elif sorex1.count()>=2:
    #     return HttpResponse('%d is been used' % email)
    # elif sorex2.count()>=2:
    #     return HttpResponse('%d is been used' % phonenumber)
    # else:
    #     dreamreal = Dreamreal(
    #         website=account,
    #         mail=email,
    #         name=passwd,
    #         phonenumber=phonenumber)
    #     dreamreal.save()
    return render(request, 'seccuseeforloginus.html')
#登出
def logout(request):
    return render(request, 'logoutss.html')
def logoutssd(request):
    return render(request, 'loginTemolates.html')

#領養
def loginin(request):
    account = request.POST.get('user')
    passwd = request.POST.get('passwd')
    sorex1 = Dreamreal.objects.get(website=account)
    sorex2 = sorex1.name
    if passwd == sorex2:
        return render(request, 'adoptforhelp.html')
    else:
        return HttpResponse('帳號密碼錯誤')
def kind(request):
    return render(request,'animal.html')
def animals(request):
    animal = request.POST.get('animal')
    if animal == 'dog':
        return render(request, 'dogs.html')
    elif animal == 'cat':
        return render(request, 'cats.html')
    elif animal == 'other':
        return render(request, 'others.html')
    else:
        return HttpResponse('fail')

#領養或看刊登
def adopt(request):
    return render(request,'adopt.html')
#刊登
def adoptfor(request):
    return render(request, 'adoptfor.html')
def adoprrfor(request, ):
    petname = request.POST.get('petname')
    petsex = request.POST.get('petsex')
    picture = request.POST.get('picture'),
    place = request.POST.get('place')
    varity = request.POST.get('varity')
    yellowcard = request.POST.get('yellowcard')
    yellowcardnumber = request.POST.get('yellowcardnumber')
    userwho = request.POST.get('userwho')
    phone = request.POST.get('phone')
    why = request.POST.get('why')
    adoptreal = Adoptreal(
        petname=petname,
        petsex=petsex,
        place=place,
        varity=varity,
        yellowcard=yellowcard,
        yellowcardnumber=yellowcardnumber,
        userwho=userwho,
        why=why,
        phonenumber=phone
    )
    adoptreal.save()
    if request.method =='POST':
        arProfileForm =ProfileForm(request.POST , request.FILES)
        if arProfileForm.is_valid():
            adoptreal = Adoptreal()
            adoptreal.picture=arProfileForm.cleaned_data['pic']
            adoptreal.save()
    return render(request,'adoptforsesss.html')
def logafter(request):
    return render(request,'adoptforhelp.html')
#領養刊登
def whatadopt(request):
    res=Adoptreal.objects.all()
    return HttpResponse(res)
def backtofirst(request):
    return render(request, 'adoptforhelp.html')
#協尋
def help(request):
    return render(request,'help.html')
def helpfor(request):
    return render(request, 'helpfor.html')
def helppfor(request):
    petname = request.POST.get('petname')
    petsex = request.POST.get('petsex')
    picture = request.POST.get('picture'),
    when = request.POST.get('when')
    varity = request.POST.get('varity')
    yellowcard = request.POST.get('yellowcard')
    yellowcardnumber = request.POST.get('yellowcardnumber')
    where = request.POST.get('where')
    phone = request.POST.get('phone')
    special = request.POST.get('special')
    helpreal = Helpreal(
        petname=petname,
        sex=petsex,
        when=when,
        varity=varity,
        yellowcard=yellowcard,
        yellowcardnumber=yellowcardnumber,
        where=where,
        special=special,
        phonenumber=phone
    )
    helpreal.save()
    if request.method =='POST':
        arProfileForm =ProfileForm(request.POST , request.FILES)
        if arProfileForm.is_valid():
            adoptreal = Adoptreal()
            adoptreal.picture=arProfileForm.cleaned_data['pic']
            adoptreal.save()
    return render(request,'helpforsesss.html')

#協尋刊登
# def lattoo(request):
#     year= request.POST.get('year')
#     month = request.POST.get('month')
#     rno , rnumber=lottoCrawl(year, month)
#     # return HttpResponse('rno')
#     return render(request, 'result.html', {'rno': rno,'rnumber':rnumber})
#
#
# def lottoCrawl(y, m):
#     import requests
#     from bs4 import BeautifulSoup
#     import re
#     # rString = ""
#     rno=''
#     rnumber = []
#     rcount=0
#     rnumber.append([])
#     my_headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
#
#     r = requests.get("https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx" , headers=my_headers)
#     if r.status_code == 200:
#         soup = BeautifulSoup(r.text, 'html.parser')
#
#         __VIEWSTATE = soup.find('input', id='__VIEWSTATE').get('value')
#         __VIEWSTATEGENERATOR = soup.find('input', id='__VIEWSTATEGENERATOR').get('value')
#         __EVENTVALIDATION = soup.find('input', id='__EVENTVALIDATION').get('value')
#
#     for year in range(int(y), int(y) + 1):
#         for month in range(int(m), int(m) + 1):
#             payload = {'__VIEWSTATE': __VIEWSTATE,
#                        '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
#                        '__EVENTVALIDATION': __EVENTVALIDATION,
#
#                        'forma': '請選擇遊戲',
#                        'SuperLotto638Control_history1$txtNO': '',
#                        'SuperLotto638Control_history1$chk': 'radYM',
#                        'SuperLotto638Control_history1$dropYear': year,
#                        'SuperLotto638Control_history1$dropMonth': month,
#                        'SuperLotto638Control_history1$btnSubmit': '查詢',
#                        }
#
#             r = requests.post("https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx" , headers=my_headers,data=payload)
#             r.encoding = 'utf-8'
#
#             if r.status_code == 200:
#                 soup = BeautifulSoup(r.text, 'html.parser')
#
#                 number = soup.find_all('span', id=re.compile("SuperLotto638Control_history1_dlQuery_SNo\d_\d"))
#                 # print(year,month)
#                 # rString += year +' ' +month+'<br>'
#                 rno+=str(year) +' ' +str(month)+'\n'
#                 for index, num in enumerate(number):
#                     # print(num.text,end=' ')
#                     # rString += num.text + " "
#                     rnumber[rcount].append(num.text)
#                     if (index + 1) % 7 == 0:
#                         # print()
#                         # rString += '<br>'
#                         rcount+=1
#                         rnumber.append([])
#                 # print("----------------------")
#                 # rString += "----------------------" + '<br>'
#
#     return rno,rnumber
#
#
# def kind(request):
#     return None


# def croups(request):
#     dreamreal= Dreamreal(
#         website='www.google.com',
#         mail = 'howard@yaho.com',
#         name = 'howard',
#         phonenumber = '0983458458'
#     )
#     dreamreal.save()
#     #read all
#     objects=Dreamreal.objects.all()
#     res='Printing all Dreamreal entries in the DB:<br>'
#
#     for elt in objects:
#         res+=elt.name+'<br>'
#     #read one entry
#     sorex=Dreamreal.objects.get(name='howard')
#     res='Printing one entry : <br>'
#     res += sorex.name
#     #delet an entry
#     res+='<br>Deleting an entry<br>'
#     sorex.delete()
#     #update
#     dreamreal = Dreamreal(
#         website='www.google.com',
#         mail='howard@yaho.com',
#         name='howard',
#         phonenumber='0983458854'
#     )
#     dreamreal.save()
#     res+='Update entry'
#     dreamreal=Dreamreal.objects.get(name='howard')
#     dreamreal.name='hank'
#     dreamreal.save()
#     return HttpResponse(res)


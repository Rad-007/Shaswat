from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#from social_core.decorators import social_auth_required
#from social_django import social_auth_required

# Create your views here.

from django.http import HttpResponse


from django.contrib.auth.models import User   


def landingpage(request):


    return render(request,'landingpage.html')



def events(request):


    return render(request,'events.html')


def payment_file(email,utr):
     
     file=open('payment.txt','a')

     s="Email:-  "+email+"          "+"UTR:-   "+utr+'\n'

    

     file.write(s)


from django.http import HttpResponseRedirect
import time

from .models import Payment

def payment(request):


    if request.method=='POST':
        email=request.POST.get('email')
        utr=request.POST.get('utr')

        pay=Payment(email=email,utr=utr)
        pay.save()

        payment_file(email,utr)



        time.sleep(8)  # wait for 5 seconds
        return HttpResponseRedirect('/')
    
    else:
        return render(request,'payment.html')





    


def team(request):


    return render(request,'team.html')

from .models import User_Profile


def signup(request):

    if request.user.is_authenticated:

        if request.method=='POST':

            id=request.user.id

            name=request.POST.get('name')
            phone=request.POST.get('phone')
            institute=request.POST.get('institute')
            user = User.objects.get(id=id)
            user_email = user.email
            gender=request.POST.get('gender')
            email=user_email
            referral=request.POST.get('referral')
            user=User_Profile(name=name,email=email,phone=phone,institute=institute,referral=referral,gender=gender)
            user.save()

            return redirect('/')

        else:
            return render(request,'signup.html')
        
    
    else:
        return render(request,'signup.html')



from social_django.models import UserSocialAuth


def get_users_list():
    google_users = UserSocialAuth.objects.filter(provider='google-oauth2')

    google_user_ids = [u.user_id for u in google_users]

    users = User.objects.filter(id__in=google_user_ids)







from django.contrib.auth import logout
from django.shortcuts import redirect

def logoutuser(request):
    logout(request)
    return redirect('/')


from django.http import FileResponse

from django.http import FileResponse
from django.shortcuts import render

def view_pdf(request, filename):
    filepath = f'static/pdfs/{filename}'
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')


def events_parti(request):


    return render(request,'event_parti.html')


def competition(request):
    
    return render(request,'competitions.html')


def photography(request):
    content={
        'name':'SHUTTER SHOWDOWN',
        'filename':'photography.pdf',
        'gfom':'https://forms.gle/S8G7EotAaHkkHp1u7'
    }
    return render(request,'event_parti.html',content)

def dance(request):
    content={
        'name':'BEAT BRAWL',
        'filename':'dance.pdf',
        'gfom':'https://forms.gle/ewyXjLMRvEqT85Tz7'
    }
    return render(request,'event_parti.html',content)

def fashion(request):
    content={
        'name':'FASHION FIESTA',
        'filename':'fashion.pdf',
        'gform':'https://forms.gle/Q8zJXkiJPjR2LtRG8'
    }
    return render(request,'event_parti.html',content)

def bandwar(request):
    content={
        'name':'BAND WAR',
        'filename':'bandwar.pdf',
        'gform':'https://forms.gle/yL1DjrrrdCTzZUEcA'
    }
    return render(request,'event_parti.html',content)

def singing(request):
    content={
        'name':'TONE OF TITANS',
        'filename':'music.pdf',
        'gform':'https://forms.gle/36WERiqkke7HEihdA'
    }
    return render(request,'event_parti.html',content)


def gaming(request):
    content={
        'name':'HEADSHOT HEROES',
        'filename':'gaming.pdf',
        'gform':''
    }
    return render(request,'event_parti.html',content)

def painting(request):
    content={
        'name':'EMO SPLASH',
        'filename':'painting.pdf',
        'gform':''
    }
    return render(request,'event_parti.html',content)

def pitch_battle(request):
    content={
        'name':'PITCH BATTLE',
        'filename':'pitch_battle.pdf',
        'gform':'https://forms.gle/T8pWHC826Se42EbC8'
    }
    return render(request,'event_parti.html',content)


def odyessey(request):
    content={
        'name':'ODYESSEY 2K50',
        'filename':'odyessey.pdf',
        'gform':'https://forms.gle/U6qMnbpJsPMwcup27'
        
    }
    return render(request,'event_parti.html',content)

def hackathon(request):
    content={
        'name':'DISRUPTATION',
        'filename':'hackathon.pdf',
        'gform':'https://forms.gle/Bgc7BSzcFrszk8EC6'
    }
    return render(request,'event_parti.html',content)

def enegron(request):
    content={
        'name':'Enegron',
        'filename':'enegron.pdf',
        'gform':'https://forms.gle/n2n5AdEESJ2v9f7v5'
    }
    return render(request,'event_parti.html',content)

def roborumble(request):
    content={
        'name':'Robo Rumble',
        'filename':'roborumble.pdf',
        'gform':'https://docs.google.com/forms/d/e/1FAIpQLSfQXZDdw8AGBRoe7hcG7YyQ9mIdyJbNgJ8ApC51xL5xdcKazA/viewform?usp=sf_link'
    }
    return render(request,'event_parti.html',content)

def haalemausam(request):
    content={
        'name':'Haal-e-Mausam',
        'filename':'haalemausam.pdf',
        'gform':'https://forms.gle/yUE5XtwiT9dqRbm47'
    }
    return render(request,'event_parti.html',content)

def coding_contest(request):
    content={
        'name':'KINETIC KODING',
        'filename':'coding_contest.pdf',
        'gform':'https://forms.gle/NQdUesENA3HEp4Jy6'
    }
    return render(request,'event_parti.html',content)

def trading(request):
    content={
        'name':'Trading Titans',
        'filename':'',
        'gform':''
    }
    return render(request,'event_parti.html',content)

def cerebral(request):
    content={
        'name':'CEREBRAL FLEX',
        'filename':'cerebral.pdf',
        'gform':'https://forms.gle/H8towPasQvpKRnFc7'
    }
    return render(request,'event_parti.html',content)

def movie(request):
    content={
        'name':'FILMY FRENZY',
        'filename':'movie.pdf',
        'gform':'https://forms.gle/CGEAty8Lh8KGCZf67'
    }
    return render(request,'event_parti.html',content)
def competition_list():
    comp=['bandwar','cerebral','coding_contest','fashion','gaming','hackathon','movie','music','odyessey','painting','pitch_battle']
    return comp


from django.contrib.auth.models import User

def profile(request):

    try:
        #user_social_auth = request.user.social_auth.get(provider='google-oauth2')
        # 'google-oauth2' is the provider ID for Google OAuth2 authentication

        #user_id = user_social_auth.uid
        #user_email = user_social_auth.extra_data['email']
        # You can retrieve any other user data from the 'extra_data' dictionary
        # provided by Google OAuth2

        id=request.user.id
        user = User.objects.get(id=id)
        user_email = user.email
        try:
            user=User_Profile.objects.get(email=user_email)
        except User_Profile.DoesNotExist:
            user=None
        email='https://www.googleapis.com/auth/userinfo.email'

        

        context={'user':user,'email':user_email}

        



        return render(request,'profile.html',context)
        
        # Create a context dictionary with the user data

        
        # Pass the context dictionary to the template and render it
    except UserSocialAuth.DoesNotExist:

        return redirect('/')


    



from django.contrib import messages

from .models import Team, Invitations

@login_required
def create_team(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        team = Team.objects.create(name=name, creator=request.user)
        team.members.add(request.user)
        messages.success(request, 'Team created successfully!')
        return redirect('dashboard')
    return render(request, 'events_parti.html')

@login_required
def join_team(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            invitation = Invitations.objects.get(code=code)
            team = invitation.team
            team.members.add(request.user)
            messages.success(request, 'You have joined the team successfully!')
            invitation.delete()
            return redirect('dashboard')
        except Invitations.DoesNotExist:
            messages.error(request, 'Invalid team code!')
    return render(request, 'events_parti.html')

@login_required
def dashboard(request):
    teams = request.user.teams.all()
    invitations = Invitations.objects.filter(team__creator=request.user)
    return render(request, 'dashboard.html', {'teams': teams, 'invitations': invitations})

@login_required
def invite(request, team_id):
    team = Team.objects.get(id=team_id)
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    Invitations.objects.create(team=team, code=code)
    messages.success(request, f'Invite code for {team.name}: {code}')
    return redirect('dashboard')
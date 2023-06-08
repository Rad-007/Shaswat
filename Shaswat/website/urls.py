


from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[


    
    path('',views.landingpage,name='landingpage'),
    path('events',views.events,name='events'),
    path('payment',views.payment,name='payment'),
    path('competition',views.competition,name='competition'),
    path('events_parti',views.events_parti,name='events_parti'),
    path('shuttershowdown',views.photography,name='shuttershowdown'),
    path('beat_brawl',views.dance,name='beat_brawl'),
    path('fashion_fiesta',views.fashion,name='fashion_fiesta'),
    path('bandwar',views.bandwar,name='bandwar'),
    path('tone_of_titans',views.singing,name='tone_of_titans'),
    path('headshot_heroes',views.gaming,name='headshot_heroes'),
    path('emo_splash',views.painting,name='emo_splash'),
    path('shark_tank',views.pitch_battle,name='shark_tank'),
    path('odyessey',views.odyessey,name='odyessey'),
    path('disruptation',views.hackathon,name='disruptation'),
    path('kinetic_koding',views.coding_contest,name='kinetic_koding'),
    path('cerebral_flex',views.cerebral,name='cerebral_flex'),
    path('filmy_frenzy',views.movie,name='filmy_frenzy'),
    path('haale_mausam',views.haalemausam,name='haale_mausam'),
    path('robo_rumble',views.roborumble,name='roborumble'),
    path('enegron',views.enegron,name='enegron'),
    path('cerebral_flex',views.cerebral,name='cerebral_flex'),
    path('trading_titans',views.trading,name='trading_titans'),
    path('team',views.team,name='team'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logoutuser,name='logout'),
    path('profile',views.profile,name='profile'),
    path('social-auth/',include('social_django.urls',namespace='social')),


    
]
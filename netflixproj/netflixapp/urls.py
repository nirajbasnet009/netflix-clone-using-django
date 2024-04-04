from django.urls import path
from .views import home,ProfileList,ProfileCreate,MovieList,MovieDetail,PlayMovie
urlpatterns = [path('',home.as_view(),name='home'),\
               path('profiles',ProfileList.as_view(),name='profile-list'),
               path('profilecreate',ProfileCreate.as_view(),name='profile-create'),
               path('watch/<str:profile_id>',MovieList.as_view(),name='movie-list'),
               path('moviedetail/<str:movie_id>',MovieDetail.as_view(),name='movie-detail'),
               path('playmovie/<str:movie_id>',PlayMovie.as_view(),name='play-movie'),]

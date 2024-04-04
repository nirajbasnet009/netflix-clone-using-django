from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View 
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import ProfileForm
from .models import Profile,Movie
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# Create your views here.

class home(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile-list')
        return render(request, 'index.html')
    
class ProfileList(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, 'profilelist.html', {'profiles':profiles})
    
class ProfileCreate(LoginRequiredMixin,View):
    def get(self,request, *args, **kwargs):
        form = ProfileForm()
        return render(request, 'profilecreate.html')

    def post(self,request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
             profile = Profile.objects.create(**form.cleaned_data)
             if profile:
                    request.user.profiles.add(profile)
                    return redirect('profile-list')
        return render(request, 'profilelist.html')
    
class MovieList(LoginRequiredMixin, View):
    def get(self,request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            return render(request, 'movielist.html', {'movies': movies})
        except Profile.DoesNotExist:
            return redirect('profile-list')

class MovieDetail(LoginRequiredMixin,View):
    def get(self,request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            return render(request, 'moviedetail.html',{'movie': movie})
        
        except Movie.DoesNotExist:
            return redirect('movie-list')
        
class PlayMovie(LoginRequiredMixin, View):
    def get(self, request, movie_id, *args, **kwargs):
        movie = Movie.objects.get(uuid=movie_id)
        videos = movie.video.all()  # Get all associated videos
        if videos:
            # For simplicity, let's assume there's only one video per movie
            
            return render(request, 'playmovie.html', {'videos': videos})
        else:
            return HttpResponse("No video found for this movie.")
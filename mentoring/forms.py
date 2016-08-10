from django import forms

from .models import Post_By_Mentor, Post_By_Mentee, Bid_By_Mentee, Bid_By_Mentor, Comment, Like, Matched_Bid_By_Mentee, Matched_Bid_By_Mentor

class Post_By_MenteeForm(forms.ModelForm):
    class Meta:
        model = Post_By_Mentee
        fields = ['title', 'gender', 'lnglat', 'major', 'grade', 'GPA', 'hours', 'date', 'price', 'intro']
        

class Post_By_MentorForm(forms.ModelForm):
    class Meta:
        model = Post_By_Mentor
        fields = ['title', 'capacity', 'hours', 'date', 'lowest_price', 'intro']


class Bid_By_MenteeForm(forms.ModelForm):
    class Meta:
        model = Bid_By_Mentee
        fields = ['price']
        
        
class Bid_By_MentorForm(forms.ModelForm):
    class Meta:
        model = Bid_By_Mentor
        fields = ['plan']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'secret']
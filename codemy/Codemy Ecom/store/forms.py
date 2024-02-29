

from django.contrib.auth.models import User  #User মডেল, যা ব্যবহারকারীদের তথ্য সংরক্ষণ করে।
from django.contrib.auth.forms import UserCreationForm,UserChangeForm  #UserCreationForm, যা নতুন ব্যবহারকারীদের সাইন আপ করার ফর্ম তৈরিতে সাহায্য করে।
from django import forms  #forms মডিউল, যা ফর্ম তৈরির জন্য সাধারণ সরঞ্জাম সরবরাহ করে।


class UpdateUserForm(UserChangeForm):
	password = None
	#email: ব্যবহারকারীর ইমেল ঠিকানা সংগ্রহের জন্য।
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	
	#first_name: ব্যবহারকারীর প্রথম নাম সংগ্রহের জন্য।
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	
	#last_name: ব্যবহারকারীর শেষ নাম সংগ্রহের জন্য।
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta: # ফর্মের মেটা তথ্য নির্ধারণ:
		
		model = User #model: এটি নির্দিষ্ট করে যে ফর্মটি User মডেলের সাথে সংযুক্ত।
		
		#fields: এটি নির্দিষ্ট করে যে ফর্মে কোন কোন ক্ষেত্র অন্তর্ভুক্ত থাকবে।
		fields = ('username', 'first_name', 'last_name', 'email',)

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		### এই অংশ ফর্মের ক্ষেত্রগুলোর চেহারা (interface) এবং (style) আচরণ কাস্টমাইজ করে। উদাহরণস্বরূপ, এটি লেবেলগুলি সরিয়ে ফেলে, প্লেসহোল্ডার যোগ করে এবং সহায়ক পাঠ্য সরবরাহ করে।
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = ''





class SignUpForm(UserCreationForm):  #এই লাইন SignUpForm নামে একটি নতুন ক্লাস তৈরি করে, যা UserCreationForm ক্লাস থেকে উত্তরাধিকার সূত্রে প্রাপ্ত। অর্থাৎ, এটি নতুন ব্যবহারকারীদের নিবন্ধনের জন্য একটি বিশেষায়িত ফর্ম।
	
	#email: ব্যবহারকারীর ইমেল ঠিকানা সংগ্রহের জন্য।
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	
	#first_name: ব্যবহারকারীর প্রথম নাম সংগ্রহের জন্য।
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	
	#last_name: ব্যবহারকারীর শেষ নাম সংগ্রহের জন্য।
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta: # ফর্মের মেটা তথ্য নির্ধারণ:
		
		model = User #model: এটি নির্দিষ্ট করে যে ফর্মটি User মডেলের সাথে সংযুক্ত।
		
		#fields: এটি নির্দিষ্ট করে যে ফর্মে কোন কোন ক্ষেত্র অন্তর্ভুক্ত থাকবে।
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		### এই অংশ ফর্মের ক্ষেত্রগুলোর চেহারা (interface) এবং (style) আচরণ কাস্টমাইজ করে। উদাহরণস্বরূপ, এটি লেবেলগুলি সরিয়ে ফেলে, প্লেসহোল্ডার যোগ করে এবং সহায়ক পাঠ্য সরবরাহ করে।
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
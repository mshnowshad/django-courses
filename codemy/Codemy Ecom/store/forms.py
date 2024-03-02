

from django.contrib.auth.models import User  #User মডেল, যা ব্যবহারকারীদের তথ্য সংরক্ষণ করে।
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm    # যা নতুন ব্যবহারকারীদের সাইন আপ করার ফর্ম তৈরিতে সাহায্য করে।
from django import forms  #forms মডিউল, যা ফর্ম তৈরির জন্য সাধারণ সরঞ্জাম সরবরাহ করে।



#Search Products - Django Wednesdays ECommerce 26





    

	
	
	
#User Profile Page - Django Wednesdays ECommerce 25

from .models import Profile


class UserInfoForm(forms.ModelForm):
    country = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}), required=True)
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}), required=True)
    address = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Main Address'}), required=True)
    address2 = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Present Address'}), required=False)
    city = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}), required=True)
    zipcode = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}), required=True)

    class Meta:
        model = Profile
        fields = ('phone', 'address', 'address2', 'city', 'zipcode', 'country')

		






#update user password = ## 23
class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1','new_password2']
	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

		
			

class UpdateUserForm(UserChangeForm):
	password = None
	#email: ব্যবহারকারীর ইমেল ঠিকানা সংগ্রহের জন্য।
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required=True)
	
	#first_name: ব্যবহারকারীর প্রথম নাম সংগ্রহের জন্য।
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),required=False)
	
	#last_name: ব্যবহারকারীর শেষ নাম সংগ্রহের জন্য।
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),required=False)


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
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),required=True)
	
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

		# এই অংশ ফর্মের ক্ষেত্রগুলোর চেহারা (interface) এবং (style) আচরণ কাস্টমাইজ করে। উদাহরণস্বরূপ, এটি লেবেলগুলি সরিয়ে ফেলে, প্লেসহোল্ডার যোগ করে এবং সহায়ক পাঠ্য সরবরাহ করে।
		
		self.fields['username'].widget.attrs['class'] = 'form-control'  #এই লাইনে ফর্মের "ইউজারনেম" ফিল্ডের HTML এলিমেন্টের "class" এট্রিবিউটে মান সেট করা হচ্ছে, যা "form-control"। এটি Bootstrap এর CSS ক্লাস, যা এই ফিল্ডটি সুন্দরভাবে স্টাইল করে।
		self.fields['username'].widget.attrs['placeholder'] = 'User Name' #এই লাইনে "ইউজারনেম" ফিল্ডের HTML এলিমেন্টের "placeholder" এট্রিবিউটে মান সেট করা হচ্ছে, যা "User Name"। এটি ফিল্ডের ভেতরে টেক্সট লেখার জন্য ব্যবহৃত হয়।
		self.fields['username'].label = ''  #  "ইউজারনেম" ফিল্ডের লেবেলের মান খালি হচ্ছে। এটি ফর্মে দেখানো হবে না।
		self.fields['username'].help_text = ''#"ইউজারনেম" ফিল্ডের সাহায্য টেক্সট খালি হচ্ছে। এটি ফিল্ডের নীচে দেখানো হবে না।

		self.fields['password1'].widget.attrs['class'] = 'form-control'  #পাসওয়ার্ড" ফিল্ডের CSS ক্লাস সেট করা হচ্ছে যেটি "form-control"।
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'  #পাসওয়ার্ড" ফিল্ডের HTML এলিমেন্টের "placeholder" এট্রিবিউটে মান সেট করা হচ্ছে, যা "Password"।
		self.fields['password1'].label = ''  #পাসওয়ার্ড" ফিল্ডের লেবেলের মান খালি হচ্ছে, তাহলে এটি ফর্মে দেখানো হবে না।
		self.fields['password1'].help_text = ''  # "পাসওয়ার্ড" ফিল্ডের সাহায্য টেক্সট খালি হচ্ছে, তাহলে এটি ফিল্ডের নীচে দেখানো হবে না।

		self.fields['password2'].widget.attrs['class'] = 'form-control'  # কনফার্ম পাসওয়ার্ড" ফিল্ডের CSS ক্লাস সেট করা হচ্ছে যেটি "form-control"।
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'  # কনফার্ম পাসওয়ার্ড" ফিল্ডের HTML এলিমেন্টের "placeholder" এট্রিবিউটে মান সেট করা হচ্ছে, যা "Confirm Password"।
		self.fields['password2'].label = ''  #কনফার্ম পাসওয়ার্ড" ফিল্ডের লেবেলের মান খালি হচ্ছে, তাহলে এটি ফর্মে দেখানো হবে না।
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'  #কনফার্ম পাসওয়ার্ড" ফিল্ডের সাহায্য টেক্সট একটি HTML স্ট্রিং হিসেবে সেট করা হচ্ছে, যা ব্যবহারকারীকে অগ্রাধিকার নিতে বলে।
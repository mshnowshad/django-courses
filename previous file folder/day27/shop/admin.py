from django.contrib import admin

# Register your models here.

from . models import Product  #> : এই লাইনে বর্তমান ডিরেক্টরি থেকে models.py ফাইলের মধ্যে থাকা Product মডেলকে ইমপোর্ট করা হচ্ছে। Django-তে, মডেল ব্যবহার করা হয় ডাটাবেস টেবিল নির্দেশ করার জন্য।

admin.site.register(Product)  #> : এখানে, Product মডেলটি দ্বারা Django এ্যাডমিন ইন্টারফেসের সাথে রেজিস্টার করা হচ্ছে। Django এ্যাডমিন সাইট দিয়ে নিবন্ধিত মডেলগুলি ব্যবহারকারী বন্ধুত্বপূর্ণ ইন্টারফেসের মাধ্যমে সহজেই CRUD (Create, Read, Update, Delete) অপারেশন করতে পারেন।











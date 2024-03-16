""" ==================================> Django CSRF Tokens & Post Request | Python Django Tutorials In Hindi #16 <======================







ডি‌জ্জাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক যা ওয়েব অ্যাপ্লিকেশন ডেভেলপমেন্ট করার জন্য ব্যবহার করা হয়। CSRF টোকেন একটি নিরাপদ মেশিন গেট রিকোয়েস্ট হ্যান্ডলিং এর জন্য ব্যবহৃত হয়। 
যখন আপনি একটি ফর্ম সাবমিট করেন বা একটি POST রিকোয়েস্ট করেন, তখন Django সিস্টেম একটি CSRF টোকেন তৈরি করে যা প্রমাণিত করে যে রিকোয়েস্টটি নিরাপদ এবং অনুমোদিত। 
এই টোকেনটি রক্ষা করে যাতে কোনো অন্য সাইট বা কোনো অন্য অস্থায়ী রুট থেকে ধরে আসা রিকোয়েস্ট স্বীকৃতি পায় না।

যখন আপনি একটি ওয়েব ফর্মে CSRF টোকেন ব্যবহার করেন, তখন প্রতিটি টাইম যখন ফর্মটি জমা দেওয়া হয়, বা ডাটা পোস্ট করা হয়, সেই ফর্মের সাথে যুক্ত করা হয় একটি টোকেন।
এই টোকেনটি সার্ভার দ্বারা তৈরি করা হয় এবং তা দিয়ে রিকোয়েস্ট ভেরিফাই করা হয় যে সঠিকভাবে ফর্ম সাবমিট হচ্ছে।

এই CSRF টোকেনগুলি দুইটি মূল উদ্দেশ্য সেবন করে: প্রথমত, এটি সার্ভার কে আপনি যেকোনো নিরাপদ রিকোয়েস্ট পাঠাচ্ছেন তা সিগনাল করে। দ্বিতীয়ত, 
এটি নিরাপদ রিকোয়েস্টগুলির সুনিশ্চিতকরণ করে যে কোনো অন্য সূত্র থেকে রিকোয়েস্ট পাঠানো হয়নি।"""














from django.http import HttpResponse
from django.shortcuts import render





def index12(request):
    return render(request,'indess.html')




def analyze12(request):
    inputtxt = request.POST.get('text','default')   # ei line ta output nibe
    
    #checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps =  request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    
    
    
    
    congra = "Congratulations! "
    
    if removepunc == "on":
        punctuations = '''.,?!:;'"()[]{}-_./-&$#@^*%'''
        analyzertxt1 = " "   #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        
        for elment in inputtxt:
            if elment not in punctuations:
                analyzertxt1 = analyzertxt1 + elment
        
        allitemindics = {'Punctuations':' Your Punctuations Analyzed text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
                
    elif fullcaps == "on":
        analyzertxt1 = ""  #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        for elment in inputtxt:
            analyzertxt1 = analyzertxt1 + elment.upper()
        allitemindics = {'Punctuations':'  Your Upper Case text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
    
    elif newlineremover == "on":
        analyzertxt1 = ""
        for elment in inputtxt:
            if elment != '\n':
                analyzertxt1 = analyzertxt1 + elment
        allitemindics = {'Punctuations':' Your  Removed Newline text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
    
    elif  extraspaceremover == "on":      ##> এই লাইনটি চেক করে যে কি 'extraspaceremover' চেকবক্সটি "on" হয়েছে কিনা।
        analyzertxt1 = " "  #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        
        for index,elment in enumerate(inputtxt):  #এই লুপটি চালু করে সাধারণভাবে প্রদত্ত 'inputtxt' টেক্সটের অক্ষর পরিসংখ্যান করে।
            if not (inputtxt[index]  == " " and inputtxt[index + 1] == " "): #> লুপের মধ্যে, যদি বর্তমান অক্ষর একটি স্পেস (" ") এবং পরবর্তী অক্ষরটি আবার স্পেস হয়।
                analyzertxt1 += elment
       
        allitemindics = {'Punctuations':' Your Removed Extra Space text : ','analyzed_text1':analyzertxt1, 'cong':congra}   #অতিরিক্ত স্পেস মুছে ফেলা হয়ে গেলে, নতুন বানানো ডিকশনারি তৈরি করা হয়। 'analyzed_text1' কী-তে আপনার বিশ্লেষণ করা টেক্সট থাকবে (analyzertxt1)।
        return render(request,'analyze12.html',allitemindics)    #সর্বশেষে, নতুন তৈরি ডিকশনারির ডেটা দিয়ে 'analyze12.html' নামক একটি HTML টেমপ্লেটে তথ্য প্রদর্শন করা হয়। 
        
        
        
        
    elif charcount == "on":
        charcountout = len(inputtxt)
        
        allitemindics = {'Punctuations':' Your Charcount in the text : ','analyzed_textchar':f'-> Your charcount is  = {charcountout}', 'cong':congra}   #অতিরিক্ত স্পেস মুছে ফেলা হয়ে গেলে, নতুন বানানো ডিকশনারি তৈরি করা হয়। 'analyzed_text1' কী-তে আপনার বিশ্লেষণ করা টেক্সট থাকবে (analyzertxt1)।
        return render(request,'analyze12.html',allitemindics)
        
    else:
        return HttpResponse("Please 'on' the 'conditions' choice one !")
    
    
    
    
        
    
    # return HttpResponse()



def about(request):
    return render(request,'about.html')
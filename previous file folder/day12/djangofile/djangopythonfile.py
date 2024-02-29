""" ==================================> adding more Features to textUtils Website <======================"""

from django.http import HttpResponse
from django.shortcuts import render





def index12(request):
    return render(request,'indess.html')



def analyze12(request):
    inputtxt = request.GET.get('text','default')   # ei line ta output nibe
    
    #checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps =  request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')
    
    
    
    
    
    congra = "->  Congratulations!  <-"
    
    if removepunc == "on":
        punctuations = '''.,?!:;'"()[]{}-_./-&$#@^*%'''
        analyzertxt1 = " "   #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        
        for elment in inputtxt:
            if elment not in punctuations:
                analyzertxt1 = analyzertxt1 + elment
        
        allitemindics = {'Punctuations':'# Your Punctuations Analyzed text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
                
    elif fullcaps == "on":
        analyzertxt1 = ""  #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        for elment in inputtxt:
            analyzertxt1 = analyzertxt1 + elment.upper()
        allitemindics = {'Punctuations':'# Your Upper Case text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
    
    elif newlineremover == "on":
        analyzertxt1 = ""
        for elment in inputtxt:
            if elment != '\n':
                analyzertxt1 = analyzertxt1 + elment
        allitemindics = {'Punctuations':'# Your  Removed Newline text :',"analyzed_text1": analyzertxt1, 'cong':congra}
        return render(request,'analyze12.html', allitemindics)
    
    elif  extraspaceremover == "on":      ##> এই লাইনটি চেক করে যে কি 'extraspaceremover' চেকবক্সটি "on" হয়েছে কিনা।
        analyzertxt1 = " "  #> প্রথমে analyzertxt1 নামে একটি খালি স্ট্রিং তৈরি করা হয়।
        
        for index,elment in enumerate(inputtxt):  #এই লুপটি চালু করে সাধারণভাবে প্রদত্ত 'inputtxt' টেক্সটের অক্ষর পরিসংখ্যান করে।
            if not (inputtxt[index]  == " " and inputtxt[index + 1] == " "): #> লুপের মধ্যে, যদি বর্তমান অক্ষর একটি স্পেস (" ") এবং পরবর্তী অক্ষরটি আবার স্পেস হয়।
                analyzertxt1 += elment
       
        allitemindics = {'Punctuations':'#Your Removed Extra Space text : ','analyzed_text1':analyzertxt1, 'cong':congra}   #অতিরিক্ত স্পেস মুছে ফেলা হয়ে গেলে, নতুন বানানো ডিকশনারি তৈরি করা হয়। 'analyzed_text1' কী-তে আপনার বিশ্লেষণ করা টেক্সট থাকবে (analyzertxt1)।
        return render(request,'analyze12.html',allitemindics)    #সর্বশেষে, নতুন তৈরি ডিকশনারির ডেটা দিয়ে 'analyze12.html' নামক একটি HTML টেমপ্লেটে তথ্য প্রদর্শন করা হয়। 
        
        
        
        
    elif charcount == "on":
        charcountout = len(inputtxt)
        
        allitemindics = {'Punctuations':'#Your Charcount in the text : ','analyzed_textchar':f'-> Your charcount is  = {charcountout}', 'cong':congra}   #অতিরিক্ত স্পেস মুছে ফেলা হয়ে গেলে, নতুন বানানো ডিকশনারি তৈরি করা হয়। 'analyzed_text1' কী-তে আপনার বিশ্লেষণ করা টেক্সট থাকবে (analyzertxt1)।
        return render(request,'analyze12.html',allitemindics)
        
    else:
        return HttpResponse("Please 'on' the 'conditions' choice one !")
    
    
        
    
    # return HttpResponse()

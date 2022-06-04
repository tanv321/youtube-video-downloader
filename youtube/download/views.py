from django.shortcuts import render, redirect
from django.contrib import messages
from pytube import YouTube


# Create your views here.
# defining function
def youtube(request):
  
    if request.method == 'POST':
        
        txt = request.FILES.get('uploaded1', False)
        if txt:
            content = txt.read()
            content  = content.decode('utf-8')
            link = content
        else:
            link = request.POST['link']
        

        jump_to = 1
        link_order = ""
        while jump_to < len(link):
            link_order = ""
            for j in range(jump_to, len(link)):
                if link[j] == " ":
                    while(link[j+1] == " "):
                        j+=1
                    
                    jump_to = j+1
                    break
                else:
                    link_order+=link[j]
                    jump_to = j+1

            video = YouTube(link_order)
            stream = video.streams.get_highest_resolution()
            stream.download()

    

  
        return render(request, 'download/youtube.html')
    return render(request, 'download/youtube.html')
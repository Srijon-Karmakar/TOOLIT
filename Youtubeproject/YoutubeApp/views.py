# views.py
from django.shortcuts import render
from django.http import HttpResponse
import yt_dlp as youtube_dl
from .forms import DownloadForm
import re


def facebook(request):
    return render(request, 'facebook.html')  # Adjust the template name as necessary

def instagram(request):
    return render(request, 'instagram.html')  # Adjust the template name as necessary

def about(request):
    return render(request, 'about.html')  # Adjust the template name as necessary

def contact(request):
    return render(request, 'contact.html')  # Create this template





def youtube(request):
    form = DownloadForm(request.POST or None)


    if form.is_valid():
        video_url = form.cleaned_data.get("url")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        
        if not re.match(regex, video_url):
            return HttpResponse('Enter a correct URL.')

        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(video_url, download=False)

            video_audio_streams = []
            for m in meta['formats']:
                file_size = m.get('filesize')
                if file_size is not None:
                    file_size = f'{round(int(file_size) / 1000000, 2)} mb'
                else:
                    file_size = 'Unknown size'

                resolution = 'Audio'
                if m.get('height') is not None:
                    resolution = f"{m['height']}x{m['width']}"
                
                video_audio_streams.append({
                    'resolution': resolution,
                    'extension': m['ext'],
                    'file_size': file_size,
                    'video_url': m['url']
                })

            video_audio_streams = video_audio_streams[::-1]

            context = {
                'form': form,
                'title': meta['title'],
                'streams': video_audio_streams,
                'description': meta.get('description', 'No description available'),
                'likes': meta.get('like_count', 0),
                'dislikes': meta.get('dislike_count', 0),
                'thumb': meta['thumbnails'][3]['url'] if len(meta['thumbnails']) > 3 else '',
                'duration': round(int(meta['duration']) / 60, 2),
                'views': f'{int(meta["view_count"]):,}'
            }
            return render(request, 'download_video.html', context)

        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')

    return render(request, 'youtube.html', {'form': form})
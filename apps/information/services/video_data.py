import string
import random
import yt_dlp
from django.core.validators import URLValidator


def validate_link(link):
    url_validator = URLValidator()
    url_validator(link)
    return link


def generate_letters(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def cover_video(video_url):
    if '&' in video_url:
        video_url = video_url.split('&')[0]

    title = generate_letters()
    ydl_opts = {
        'skip_download': True,
        'writethumbnail': True,
        'outtmpl': f'media/video/cover/{title}.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return f'video/cover/{title}.webp'

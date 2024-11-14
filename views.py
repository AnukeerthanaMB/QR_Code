from django.shortcuts import render
from core import settings
import qrcode
import time

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        img = qrcode.make(data)
        img_name = 'qr' + str(time.time()) + '.png'
        img.save(f'{settings.BASE_DIR}/static/{img_name}')
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')



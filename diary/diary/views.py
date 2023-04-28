# diary/views.py

import datetime
import os
from django.shortcuts import render, redirect
from .models import DiaryEntry

def diary(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        text = request.POST.get('text')
        dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        file_name = dt.strftime('%Y-%m-%d.txt')
        file_path = os.path.join('diary', 'entries', file_name)
        if os.path.exists(file_path):
            with open(file_path, 'a') as f:
                f.write(text)
        else:
            with open(file_path, 'w') as f:
                f.write(text)
        entry = DiaryEntry(file_name=file_name, date=date, text=text)
        entry.save()
        return redirect('diary')
    else:
        return render(request, 'diary.html')


def diary(request):
    # POSTでデータを受け取る処理
    # ...
    # DiaryEntryモデルから全ての日記を取得する
    entries = DiaryEntry.objects.all()
    # diary.htmlにentriesを渡す
    return render(request, 'diary.html', {'entries': entries})
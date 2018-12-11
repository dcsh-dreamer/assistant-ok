from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Journal

# Create your views here.
# 日誌列表
class JournalList(ListView):
    model = Journal
    ordering = ['-id']      # 依 id 欄位反向排序(新的在前面)

# 新增日誌
class JournalCreate(CreateView):
    model = Journal
    fields = ['content']            # 自動產生表單時僅顯示 content 欄位
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 修改日誌
class JournalUpdate(UpdateView):
    model = Journal
    fields = ['content']            # 自動產生表單時僅顯示 content 欄位
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 刪除日誌
class JournalDelete(DeleteView):
    model = Journal
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'confirm_delete.html'
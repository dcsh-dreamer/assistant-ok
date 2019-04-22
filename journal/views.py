from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# 日誌列表
class JournalList(LoginRequiredMixin, ListView):
    model = Journal
    ordering = ['-id']      # 依 id 欄位反向排序(新的在前面)
    paginate_by = 3         # 設定每頁最多顯示的資料筆數

# 新增日誌
class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['content']            # 自動產生表單時僅顯示 content 欄位
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 修改日誌
class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = ['content']            # 自動產生表單時僅顯示 content 欄位
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'form.html'

# 刪除日誌
class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    success_url = '/journal/'       # 操作成功後重新導向日誌列表頁面
    template_name = 'confirm_delete.html'
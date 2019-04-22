from django.db import models
import pytz

# Create your models here.
# 支出紀錄
class Expense(models.Model):
    CATE_UNDEFINED      = 0
    CATE_EATING         = 1
    CATE_CLOTHING       = 2
    CATE_TRANSPORTATION = 3
    CATE_EDUCATION      = 4
    CATE_ENTERTAINMENT  = 5
    CATE_OTHER          = 99

    CATEGORY_CHOICES = (
      (CATE_UNDEFINED,      "未分類"),
      (CATE_EATING,         "飲食"),
      (CATE_CLOTHING,       "衣服"),
      (CATE_TRANSPORTATION, "交通"),
      (CATE_EDUCATION,      "教育"),
      (CATE_ENTERTAINMENT,  "娛樂"),
      (CATE_OTHER,          "其它"),
    )

    # 欄位定義
    item     = models.CharField('項目', max_length=30)
    category = models.IntegerField('支出類別', default=0, choices=CATEGORY_CHOICES)
    amount   = models.IntegerField('支出金額', default=0)
    time     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {} : {} 元".format(
            self.time.astimezone(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S'),
            self.item, 
            self.amount
        )
from django.contrib import admin
from app.models import BookInfo, PersonInfo


# django admin 对数据库进行操作
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete', 'create_data', 'update_date']


admin.site.register(BookInfo, BookInfoAdmin)


class PersonInfoAdmin(admin.ModelAdmin):
    list_display = ['pname', 'pgender', 'isDelete', 'pcomment', 'create_data', 'update_date']


admin.site.register(PersonInfo, PersonInfoAdmin)

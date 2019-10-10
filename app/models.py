from django.db import models


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # 指定btitle对应的字段名为title
    # 没有主键时，自动创建主键id
    btitle = models.CharField(max_length=20, verbose_name="书名")
    # YYYY-mm-dd
    bpub_date = models.DateField(verbose_name="发布日期")  # 发布日期
    bread = models.PositiveIntegerField(default=0, verbose_name="阅读量")  # 阅读量
    bcomment = models.PositiveIntegerField(default=0, verbose_name="评论量")  # 评论量
    isDelete = models.BooleanField(default=False, verbose_name="逻辑删除", db_column="is_delete")  # 逻辑删除
    # 创建时，添加时间。
    create_data = models.DateTimeField(auto_now_add=True, null=True, blank=False, verbose_name="创建时间")
    # 修改时间，当修改数据时，生成新的时间。
    update_date = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        db_table = "book_info"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.btitle}"


# 定义人物模型类PersonInfo
class PersonInfo(models.Model):
    pname = models.CharField(max_length=20, verbose_name="人物姓名")
    pgender = models.BooleanField(default=True, verbose_name="人物性别")
    isDelete = models.BooleanField(default=False, verbose_name="逻辑删除")
    # 人物描述，数据库中的字段可以为空，但后台管理页面的输入框不能为空
    pcomment = models.CharField(max_length=200, null=True, blank=False)
    create_data = models.DateTimeField(auto_now_add=True, null=True, blank=False, verbose_name="创建时间")
    # 修改时间，当修改数据时，生成新的时间。
    update_date = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        db_table = "person_info"
        verbose_name = "人物信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.pname}"

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Author(models.Model):
#     """博客作者模型"""
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#     descript = models.TextField()
#
#     def __unicode__(self):
#         return u'%s' % (self.name)

class Blog(models.Model):
    """博客模型"""
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING) # 一对一外键，关联作者模型
    blog_type = models.ForeignKey('BlogType',on_delete=models.DO_NOTHING)
    content = models.TextField() #长文本字段，可以写很多内容

    create_time = models.DateTimeField(auto_now_add=True) #日期，新增自动写入
    last_update_time = models.DateTimeField(auto_now=True) #日期，修改自动更新
    recommend = models.BooleanField(default=False) #布尔字段，用于标记是否推荐博文

    class Meta: #模型的元数据(模型的子类)
        # 排序
        ordering=['-create_time']

    def __str__(self):
        return "<Blog>:%s" % self.title

class BlogType(models.Model):
    """博客分类"""
    type_name = models.CharField(max_length=15)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_name


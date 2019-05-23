import xadmin
from xadmin import views
from label.models import labelitem, CatagoryS, CatagoryF

class labelItemAdmin(object):
    list_display = ['recorder', 'text', 'cat_id']  # 展示的内容
    search_fields = ['text','mid']  # 搜索时按以上字段搜索
    list_filter = ['cat_id','time','recorder','cat_id__catagory_f']  # 筛选器内容
    readonly_fields = ['recorder', 'image', 'mid', 'text', 'time',]
    ordering = ['-time']

class CatSAdmin(object):
    list_display = ['id', 'name', 'catagory_f']

class CatFAdmin(object):
    list_display = ['id', 'name']

xadmin.site.register(labelitem, labelItemAdmin)
xadmin.site.register(CatagoryF, CatFAdmin)
xadmin.site.register(CatagoryS, CatSAdmin)

class GlobalSettings(object):
    # 修改title
    site_title = '图文标注平台'
    # 修改footer
    site_footer = '图文标注平台'
    # 收起菜单
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)
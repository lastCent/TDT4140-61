from django.contrib import admin
import quiz.models as m

#admin.site.register(m.Question)
admin.site.register(m.Person)
admin.site.register(m.Course)
admin.site.register(m.CourseMembers)
admin.site.register(m.Result)
admin.site.register(m.Exercise)
admin.site.register(m.Question)
admin.site.register(m.ThemeTag)


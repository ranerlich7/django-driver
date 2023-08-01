from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin

from .models import Driver, Race, Team


# We are adding to driver the usual UserAdmin.
# but we need to add our fields like  'age'
# so we add this code
fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'age', 'team')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Driver, UserAdmin)

###############
# These are optional steps to show models in admin
# you can just register simply by:
# admin.site.register(Race)
# admin.site.register(Team)

# new RaceAdmin
# race admin we use filter_horizonal which is good for many to many.


class RaceAdmin(ModelAdmin):
    filter_horizontal = ('driver',)


admin.site.register(Race, RaceAdmin)

# new TeamAdmin
# in team we can use inline class which is good for foreign key


class DriverInline(admin.TabularInline):
    model = Driver
    fields = ['username']
    extra = 0  # Set the number of empty book forms to display


class TeamAdmin(admin.ModelAdmin):
    inlines = [DriverInline]


admin.site.register(Team, TeamAdmin)

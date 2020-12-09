from django.contrib import admin
from .models import JobOrganization, JobListing, JobApplicant, JobOffersMade, Skill, JobListingSkill, JobApplicantSkill

# Register your models here.
admin.site.register(JobOrganization)
admin.site.register(JobListing)
admin.site.register(JobApplicant) 
admin.site.register(JobOffersMade)
admin.site.register(Skill)
admin.site.register(JobListingSkill) 
admin.site.register(JobApplicantSkill) 
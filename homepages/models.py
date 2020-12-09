from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class JobOrganization(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.CharField(max_length=25)
    company_phone = models.CharField(max_length=10)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=25)
    size = models.CharField(max_length=2)
    sector = models.CharField(max_length=2)

    def __str__(self):
        return (self.company_name)

class JobListing(models.Model):
    job_title = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='NULL')
    contracts = models.CharField(max_length=10)
    description = models.CharField(max_length=3000)
    organization = models.ForeignKey(JobOrganization, on_delete=models.CASCADE)

    def __str__(self):
        return (self.job_title)

class JobApplicant(models.Model):
    applicant_email = models.CharField(max_length=25)
    applicant_phone = models.CharField(max_length=10)
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

class Skill(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return (self.skill_name)

class JobOffersMade(models.Model):
    applicant = models.ForeignKey(JobApplicant, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)

    def __str__(self):
        return (self.applicant.first_name + ' ' + self.applicant.last_name + ' ' + self.job_listing.job_title)

class JobListingSkill(models.Model): # linking table between Skill and JobListing Table
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(4)]) # skill level can be between 0 and 4

    def __str__(self):
        return (self.job_listing.job_title + ': ' + self.skill.skill_name + '-' + str(self.skill_level))

class JobApplicantSkill(models.Model): # linking table between Skill and Applicant Table
    applicant = models.ForeignKey(JobApplicant, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(4)])

    def __str__(self):
        return (self.applicant.first_name + ' ' + self.applicant.last_name + ': ' + self.skill.skill_name + '-' + str(self.skill_level))
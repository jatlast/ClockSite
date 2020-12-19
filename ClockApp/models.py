# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.conf import settings
from django.db import models
from django.utils import timezone


# A logging table
class SysLog(models.Model):
    logid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=32, blank=True, null=True)
    inserted = models.DateTimeField(blank=True, null=True)
    exceptxt = models.CharField(max_length=255, blank=True, null=True)
    querytxt = models.CharField(max_length=255, blank=True, null=True)
    errtxt = models.CharField(max_length=255, blank=True, null=True)
    msgtxt = models.CharField(max_length=255, blank=True, null=True)
    key1 = models.CharField(max_length=32, blank=True, null=True)
    val1 = models.CharField(max_length=32, blank=True, null=True)
    key2 = models.CharField(max_length=32, blank=True, null=True)
    val2 = models.CharField(max_length=32, blank=True, null=True)
    key3 = models.CharField(max_length=32, blank=True, null=True)
    val3 = models.CharField(max_length=32, blank=True, null=True)
    key4 = models.CharField(max_length=32, blank=True, null=True)
    val4 = models.CharField(max_length=32, blank=True, null=True)
    key5 = models.CharField(max_length=32, blank=True, null=True)
    val5 = models.CharField(max_length=32, blank=True, null=True)
        
    class Meta:
        managed = True
        db_table = 'SysLog'
        get_latest_by = 'logid'
        ordering = ["-logid"]

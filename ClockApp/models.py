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


# Customer table
class Customer(models.Model):
    cID = models.IntegerField(db_column='cID', primary_key=True) # Unique ID
    cDateCreated = models.DateTimeField(db_column='cDateCreated', blank=True, null=True) # Date customer was added to the system (set by DB)
    cName = models.CharField(db_column='cName', max_length=64, blank=False, null=False) # Customer's full name
    cPhone = models.CharField(db_column='cPhone', max_length=10, blank=False, null=False) # 10 digit US phone number
    cGender = models.CharField(db_column='cGender', max_length=1, blank=False, null=False) # 'M' or 'F'
    cDOB = models.DateTimeField(db_column='cDOB', blank=True, null=True) # Customer's date of birth (may generate mostly NULLs)
    cEmail = models.CharField(db_column='cEmail', max_length=128, blank=False, null=False) # Customer's email address (and name for system login)
    cPW = models.CharField(db_column='cPW', max_length=16, blank=False, null=False) # Password
    cAddress1 = models.CharField(db_column='cAddress1', max_length=64, blank=False, null=False) # Customer's street address
    cAddress2 = models.CharField(db_column='cAddress2', max_length=16, blank=False, null=False) # Customer's Apt, Unit, Suite, etc
    cCity = models.CharField(db_column='cCity', max_length=16, blank=False, null=False) # Customer's City
    cState = models.CharField(db_column='cState', max_length=2, blank=False, null=False) # Customer's State
    cZip = models.CharField(db_column='cZip', max_length=7, blank=False, null=False) # Customer's Zip Code

    class Meta:
        managed = True
        db_table = 'Customer'
        get_latest_by = 'cID'
        ordering = ["-cName"]

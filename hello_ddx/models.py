from django.db import models

class Ddxlist(models.Model):
  abnormal_value = models.CharField(max_length = 50)
  bt_category = models.CharField(max_length = 30 , default = 'None')
  upperzero_lowerone = models.IntegerField(default = 0)
  true_up = models.BooleanField(default = False)

  def __str__(self):
    ddx = self.abnormal_value
    ddx += '(「'+self.bt_category+'」'
    if self.true_up == False:
      ddx += '「down」)'
    else:
      ddx += '「up」)'
    return ddx

  
class Firstddxlist(models.Model):
  ddxlist = models.ForeignKey(Ddxlist,on_delete = models.CASCADE)
  differential_list_first = models.CharField(max_length = 50)
  first_bt_category = models.CharField(max_length = 30)
  first_true_up = models.BooleanField(default = False)

  def __str__(self):
    first = self.differential_list_first
    first += '(「'+self.first_bt_category+'」'
    if self.first_true_up == False:
      first += '「down」)'
    else:
      first += '「up」)'

    return first

class Secondddxlist(models.Model):
  firstddxlist = models.ForeignKey(Firstddxlist,on_delete = models.CASCADE)
  differential_list_second = models.CharField(max_length = 50)
  second_bt_category = models.CharField(max_length = 30)
  second_true_up = models.BooleanField(default = False)

  def __str__(self):
    second = self.differential_list_second
    second += '(「'+self.second_bt_category+'」'
    if self.second_true_up == False:
      second += '「down」)'
    else:
      second += '「up」)'
    
    return second

class Thirdddxlist(models.Model):
  secondddxlist = models.ForeignKey(Secondddxlist,on_delete = models.CASCADE)
  differential_list_third = models.CharField(max_length = 50)
  third_bt_category = models.CharField(max_length = 30)
  third_true_up = models.BooleanField(default = False)

  def __str__(self):
    third = self.differential_list_third
    third += '(「'+self.third_bt_category+'」'
    if self.third_true_up == False:
      third += '「down」)'
    else:
      third += '「up」)'
    
    return third
# Create your models here.

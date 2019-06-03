from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    location_x = models.FloatField(null=True, blank=True, default=None)
    location_y = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.user.username


class Spot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location_x = models.FloatField(blank=True, null=True)
    location_y = models.FloatField(blank=True, null=True)
    near_station = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True, blank=True)
    like = models.IntegerField(default=0)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    content = models.TextField()
    picture = models.ImageField(blank=True, null=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.spot.name + '-' + self.user.username


class Station(models.Model):
    class Meta:
        ordering = ['fr_code']

    STATION_NUM_CHOICES = [
        ('1', '1호선'),
        ('2', '2호선'),
        ('3', '3호선'),
        ('4', '4호선'),
        ('5', '5호선'),
        ('6', '6호선'),
        ('7', '7호선'),
        ('8', '8호선'),
        ('9', '9호선'),
        ('A', '공항철도'),
        ('B', '분당선'),
        ('E', '전대에버라인'),
        ('G', '경춘선'),
        ('I', '인천1호선'),
        ('I2', '인천2호선'),
        ('K', '경의중앙선'),
        ('KK', '경강선'),
        ('S', '신분당선'),
        ('SU', '수인선'),
        ('T', '테스트'),
        ('U', '의정부경전철'),
        ('UI', '우이신설선')
    ]
    line_num = models.CharField(
        max_length=3,
        choices=STATION_NUM_CHOICES
    )
    station_cd = models.CharField(max_length=4)
    station_nm = models.CharField(max_length=20)
    fr_code = models.CharField(max_length=5)
    transfer_count = models.IntegerField(default=1)
    naver_cd = models.CharField(max_length=10, default='', blank=True)
    head_station = models.CharField(max_length=4)
    tail_station = models.CharField(max_length=4)
    head_time = models.FloatField(null=True)
    tail_time = models.FloatField(null=True)
    tag_count = models.IntegerField(default=0)

    def __str__(self):
        return self.station_nm + '({})'.format(self.line_num)

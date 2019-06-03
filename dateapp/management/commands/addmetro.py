from django.core.management.base import BaseCommand, CommandError
from dateapp.models import *
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        Station.objects.all().delete()
        with open('asset/metro.csv', 'r', encoding='utf-8') as f:
            rdr = csv.reader(f)
            for line in rdr:
                (line_num, station_cd, station_nm, fr_code, transfer_count, naver_cd, head_time, tail_time, id,
                 tag_count, head_station, tail_station) = line
                if head_time == '':
                    head_time = None
                if tail_time == '':
                    tail_time = None
                Station.objects.create(
                    line_num=line_num,
                    station_cd=station_cd,
                    station_nm=station_nm,
                    fr_code=fr_code,
                    transfer_count=int(transfer_count),
                    naver_cd=naver_cd,
                    head_time=head_time,
                    tail_time=tail_time,
                    tag_count=int(tag_count),
                    head_station=head_station,
                    tail_station=tail_station,
                )

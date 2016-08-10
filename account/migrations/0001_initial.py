# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 08:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mtm.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('남', '남'), ('여', '여')], default='', max_length=20, verbose_name='성별')),
                ('lnglat', models.CharField(max_length=20, verbose_name='멘토 위치')),
                ('highschool', models.CharField(max_length=40, verbose_name='출신 고등학교')),
                ('university', models.CharField(max_length=40, verbose_name='재학중인 대학교')),
                ('major', models.CharField(choices=[('간호대학', '간호대학'), ('건축학과', '건축학과'), ('경영대학', '경영대학'), ('농경제사회학부', '농경제사회학부'), ('사회과학계열', '사회과학계열'), ('심리학과', '심리학과'), ('소비자아동학부', '소비자아동학부'), ('의류학과', '의류학과'), ('인문계열', '인문계열'), ('언어학과', '언어학과'), ('교육학과', '교육학과'), ('국어교육과', '국어교육과'), ('물리교육과', '물리교육과'), ('사회교육과', '사회교육과'), ('생물교육과', '생물교육과'), ('역사교육과', '역사교육과'), ('영어교육과', '영어교육과'), ('지구과학교육과', '지구과학교육과'), ('지리교육과', '지리교육과'), ('체육교육과', '체육교육과'), ('화학교육과', '화학교육과'), ('수학교육과', '수학교육과'), ('물리천문학부', '물리천문학부'), ('바이오시스템소재학부', '바이오시스템소재학'), ('산림과학부', '산림과학부'), ('생명과학부', '생명과학부'), ('수리과학부', '수리과학부'), ('식물생산과학부', '식물생산과학부'), ('식품영양학과', '식품영양학과'), ('응용생물화학부', '응용생물화학부'), ('화학부', '화학부'), ('건설환경공학부', '건설환경공학부'), ('기계항공공학부', '기계항공공학부'), ('산업공학과', '산업공학과'), ('식품동물생명공학부', '식품동물생명공학부'), ('재료공학부', '재료공학부'), ('전기정보공학부', '전기정보공학부'), ('조경지역시스템공학부', '조경지역시스템공학부'), ('조선해양공학과', '조선해양공학과'), ('컴퓨터공학부', '컴퓨터공학부'), ('화학생물공학부', '화학생물공학부'), ('의예과', '의예과')], default='', max_length=40, verbose_name='전공')),
                ('grade', models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년 이상', '4학년 이상')], default='', max_length=40, verbose_name='학년')),
                ('career', models.TextField(verbose_name='약력')),
                ('intro', models.TextField(verbose_name='기타 소개')),
                ('image', models.ImageField(blank=True, null=True, upload_to=mtm.utils.random_name_upload_to, verbose_name='멘토 소개 사진')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mentorinfo',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
    ]

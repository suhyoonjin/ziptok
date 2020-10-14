from django.db import models

# Create your models here.

class User(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField(max_length=24,verbose_name = '사용자명')
    password = models.CharField(max_length=200,verbose_name = '비밀번호')
    name = models.CharField(max_length=50,verbose_name = '이름',null = True)
    birth = models.CharField(max_length=10,verbose_name = '생년월일',null = True)
    email = models.CharField(max_length=50,verbose_name = '이메일',null = True)
    phone_num = models.CharField(max_length=15,verbose_name = '휴대폰번호',null = True)
    addr = models.CharField(max_length=50,verbose_name = '주소',null = True)
    rcmd_id = models.CharField(max_length=24,verbose_name = '추천인아이디',null = True)
    is_expert = models.CharField(max_length=10,verbose_name = '전문가여부',null = True)
    registered_dttm = models.DateTimeField(auto_now_add=True,verbose_name='등록시간')
    #저장되는 시점의 시간을 자동으로 삽입해준다.

    def __str__(self):  # 이 함수 추가
        return self.username  # User object 대신 나타낼 문자

    class Meta: #메타 클래스를 이용하여 테이블명 지정
       db_table = 'user'

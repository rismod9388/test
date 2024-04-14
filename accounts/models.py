from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password, email, name, nickname, **extra_fields):
        user = self.model(
            user_id = user_id,
            email = email,
            name = name,
            nickname=nickname,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, user_id, password, email=None,  name=None, nickname=None):
        user = self.create_user(user_id, password, email,name,nickname)
        user.is_superuser = True
        # user.is_staff = True
        # user.is_admin = True
        # user.level = 0
        user.save(using=self._db)
        return user  
#회원등록 모델
class Users(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager() 

    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일",null=True, unique=True)
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    nickname = models.CharField(max_length=128, verbose_name="닉네임", null=True)
    registered_dttm = models.DateField(auto_now_add=True, verbose_name="등록시간")

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_id
    def get_by_natural_key(self, user_id):
        return self.__class__.objects.get(user_id=user_id)
    class Meta:
        db_table = "users"
        verbose_name ="사용자"
        verbose_name_plural = "사용자"


from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_email, user_password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        username = extra_fields.pop('username', None)
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(email=user_email, **extra_fields)
        user.set_password(user_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_email, user_password, **extra_fields)
    


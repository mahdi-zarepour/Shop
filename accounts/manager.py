from django.contrib.auth.models import (
    BaseUserManager,
)


class MyUserManager(BaseUserManager): # The model manager class is responsible for how the user is created.

    def create_user(self, email, phone, password):
        if not [email, phone]:
            raise ValueError('users must have Email and Phone')
            
        # self.model: User Model
        user = self.model(
           email=self.normalize_email(email), # set email to lower case and normal
           phone=phone,
        )
        user.set_password(password) # Hash Password
        user.save(using=self._db)
        return user


    def create_normal_user(self, email, phone, password): # create normal user
        user = self.create_user(email, phone, password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email, phone, password): # create super user
        user = self.create_user(email, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
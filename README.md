# Django Student & Teacher Rest-Auth Boilerplate

### Thanks
* allauth
* auth token
* corsheaders
* rest_auth
* rest_framework

***


For Signup ```http://127.0.0.1:8000/user/rest-auth/signup```

Allways teacher will be ```is_teacher: !is_student```

```
{
    "username": "farjanul",
    "email": "email@email.com",
    "first_name": "Farjanul",
    "last_name": "Nayem",
    "password1": "hTdg62YUgGS",
    "password2": "hTdg62YUgGS",
    "is_student": true,
    "is_teacher": false
}
```

for login ```http://127.0.0.1:8000/rest-auth/login/```

```
{
    "username": "farjanul",
    "password2": "hTdg62YUgGS"
}
```

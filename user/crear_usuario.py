from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()


usuarios = [('user1','contraseña1'),
('user1','contraseña1'),
('user2','contraseña1'),
('user3','contraseña1'),
('user4','contraseña1'),
('user5','contraseña1'),
('user6','contraseña1'),
('user7','contraseña1'),
('user8','contraseña1')]

for item in usuarios:
    item = User.objects.create_user(item[0])
    item.set_password(item[1])
    item.save()

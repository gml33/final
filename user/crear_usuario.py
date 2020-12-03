from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()
item = User.objects.create_user('Tomas')
item.set_password('contraseña1')
item.last_name = 'Shelby'
item.save()



'''


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
    item = User.objects.create_user('mayra')
    item.set_password('contraseña1')
    item.save()
'''





item = User.objects.create_user('mayra')
item.set_password('contraseña1')
item.last_name = 'bruzzone'
item.save()

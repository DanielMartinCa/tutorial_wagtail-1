from django.conf import settings

settings.configure(DEBUG=True)

from personalempresa.models import PersonalEmpresa

for p in PersonalEmpresa.objects.all():
    print(p)
    
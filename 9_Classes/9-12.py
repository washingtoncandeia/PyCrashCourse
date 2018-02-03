##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
# Faça você mesmo, p.249
# 9.12 - Vários módulos
##-------------------------------

from user import User
from privileges import Privileges

admi = User('mendoim', 'brown', 8)
print(admi.describe_user())

ad = Privileges()
ad.show_privileges()
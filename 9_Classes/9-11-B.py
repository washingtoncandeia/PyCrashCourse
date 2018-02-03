##-------------------------------
# Cap.9 - Classes
# Python Crash Course
# Autor: Washington Candeia
##-------------------------------

# Faça você mesmo, p.249
# 9.10 - Importando Restaurant

from admin import Privileges, Admin

eu = Admin('washington', 'araujo', 34)
print(eu.describe_user())
eu.privileges.show_privileges()

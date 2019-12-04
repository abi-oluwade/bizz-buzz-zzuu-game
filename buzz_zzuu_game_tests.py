from buzz_zzuu_game_functions import *


###### Make bizzzuu Test ########
print("testing_bizzzuu with 30. Expected --> 'True'")
print(bizzzuu(30) == True)
print('got:', bizzzuu(30))

print("testing_bizzzuu with 29. Expected --> 'False'")
print(bizzzuu(30) == False)
print('got:', bizzzuu(29))

###### Make buzz Test ########
print("testing_buzz with 10. Expected --> 'True'")
print(buzz(30) == True)
print('got:', buzz(10))

print("testing_buzz with 9. Expected --> 'False'")
print(buzz(30) == False)
print('got:', buzz(9))

###### Make zzuu Test ########
print("testing_zzuu with 12. Expected --> 'True'")
print(zzuu(30) == True)
print('got:', zzuu(12))

print("testing_zzuu with 8. Expected --> 'False'")
print(zzuu(30) == False)
print('got:', zzuu(8))
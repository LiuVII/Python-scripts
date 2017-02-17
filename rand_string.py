import random
import string


n = int(input('How many strings need to be generated? ').strip())
lmax = int(input('What is maximum length? ').strip())
unique = int(input('Are string need to be unique (1 - yes/0 - no)? ').strip()) 
sep_l = input('Choose sep for output ')
lst = []
for i in range(n):
	l = random.randrange(1, lmax + 1)
	s = ''.join(random.choice(string.ascii_uppercase) for _ in range(l))
	if unique == 0 or (unique == 1 and s not in lst):
		lst.append(s)
	else:
		i -= 1
print(*lst, sep=sep_l)

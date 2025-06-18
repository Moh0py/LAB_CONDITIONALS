

wieght = float(input('wieght: '))
height = float(input('height: '))
bmi=  ( wieght / height ** 2) 
print(f'your bmi is {round(bmi,2)}')

if bmi > 25:
  print('You are overwieght you need to work out more and watch your diet')

elif bmi >= 18.5:
    print('You are fit & healthy.')
else: 
    print('You are underweight. Watch your health.')

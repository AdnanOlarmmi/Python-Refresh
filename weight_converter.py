weight = int(input('Weight: '))
weightUnit = input('(K)g or (L)bs: ')
conversionRate = 0.45

if weightUnit.lower() == 'k':
    print(f'Weight in L: {weight / conversionRate}L')
elif weightUnit.lower() == 'l':
    print(f'Weight in Kg: {weight * conversionRate}Kg')

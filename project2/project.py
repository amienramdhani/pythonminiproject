def search(arr, x):
    a = 0
    for i in range(len(arr)):
        if arr[i] >= x:
            a += 1
    return a


arr = [241, 162, 212, 220, 206, 152, 134,
       128, 137, 143, 124, 125, 107, 149, 155]
x = 170
print('jumlah warga yang tingginya 170 cm ', search(arr, x), 'orang')


def searchGender(male, y):
    a = 0
    for i in range(len(male)):
        if male[i] >= y:
            a += 1
    return a


male = [241, 162, 212, 220, 206, 152]
y = 170
print('Laki-laki yang memiliki tinggi lebih dari 170 cm sebanyak',
      searchGender(male, y), ' orang')


def searchGender2(female, y):
    a = 0
    for i in range(len(female)):
        if female[i] >= y:
            a += 1
    return a


female = [134, 128, 137, 143, 124, 125, 107, 149, 155]
y = 170
print('Perempuan yang memiliki tinggi lebih dari 170 cm sebanyak',
      searchGender2(female, y), ' orang')

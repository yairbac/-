# Functions
def exercise_1(d,m,y):
    t = 'The date is valid'
    f = 'invalid date'
    if 100 <= y <= 2100:
        if m in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= d <= 31:
                return t
            else:
                return f
        elif m in [4, 6, 9, 11]:
            if 1 <= d <= 30:
                return t
            else:
                return f
        elif m == 2:
            if 1 <= d <= 28:
                return t
            else:
                if y % 4 == 0:
                    if y % 100 == 0:
                        if y % 400 == 0:
                            return t
                        else:
                            return f
                    else:
                        return f
                else:
                    return f
        else:
            return f
    else:
        return f
# -------------------------------------------------
def exercise_2(n):
    if 1 <= n <= 10:
        for i in range(n + 1):
            print((n - i) * ' ', end='')
            for j in range(i):
                print('*', end=' ')
            print()
        return''
        pass
    else:
        l = 0
        while l<2:
            n=int(input('Imput number of rows (between 1 and 10): '))
            if 1 <= n <= 10:
                for i in range(n + 1):
                    print((n - i) * ' ', end='')
                    for j in range(i):
                        print('*', end=' ')
                    print()
                break
            else:
                l += 1
                if l == 2:
                    print('3 mistakes, Bye Bye!')
        return ''
#--------------------------------------------------
def exercise_3(n):
    if n>123456787:
        print('The number digits cannot be ascending')
    else:
        def prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            if n == 2:
                return True
        p = n
        n += 1
        while prime(n) is False:
            n += 1
        print('The first prime number greater than', p, 'is:', n)
        # first prime number
        n+=1
        l1 = []
        for i in str(n):
            l1 += [int(i)]
        for i in range(len(l1) - 1):
            if l1[i] >= l1[i + 1]:
                l1[i + 1] = l1[i] + 1
        print('The first number with digits in ascending order as a List is: ', l1)
    return''
#___________________________________________________
def exercise_4(a,b,c):
    a, b, c = int(a), int(b), int(c)
    x = ''
    y = ''
    if a + b <= c or a + c <= b or b + c <= a:
        x = 'Illegal triangle'
    elif a == b == c:
        x = 'Equilateral'
    elif a == b != c or a == c != b or c == b != a:
        x = 'Isosceles'
    else:
        x = 'Scalene'
    if c > a and c > b and a ** 2 + b ** 2 == c ** 2 or b > a and b > c and a ** 2 + c ** 2 == b ** 2 or a > b and a > c and b ** 2 + c ** 2 == a ** 2:
        y = 'Right'
    elif c > a and c > b and a ** 2 + b ** 2 <= c ** 2 or b > a and b > c and a ** 2 + c ** 2 <= b ** 2 or a > b and a > c and b ** 2 + c ** 2 <= a ** 2:
        y = 'Obtuse'
    else:
        y = 'Acute'
    if x == 'Illegal triangle':
        return x
    else:
        print(tuple([x, y]))
        return''


# Display the menu
print("Question numbers:")
print("1. Exercise 1")
print("2. Exercise 2")
print("3. Exercise 3")
print("4. Exercise 4")

# Get user input for exercise choice
question = int(input("Enter your choice (1-4): "))

if question == 1:
    d = int(input('Enter a day: '))
    m = int(input('Enter a month: '))
    y = int(input('Enter a year: '))
    print(exercise_1(d,m,y))
elif question == 2:
    n = int(input('Imput number of rows (between 1 and 10): '))
    print(exercise_2(n))
elif question == 3:
    n = int(input('Enter an integer: '))
    print(exercise_3(n))

elif question == 4:
        a, b, c = input('Enter 3 numbers: ').split( )
        print(exercise_4(a, b, c))
else:
    print("Invalid choice.")

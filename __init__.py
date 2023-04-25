from math_game import add, substract, multiply, divide

def game():
    score = 0
    while True:
        print('======== Menu ========\n1. Add\n2. Substract\n3. Multiply\n4. Divide')
        operation = int(input('Choose an operation: '))
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))
        if operation == 1:
            result = add(num_1, num_2)
        if operation == 2:
            result = substract(num_1, num_2)
        if operation == 3:
            result = multiply(num_1, num_2)
        if operation == 4:
            if divide(num_1,num_2)!="NO":       
                result = divide(num_1, num_2)
            else:
                result="NO"
        if result == answer:
            score += 1
            print('Correct!!')
        elif result=="NO":
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========\n You score is {score}')
    
game()


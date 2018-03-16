##-------------------------------
# Cap.10 - Arquivos e exceções
# Python Crash Course
# Eric Matthes
# Autor: Washington Candeia
# division.py, p.270
##-------------------------------

print("Give two numbers, and I'll divide them")
print("Enter 'q' to quit.")

# Laço while
while True:
    first_number = input('First number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')

    # Bloco try-except
    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero.")

    else:
        print("Answer: " + str(answer))


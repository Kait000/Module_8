def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(1001, 'Any_string'))
print(add_everything_up('New_string', 20.02))
print(add_everything_up(1001, 20.02))

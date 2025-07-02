execute = lambda function, *args: function(*args)

double = lambda value_factor: lambda value: value * value_factor

double = execute(double, 2)

print(double(2))

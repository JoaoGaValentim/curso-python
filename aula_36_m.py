from typing_extensions import Generator


print("Hello, World!")

PI: float = 3.1415
pi_multiply_gen: Generator[float] = (PI * i for i in range(10))

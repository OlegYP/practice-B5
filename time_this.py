import time
import random

def time_this(num_runs):
    def actual_decorator(func):
        import time
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(num_runs):
                ts = time.time()
                return_value = func(*args, **kwargs)
                te = time.time()
                total = total + (te - ts)
            print('=== Average time = {:.2f} sec ==='.format(total / num_runs))
            return return_value
        return wrapper
    return actual_decorator

# укажем сколько раз запустить функцию внутри декоратора
@time_this(5)
def test():
    # имитируем время выполнения функции путем генерации времени задержки в диапазоне от 1 до 4 сек.
   delay = random.randint(1, 4)
   time.sleep(delay)
   # после каждого запуска функции сообщаем сколько времени она реально выполнялась
   print('function test finished with delay {} sec'.format(delay))

if __name__ == "__main__":
    test()

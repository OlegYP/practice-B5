import time
import random

class Timing:
    def __init__(self, function_to_run):
        self.num_runs = 3
        self.func_to_run = function_to_run

    def __call__(self, *args, **kwargs):
        avg = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        fn = self.func_to_run.__name__
        print(
            "[Timing] Среднее время выполнения %s за %s запусков: %.5f секунд" % (
                fn,
                self.num_runs,
                avg
            )
        )
        return self.func_to_run(*args, **kwargs)

@Timing
def test():
    # имитируем время выполнения функции путем генерации времени задержки в диапазоне от 1 до 4 сек.
   delay = random.randint(1, 4)
   time.sleep(delay)
   # после каждого запуска функции сообщаем сколько времени она реально выполнялась
   print('function test finished with delay {} sec'.format(delay))

if __name__ == "__main__":
    test()
import time
import multiprocessing

def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)

if __name__ == '__main__':
    start = time.time()
    names = ['cat', 'dog', 'bird', 'pig']
    pool = multiprocessing.Pool(processes=4)
    pool.map(heavy_work, names)
    pool.close()
    pool.join()

    end = time.time()

    print("수행시간: %f 초" % (end - start))


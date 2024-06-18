import time
import multiprocessing

def heavy_work(name):
    result = 0

    for i in range(4000000):
        result += i

    print('%s done' % name)

if __name__ == '__main__':

    start = time.time()
    procs = []

    process_names = ['cat', 'dog', 'bird', 'bug']

    for i in range(4):

        p = multiprocessing.Process(target=heavy_work, args=(process_names[i], ))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()  # 프로세스가 모두 종료될 때까지 대기

    end = time.time()

    print("수행시간: %f 초" % (end - start))



    
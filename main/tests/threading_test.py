import time
import threading


def heavy_work(name):
    result = 0
    for i in range(4000000):
        result += i
    print('%s done' % name)

if __name__ == '__main__':

    start = time.time()
    threads = []
    process_names = ['cat', 'dog', 'bird', 'bug']

    for i in range(4):
        t = threading.Thread(target=heavy_work, args=(process_names[i], ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()  # 스레드가 종료될 때까지 대기

    end = time.time()

    print("수행시간: %f 초" % (end - start))

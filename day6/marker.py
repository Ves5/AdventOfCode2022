with open('day6/signal.txt') as f:
    signal = f.readline()
    for i in range(0, len(signal) - 3):
        # part 1
        # if len(set([signal[i], signal[i+1], signal[i+2], signal[i+3]])) == 4:
        #     print(i+4)
        #     break
        # part 2
        if len(set([signal[x] for x in range(i, i+14)])) == 14:
            print(i+14)
            break
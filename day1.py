def main():
    # pull text from an txt file
    with open('day1.input.txt', 'r') as f:
        file_text = f.readlines()
        measurements = [int(line.rstrip()) for line in file_text]

        incr = 0
        decr = 0

        # # task 1
        # for i in range(1, len(measurements)):
        #     if measurements[i] > measurements[i-1]:
        #         incr+=1
        #     elif measurements[i] < measurements[i-1]:
        #         decr += 1

        # task 2
        measurements_sliding_window = [measurements[i:i+3] for i in range(len(measurements)-1)]
        for i in range(1, len(measurements_sliding_window)):
            if len(measurements_sliding_window[i]) < 3:
                break
            if sum(measurements_sliding_window[i]) > sum(measurements_sliding_window[i-1]):
                incr+=1
            elif sum(measurements_sliding_window[i]) < sum(measurements_sliding_window[i-1]):
                decr += 1

        print(f"Number of Increased {incr}")


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
def breathing_rate(breath_list):
    prev = breath_list[0]
    curr = breath_list[1]
    count = 0
    total_diff = 0
    for item in range(len(breath_list)):
        count += 1
        diff = curr - prev
        prev = curr
        curr = breath_list[item]
        if diff != 0:
            total_diff = diff + total_diff
            print(total_diff)

        if total_diff <= -4 and count < 50:
            print("drowsy")
        elif count > 50:
            count = 0

def main():
    listooo = [13,13,13,13,13,13,13,13,13,13,13,12,12,12,12,12,12,11,11,11,11,11,10,10,10,10,10,9,9,9,9,9,9,8,8,12,12,12,12,12,12,12,12]
    print(len(listooo))
    breathing_rate(listooo)
    plt.plot(listooo)
    plt.show()

if __name__ == "__main__":
    main()




lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

def reflowAndJustify(lines, X):
    total=""

    for line in lines:
        total += line

    words = list(total.split())
    word_count = [len(x) for x in words]
    # word_count[-1]-=1


    print(word_count)
    total = total.replace(' ', '-')

    for i in range(len(total)//X):
        print(total[X*i:X*(i+1)])
    # print(total)

reflowAndJustify(lines, 24)
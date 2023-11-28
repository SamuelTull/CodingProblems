from random import shuffle

from matplotlib.pyplot import box


def new_shuffle(N):
    shuffle_list = [i for i in range(N)]
    order_list = [i for i in range(N)]
    shuffle(shuffle_list)
    box_dict = {i: shuffle_list[i] for i in range(N)}
    loops = []
    while order_list:
        i = order_list[0]
        loops.append([i])
        order_list.remove(i)

        j = box_dict[i]
        while i != j:
            loops[-1].append(j)
            order_list.remove(j)
            j = box_dict[j]
    """for loop in loops:
        print(len(loop), loop)"""
    max_loop = max(len(loop) for loop in loops)
    # print("Max:", max_loop)
    return max_loop


fail = 0
succ = 0
for i in range(10000):
    max_loop = new_shuffle(100)
    if max_loop > 50:
        fail += 1
    else:
        succ += 1

print(succ, fail, succ / (fail + succ) * 100)

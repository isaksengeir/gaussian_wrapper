
cpus = 32
linda = 4


def linda_distribute(lindas, cpus):
    """
    :param lindas:
    :param cpus:
    :return: array with distributed cpus
    """
    cpu_array = [list() for i in range(lindas)]
    l_ = 0

    for i in range(cpus):
        cpu_array[l_].append(i)
        l_ += 1
        if l_ >= lindas:
            l_ = 0

    return cpu_array


def linda_distribute_ordered(lindas, cpus):
    """
    :param lindas:
    :param cpus:
    :return: array with cpus ordered
    """
    cpu_array = [list() for i in range(lindas)]
    l_ = 0
    group_size = int(cpus/lindas)
    remain = cpus % lindas

    for i in range(cpus):
        if len(cpu_array[l_]) >= group_size:
            if remain > 0 and len(cpu_array[l_]) == group_size:
                remain -= 1
            else:
                l_ += 1

        cpu_array[l_].append(i)

    return cpu_array


def print_lindas(cpu_array):
    for linda in range(len(cpu_array)):
        print(f"Linda {linda+1}: {' '.join([str(x) for x in cpu_array[linda]][:])}")


if __name__ == "__main__":
    cpu_list = linda_distribute_ordered(lindas=linda, cpus=cpus)
    print_lindas(cpu_array=cpu_list)

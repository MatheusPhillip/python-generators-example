import timeit

def generator():
    for i in range(10_000):
        yield i

def generator_return():
    temp = []
    for i in generator():
        if i == 1_000:
            break
        temp.append(i)
    
    return temp

def for_loop():
    temp_list: list[int] = []

    for i in range(10_000):
        temp_list.append(i)

    return temp_list

if __name__ == '__main__':
    time_for = timeit.timeit(stmt=for_loop, number=10_000)
    time_yield_to_list = timeit.timeit(stmt=generator_return, number=10_000)
    time_yield = timeit.timeit(stmt=generator, number=10_000)


    print('For Loop: ', round(time_for, 5))
    print('Yield: ', round(time_yield, 5))

    percent_faster = (time_for / time_yield) * 100
    
    print(f'{(round(percent_faster, 2)):,}% faster')

    print('Yield To List: ', round(time_yield_to_list, 5))
    percent_faster = (time_for / time_yield_to_list) * 100
    print(f'{(round(percent_faster, 2)):,}% faster')
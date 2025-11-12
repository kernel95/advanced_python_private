# generator_investigation.oy

#this function return a generator
# it will create items when needed or generate let's say
def count_up_to(n):

    print("count_up_to called")
    count = 1

    while count <= n:
        yield count
        print(f"looped {count}")
        count += 1



g = count_up_to(10)

#next function gets the next value of the generator
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)
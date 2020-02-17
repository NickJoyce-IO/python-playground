# We also want to be able to continue to add numbers to our chain.

# add(1)(2)(3); // 6
# add(1)(2)(3)(4); // 10
# add(1)(2)(3)(4)(5); // 15

class add(int):
    def __call__(self, v):
        return add(self + v)

print(add(1)(2)(3))
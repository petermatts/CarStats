def mySum(*x: tuple[int]) -> int:
    total = 0
    for i in x:
        total += i
    return total


if __name__ == "__main__":
    assert(mySum(1,2,3) == 6)
    assert(mySum(1,2,3,4,5) == 15)
    assert(mySum(1,2,4,9,16) == 32)
    assert(mySum(1,-1,1,-1) == 0)
    assert(mySum() == 0)

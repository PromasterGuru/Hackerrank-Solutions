def migratoryBirds(arr):
    type_of_bird = 0
    frequency = 0
    for i in range(1,6):
        if(arr.count(i) > frequency):
            frequency = arr.count(i)
            type_of_bird = i
        elif arr.count(i) == frequency:
            if(i < type_of_bird):
                type_of_bird = i
    return type_of_bird

if __name__ == "__main__":
    arr = [1,4,4,4,5,5]
    arr = [1,1,2,2,2,3,3,3]
    arr = [1,1,2,2,3]
    print(migratoryBirds(arr))
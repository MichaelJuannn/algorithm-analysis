def countMomentum(mass,velocity):
    momentum = mass * velocity
    return momentum

def countBounce(mass,velocity,height):
    if countMomentum(mass,velocity) == 0:
        return "you have no momentum"
    bounces = 0
    while height > 0:
        height = height - (height * 0.5)
        print(height)
    return bounces

countBounce(10,3,5)
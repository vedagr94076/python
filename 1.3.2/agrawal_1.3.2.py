def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return float(total + tip)

def hyp(leg1, leg2):
    '''Finds hypotenuse of 3rd leg'''
    hyp_squared = leg1**2 + leg2**2
    hyp = hyp_squared**.5
    return float(hyp)

def mean(a, b, c):
    mean = (a+b+c)/3.0
    return float(mean)

def perimeter(base, height):
    perimeter = (base*2)+(height*2)
    return float(perimeter)
    
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)
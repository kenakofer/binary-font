#!/usr/bin/env python3

def better(num, base, precision_override=0, space_every=0):
    if not base in [2, 16]:
        return
    num = str(num)
    if isinstance(num, str):
        if "." not in num:
            intpart = int(num)
            remainder = 0
            precision = 1
        else:
            intpart, remainder = num.split(".")
            precision = 1 / (10 ** len(remainder))
            intpart = int(intpart)
            remainder = float("."+remainder)
            
    if precision_override > 0:
        precision = precision_override
            
    if base == 2:
        string = bin(intpart)[2:]
    elif base == 16:
        string = hex(intpart)[2:]
        
    if space_every > 0:
        for i in range(len(string)-space_every, 0, -1*space_every):
            string = string[:i] + " " + string[i:]
    if remainder == 0:
        return string
    
    string += "."
    
    base_precision = 1 / base
    for d in range(-1, -10, -1):
        if remainder == 0:
            break
        base_precision /= float(base)
        if base_precision < precision:
            break
        
        for i in range(base-1, -1, -1):
            if i * base ** d <= remainder:
                string += hex(i)[2:]
                remainder -= i * base ** d
                break
    return string
    
    
class NumName:
    def __init__(self, val, name, syllables=1, omit_multiple=False):
        self.val = val
        self.name = name
        self.syllables = syllables
        self.omit_multiple = omit_multiple
        
NUM_PLACE = [
    NumName(256**4, "int"),
    NumName(256**2, "short"),
    NumName(256, "char"), # or byte
    NumName(16, "", 0),
]

NUM_PLACE_DECIMAL = [
    NumName(1000000000000, "trillion", 2),
    NumName(1000000000, "billion", 2),
    NumName(1000000, "million", 2),
    NumName(1000, "thousand", 2),
    NumName(100, "hundred", 2),
    NumName(90, "ninety", 2, True),
    NumName(80, "eighty", 2, True),
    NumName(70, "seventy", 2, True),
    NumName(60, "sixty", 2, True),
    NumName(50, "fifty", 2, True),
    NumName(40, "forty", 2, True),
    NumName(30, "thirty", 2, True),
    NumName(20, "twenty", 2, True),
]

SMALL_NUMS = [
    NumName(0, "zero", 2),
    NumName(1, "one"),
    NumName(2, "two"),
    NumName(3, "three"),
    NumName(4, "four"),
    NumName(5, "five"),
    NumName(6, "six"),
    NumName(7, "seven", 2),
    NumName(8, "eight"),
    NumName(9, "nine"),
    NumName(10, "ten"),
    NumName(11, "eleven", 3),
    NumName(12, "twelve"),
    NumName(13, "thirteen", 2),
    NumName(14, "fourteen", 2),
    NumName(15, "fifteen", 2),
    NumName(16, "sixteen", 2),
    NumName(17, "seventeen", 2),
    NumName(18, "eighteen", 2),
    NumName(19, "nineteen", 2),
]

SMALL_NUMS2 = [
    NumName(0, "zero", 2),
    NumName(1, "one"),
    NumName(2, "two"),
    NumName(3, "three"),
    NumName(4, "four"),
    NumName(5, "five"),
    NumName(6, "six"),
    NumName(7, "seven", 2),
    NumName(8, "eight"),
    NumName(9, "nine"),
    NumName(10, "alpha"),
    NumName(11, "bravo", 2),
    NumName(12, "charlie", 2),
    NumName(13, "delta", 2),
    NumName(14, "echo", 2),
    NumName(15, "foxtrot", 2),
]
SMALL_NUMS3 = [
    NumName(0, "zero", 2),
    NumName(1, "one"),
    NumName(2, "two"),
    NumName(3, "three"),
    NumName(4, "four"),
    NumName(5, "five"),
    NumName(6, "six"),
    NumName(7, "seven", 2),
    NumName(8, "eight"),
    NumName(9, "nine"),
    NumName(10, "A"),
    NumName(11, "B"),
    NumName(12, "C"),
    NumName(13, "D"),
    NumName(14, "E"),
    NumName(15, "F"),
]
   
def verbalize(binint, count_syllables=False, small_nums=None, place_names=None):
    small_nums = small_nums if small_nums else SMALL_NUMS
    place_names = place_names if place_names else NUM_PLACE
    for num_place in place_names:
        if binint >= num_place.val:
            multiples = int(binint / num_place.val)
            multiples_return = "" if num_place.omit_multiple else verbalize(multiples, count_syllables, small_nums=small_nums, place_names=place_names)
            place_return = num_place.syllables if count_syllables else (" " + num_place.name).rstrip()
            remainder = binint - multiples * num_place.val
            remainder_return = verbalize(remainder, count_syllables, small_nums=small_nums, place_names=place_names)
            if not count_syllables:
                remainder_return = " " + remainder_return
            if remainder == 0:
                remainder_return = 0 if count_syllables else ""
            return multiples_return + place_return + remainder_return
    for num in small_nums:
        if binint == num.val:
            return num.syllables if count_syllables else num.name
    return 0 if count_syllables else "???"

# for i in range(1, 100, 1):
    # print("sub ." + str(i) + " by " + better(i/100.0,2))
    # print("sub 5." + str(i) + " by " + better(5 + i/100.0,2))

for i in [1234567899125]:
    print("say", i, better(i, 2, 4), " as " + verbalize(i), "Syllables:", verbalize(i, True))
    print(verbalize(i, place_names=NUM_PLACE_DECIMAL))
    print(verbalize(i, small_nums=SMALL_NUMS2))
    print(verbalize(i, small_nums=SMALL_NUMS3))

import math


def func1(std_rc, input_rp, std_c, std_rb, input_rotationAngle):
    temp1 = math.pow(std_rc + input_rp)
    temp5 = (math.pow(std_rb) + math.pow(std_c) - math.pow(std_rc)) / (2 * std_rb * std_c)
    temp6 = input_rotationAngle * math.pi / 180
    temp4 = temp6 - math.acos(temp5)
    temp2 = math.pow(std_c * math.cos(temp4) - std_rb)
    temp3 = std_c * math.sin(temp4)
    return (math.sqrt(temp1 - temp2) + temp3 - input_rp - std_rb * temp6)

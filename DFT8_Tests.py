
from DFT_DCT import *

"""
    8-DFT Tests
"""

print("\n8-DFT TEST RESULTS\n")

# Test 1 - DC Test
input_re = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]
input_im = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]

vhdl_re_out = [32767, 0, 0, 0, 0, 0, 0, 0]
vhdl_im_out = [32767, 0, 0, 0, 0, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 2 - Dirac Test
input_re = [32767, 0, 0, 0, 0, 0, 0, 0]
input_im = [0, 0, 0, 0, 0, 0, 0, 0]

vhdl_re_out = [4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095]
vhdl_im_out = [0, 0, 0, 0, 0, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 3 - Spiral Test
input_re = [32767,0,-32767,0,32767,0,-32767,0]
input_im = [0,32767,0,-32767,0,32767,0,-32767]

vhdl_re_out = [0,0,32767,0,0,0,0,0]
vhdl_im_out = [0, 0, 0, 0, 0, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 4 - Random Test 1
input_re = [1315, -10480, -22880, -2692, 10179, 21419, -10685, -14802]
input_im = [-23958, 28901, 12319, 19622, 30781, -23915, -8253, -2061]

vhdl_re_out = [-3579,4158,4060,6795,-1940,-1231,7204,-14154]
vhdl_im_out = [4179,-818,-3210,-9369,-1457,-9819,3898,-7365]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 5 - Random Test 2
input_re = [-5798, -5908, 10780, -28330, -22883, -3043, 30776, -7628]
input_im = [5632, -30150, -7207, -17212, -23616, -15993, 2387, 30743]

vhdl_re_out = [-4005,-2978,-16240,-3732,7223,4849,-1321,10401]
vhdl_im_out = [-6927,11225,-5021,252,1226,1085,1730,2060]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 6 - Random Test 3
input_re = [10014, -24452, 25777, -16834, 5967, -21443, -22077, 29968]
input_im = [12995, 18474, 19649, -2241, 20505, 29425, -20801, -3248]

vhdl_re_out = [-1636,8553,8208,-9301,6555,2571,-5139,199]
vhdl_im_out = [9344,-3575,11710,10503,-1258,-10266,-3048,-417]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)
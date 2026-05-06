
from DFT import *

"""
    8-DFT Tests
"""

print("\n8-DFT TEST RESULTS\n")

# Test 1 - DC Test
input_re = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]
input_im = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]

vhdl_re_out = [32767, 0, 0, 0, 0, 0, 0, 0]
vhdl_im_out = [32767, 0, 0, 0, 0, 0, 0, 0]

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 2 - Dirac Test
input_re = [32767, 0, 0, 0, 0, 0, 0, 0]
input_im = [0, 0, 0, 0, 0, 0, 0, 0]

vhdl_re_out = [4095, 4095, 4095, 4095, 4095, 4095, 4095, 4095]
vhdl_im_out = [0, 0, 0, 0, 0, 0, 0, 0]

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 3 - Spiral Test
input_re = [32767,0,-32767,0,32767,0,-32767,0]
input_im = [0,32767,0,-32767,0,32767,0,-32767]

vhdl_re_out = [0,0,32767,0,0,0,0,0]
vhdl_im_out = [0, 0, 0, 0, 0, 0, 0, 0]

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 4 - Random Test 1
input_re = [1315, -10480, -22880, -2692, 10179, 21419, -10685, -14802]
input_im = [-23958, 28901, 12319, 19622, 30781, -23915, -8253, -2061]

vhdl_re_out = []
vhdl_im_out = []

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 5 - Random Test 2
input_re = [-5798, -5908, 10780, -28330, -22883, -3043, 30776, -7628]
input_im = [5632, -30150, -7207, -17212, -23616, -15993, 2387, 30743]

vhdl_re_out = []
vhdl_im_out = []

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 6 - Random Test 3
input_re = [10014, -24452, 25777, -16834, 5967, -21443, -22077, 29968]
input_im = [12995, 18474, 19649, -2241, 20505, 29425, -20801, -3248]

vhdl_re_out = []
vhdl_im_out = []

display_results(input_re, input_im, vhdl_re_out, vhdl_im_out)
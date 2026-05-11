
from DFT_DCT import *

"""
    4-DFT Tests
"""

print("\n4-DFT TEST RESULTS\n")

# Test 1 - DC Test
input_re = [32767, 32767, 32767, 32767]
input_im = [32767, 32767, 32767, 32767]

vhdl_re_out = [32767, 0, 0, 0]
vhdl_im_out = [32767, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 2 - Dirac Test
input_re = [32767, 0, 0, 0]
input_im = [0, 0, 0, 0]

vhdl_re_out = [8191,8191,8191,8191]
vhdl_im_out = [0, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 3 - Spiral Test
input_re = [32767, 0, -32767, 0]
input_im = [0, 32767, 0, -32767]

vhdl_re_out = [0, 32767, 0, 0]
vhdl_im_out = [0, 0, 0, 0]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 4 - Random Test 1
input_re = [19280, -993, -29155, -6286]
input_im = [20643, 16337, -4209, 1131]

vhdl_re_out = [-4289,15910,-649,8307]
vhdl_im_out = [8475,4889,-259,7536]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 5 - Random Test 2
input_re = [-5252, 29225, -14093, 5491]
input_im = [-29332, -6552, 14542, -30445]

vhdl_re_out = [3842,8183,-13516,-3763]
vhdl_im_out = [-12947,-16902,5551,-5035]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)

# Test 6 - Random Test 3
input_re = [7245, 18064, -23470, -14608]
input_im = [-19448, -1440, -6090, 12743]

vhdl_re_out = [-3193,4133,-4921,11224]
vhdl_im_out = [-3559,-11508,-9211,4828]

compare_dft(input_re, input_im, vhdl_re_out, vhdl_im_out)
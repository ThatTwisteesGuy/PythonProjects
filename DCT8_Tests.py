
from DFT_DCT import *

"""
    8-DCT Tests
"""

print("\n8-DCT W=16 TEST RESULTS\n")

# Test 1 - DC Test
input = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]

vhdl_out = [32767, 0, 0, 0, 0, 0, 0, 0]

compare_dct(input, vhdl_out)

# Test 2 - Dirac Test
input = [32767, 0, 0, 0, 0, 0, 0, 0]

vhdl_out = [4095,4016,3783,3405,2895,2276,1568,800]

compare_dct(input, vhdl_out)

# Test 3 - Nyquist Test
input = [32767, -32767, 32767, -32767, 32767, -32767, 32767, -32767]

vhdl_out = [0,4175,0,4926,0,7373,0,20995]

compare_dct(input, vhdl_out)

# Test 4 - Cosine Test
input = [32767,  16384, -16384, -32767, -16384,  16384,  32767,  16384]

vhdl_out = [6143,-2370,13703,7257,-4344,645,-974,140]

compare_dct(input, vhdl_out)

# Test 5 - Random Test 1
input = [10440, 28148, -20174, 23320, -18047, 19479, -4256, 23910]

vhdl_out = [7852,-29,4533,-202,1451,-1575,-1448,-11771]

compare_dct(input, vhdl_out)

# Test 6 - Random Test 2
input = [3038, 10496, -17798, 5114, -28785, -30277, -22846, -3359]

vhdl_out = [-10553,5942,4405,-4033,3220,184,-3009,-5018]

compare_dct(input, vhdl_out)

# Test 7 - Random Test 3
input = [19244, 19052, 10677, -27739, 31801, 23486, 17463, -31029]

vhdl_out = [7869,3986,-1718,10891,-6930,-3204,-1029,7084]

compare_dct(input, vhdl_out)


print("\n8-DCT W=18 TEST RESULTS\n")

# Test 1 - DC Test
input = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]

vhdl_out = [32767, 0, 0, 0, 0, 0, 0, 0]

compare_dct(input, vhdl_out)

# Test 2 - Dirac Test
input = [32767, 0, 0, 0, 0, 0, 0, 0]

vhdl_out = [4095,4017,3784,3405,2896,2276,1568,800]

compare_dct(input, vhdl_out)

# Test 3 - Nyquist Test
input = [32767, -32767, 32767, -32767, 32767, -32767, 32767, -32767]

vhdl_out = [0,4175,0,4926,0,7373,0,20995]

compare_dct(input, vhdl_out)

# Test 4 - Cosine Test
input = [32767,  16384, -16384, -32767, -16384,  16384,  32767,  16384]

vhdl_out = [6143,-2370,13703,7257,-4345,645,-973,141]

compare_dct(input, vhdl_out)

# Test 5 - Random Test 1
input = [10440, 28148, -20174, 23320, -18047, 19479, -4256, 23910]

vhdl_out = [7852,-29,4534,-202,1451,-1575,-1448,-11771]

compare_dct(input, vhdl_out)

# Test 6 - Random Test 2
input = [3038, 10496, -17798, 5114, -28785, -30277, -22846, -3359]

vhdl_out = [-10553,5942,4405,-4033,3220,185,-3008,-5018]

compare_dct(input, vhdl_out)

# Test 7 - Random Test 3
input = [19244, 19052, 10677, -27739, 31801, 23486, 17463, -31029]

vhdl_out = [7869,3986,-1718,10891,-6930,-3204,-1029,7084]

compare_dct(input, vhdl_out)


print("\n8-DCT W=20 TEST RESULTS\n")

# Test 1 - DC Test
input = [32767, 32767, 32767, 32767, 32767, 32767, 32767, 32767]

vhdl_out = [32767, 0, 0, 0, 0, 0, 0, 0]

compare_dct(input, vhdl_out)

# Test 2 - Dirac Test
input = [32767, 0, 0, 0, 0, 0, 0, 0]

vhdl_out = [4095,4017,3784,3405,2896,2276,1568,800]

compare_dct(input, vhdl_out)

# Test 3 - Nyquist Test
input = [32767, -32767, 32767, -32767, 32767, -32767, 32767, -32767]

vhdl_out = [0,4175,0,4926,0,7373,0,20995]

compare_dct(input, vhdl_out)

# Test 4 - Cosine Test
input = [32767,  16384, -16384, -32767, -16384,  16384,  32767,  16384]

vhdl_out = [6143,-2370,13703,7257,-4345,645,-973,141]

compare_dct(input, vhdl_out)

# Test 5 - Random Test 1
input = [10440, 28148, -20174, 23320, -18047, 19479, -4256, 23910]

vhdl_out = [7852,-29,4534,-202,1451,-1575,-1448,-11771]

compare_dct(input, vhdl_out)

# Test 6 - Random Test 2
input = [3038, 10496, -17798, 5114, -28785, -30277, -22846, -3359]

vhdl_out = [-10553,5942,4405,-4033,3220,185,-3008,-5018]

compare_dct(input, vhdl_out)

# Test 7 - Random Test 3
input = [19244, 19052, 10677, -27739, 31801, 23486, 17463, -31029]

vhdl_out = [7869,3986,-1718,10891,-6930,-3204,-1029,7084]

compare_dct(input, vhdl_out)
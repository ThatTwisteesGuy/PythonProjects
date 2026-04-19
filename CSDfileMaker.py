import math


def to_csd(num, bits=16):
    """
    Converts an integer to its Canonical Signed Digit (CSD) representation.
    Returns a list of length 'bits' containing 1, -1, or 0.
    Index 0 is the Least Significant Bit (LSB).
    """
    csd = [0] * bits
    carry = 0
    for i in range(bits):
        # Get the current bit and the next bit to determine if we need to carry
        b = (num >> i) & 1
        b_next = (num >> (i + 1)) & 1

        val = b + carry
        if val == 0:
            csd[i] = 0
            carry = 0
        elif val == 1:
            if b_next == 1:
                csd[i] = -1
                carry = 1
            else:
                csd[i] = 1
                carry = 0
        elif val == 2:
            csd[i] = 0
            carry = 1
        elif val == 3:
            csd[i] = -1
            carry = 1

    return csd


def generate_twiddle_vhdl():
    pos_masks = []
    neg_masks = []

    # Calculate values for k from 0 to 63
    for k in range(64):
        # Math: cos(k * 2pi / 256) which simplifies to cos(k * pi / 128)
        ideal_val = math.cos(k * math.pi / 128.0)

        # Scale to 16-bit range (multiply by 2^15) and round to nearest integer
        scaled_val = int(round(ideal_val * 32768))

        # Convert to strict CSD
        csd = to_csd(scaled_val, bits=16)

        pos_str = ""
        neg_str = ""

        # Parse the CSD array (LSB at index 0) into MSB-first strings
        for i in reversed(range(16)):
            if csd[i] == 1:
                pos_str += "1"
                neg_str += "0"
            elif csd[i] == -1:
                pos_str += "0"
                neg_str += "1"
            else:
                pos_str += "0"
                neg_str += "0"

        pos_masks.append(pos_str)
        neg_masks.append(neg_str)

    # ------------------------------------------------------------------------
    # Format and build the VHDL output string
    # ------------------------------------------------------------------------
    vhdl = "library IEEE;\n"
    vhdl += "use ieee.std_logic_1164.all;\n\n"
    vhdl += "package twiddle_constants_pkg is\n"
    vhdl += "    -- Each entry is a 16-bit mask for Base 256\n"
    vhdl += "    type csd_table is array (0 to 63) of std_logic_vector(15 downto 0);\n\n"
    vhdl += "    -- POSITIVE MASKS: Bits indicating an ADD operation\n"
    vhdl += "    constant CSD_POS : csd_table := (\n"

    for k in range(64):
        vhdl += f"        {k:<2} => \"{pos_masks[k]}\",\n"

    vhdl += "        others => \"0000000000000000\"\n"
    vhdl += "    );\n\n"

    vhdl += "    -- NEGATIVE MASKS: Bits indicating a SUBTRACT operation (CSD)\n"
    vhdl += "    constant CSD_NEG : csd_table := (\n"

    for k in range(64):
        vhdl += f"        {k:<2} => \"{neg_masks[k]}\",\n"

    vhdl += "        others => \"0000000000000000\"\n"
    vhdl += "    );\n"
    vhdl += "end package twiddle_constants_pkg;\n"

    return vhdl


# Generate the VHDL and save it to a file
if __name__ == "__main__":
    vhdl_output = generate_twiddle_vhdl()

    # Print to console (optional)
    print(vhdl_output)

    # Export to a VHDL file
    filename = "twiddle_constants_pkg.vhd"
    with open(filename, "w") as f:
        f.write(vhdl_output)
    print(f"\n--- Successfully exported VHDL to {filename} ---")
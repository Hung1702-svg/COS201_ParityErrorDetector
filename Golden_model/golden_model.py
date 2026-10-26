
# Parity Error Detector

# Cac truong hop kiem tra
test_data = [178, 178, 255, 255, 0]
test_error = [0, 1, 0, 1, 0]

for i in range(len(test_data)):

    data = test_data[i]
    error_enable = test_error[i]

    # Chuyen data thanh 8 bit
    data_bits = []

    for j in range(7, -1, -1):
        bit = (data // (2 ** j)) % 2
        data_bits.append(bit)

    # Tao parity bit
    count = 0

    for bit in data_bits:
        if bit == 1:
            count = count + 1

    if count % 2 == 0:
        parity_bit = 0
    else:
        parity_bit = 1

   

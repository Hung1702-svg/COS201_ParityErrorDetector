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
# Mo phong loi truyen
    data_rx = data_bits.copy()
    if error_enable == 1:
        if data_rx[5] == 0:
            data_rx[5] = 1
        else:
            data_rx[5] = 0
    # Kiem tra parity
    count = 0
    for bit in data_rx:
        if bit == 1:
            count = count + 1

    count = count + parity_bit
    if count % 2 == 0:
        error_flag = 0
    else:
        error_flag = 1
    # In ket qua
    print("Data:", "".join(str(bit) for bit in data_bits))
    print("Parity:", parity_bit)
    print("Error enable:", error_enable)
    print("Received data:", "".join(str(bit) for bit in data_rx))
    print("Error flag:", error_flag)
    # So sanh ket qua
    if error_flag == error_enable:
        print("PASS")
    else:
        print("FAIL")
    print("--------------------")

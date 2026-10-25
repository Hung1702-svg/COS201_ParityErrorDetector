module top (
    input wire [7:0] data_in,
    input wire error_enable,
    output wire parity_bit,
    output wire [7:0] data_rx,
    output wire error_flag
);
// Module 1: Tao parity bit
parity_generator U1 (
    .data_in(data_in),
    .parity_bit(parity_bit)
);
// Module 2: Mo phong loi truyen du lieu
error_injector U2 (
    .data_in(data_in),
    .error_enable(error_enable),
    .data_out(data_rx)
);
// Module 3: Kiem tra parity
parity_checker U3 (
    .data_rx(data_rx),
    .parity_rx(parity_bit),
    .error_flag(error_flag)
);
endmodule

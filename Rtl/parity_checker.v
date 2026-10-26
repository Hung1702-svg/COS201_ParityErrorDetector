module parity_checker (
    input wire [7:0] data_rx,
    input wire parity_rx,
    output reg error_flag
);
always @(*) begin
    error_flag = data_rx[0] ^
                 data_rx[1] ^
                 data_rx[2] ^
                 data_rx[3] ^
                 data_rx[4] ^
                 data_rx[5] ^
                 data_rx[6] ^
                 data_rx[7] ^
                 parity_rx;
end
endmodule

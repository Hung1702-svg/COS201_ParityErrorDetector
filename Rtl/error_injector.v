module error_injector (
    input wire [7:0] data_in,
    input wire error_enable,
    output reg [7:0] data_out
);
always @(*) begin
    if (error_enable == 1'b0) begin
        data_out = data_in;
    end
    else begin
        data_out = data_in;
        data_out[5] = ~data_in[5];
    end
end
endmodule

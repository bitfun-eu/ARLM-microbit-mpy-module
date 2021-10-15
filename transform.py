def T(in_range, out_range, v): 
    in_low = min(in_range)
    in_high = max(in_range)
    assert in_low <= v <= in_high, "value not in range!" + str(in_low) + ',' + s
    out_first, out_second = out_range
    # input range
    input_range = in_high - in_low
    output_range = abs(out_first - out_second)
    # where is v in in_range?
    p = (v - in_low)/input_range
    # how much does this translated in out_range?
    d = p * output_range
    # decide the final value
    if out_first <= out_second:
        v_new = out_first + d 
    else:
        v_new = out_first - d 
    # decide if returns int or float
    if isinstance(out_first, float) or isinstance(out_second, float):
        return v_new
    else:
        return round(v_new)

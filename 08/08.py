with open("input.txt") as f:
    input = f.read().splitlines()

signal_patterns = [line.split("|") for line in input]
signal_patterns = [[input.strip().split(" "), output.strip().split(" ")] for input, output in signal_patterns]

def sort_string(string):
    return ''.join(sorted(string))

def part_one():
    outputs = [output for _, output in signal_patterns]
    output_segments_length = [len(segment) for output in outputs for segment in output]
    segment_counts = {num: 0 for num in range(8)}
    for segment_length in output_segments_length:
        segment_counts[segment_length] += 1

    total = 0
    [
        total := total + segment_count
        for num_segments, segment_count in segment_counts.items()
        if num_segments in [7, 4, 2, 3]
    ]

    print(total)


def part_two():
    signal_map = {num: 0 for num in range(10)}
    output_value_total = 0
    for input, output in signal_patterns:
        sorted_inputs = sorted(input, key=len)
        for signal in sorted_inputs:
            match len(signal):
                case 2:
                    signal_map[1] = sort_string(signal)
                case 3:
                    signal_map[7] = sort_string(signal)
                case 4:
                    signal_map[4] = sort_string(signal)
                case 5:
                    #  2, 3 or 5
                    four_minus_one = [segment for segment in signal_map[4] if segment not in signal_map[1]]
                    if all(segment in signal for segment in signal_map[1]):
                        signal_map[3] = sort_string(signal)
                    elif all(segment in signal for segment in four_minus_one):
                        signal_map[5] = sort_string(signal)
                    else: 
                        signal_map[2] = sort_string(signal)
                case 6:
                    # 0, 6 or 9
                    if signal_map[1]:
                        if any(segment not in signal for segment in signal_map[1]):
                            signal_map[6] = sort_string(signal)
                        elif all(segment in signal for segment in signal_map[4]):
                            signal_map[9] = sort_string(signal)
                        else: 
                            signal_map[0] = sort_string(signal)
                case 7:
                    signal_map[8] = sort_string(signal)



        out = ''
        for signal in output:
            signal = sort_string(signal)
            index = list(signal_map.values()).index(signal)
            signal_value = list(signal_map.keys())[index]
            out += str(signal_value)
        output_value_total += int(out)
        
    print(output_value_total)


part_one()
part_two()

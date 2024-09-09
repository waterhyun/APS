import sys
sys.stdin = open('swea/bit/input.txt', 'r')

def hex_to_bin(hex_str):
    return ''.join(bin(int(c, 16))[2:].zfill(4) for c in hex_str)

def decode_barcode(barcode):
    patterns = {
        "0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, 
        "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7, 
        "0110111": 8, "0001011": 9
    }
    
    digits = []
    for i in range(0, len(barcode), 7):
        segment = barcode[i:i+7]
        if segment in patterns:
            digits.append(patterns[segment])
        else:
            return None
    return digits

def check_validity(code):
    if len(code) != 8:
        return False
    odd_sum = sum(code[i] for i in range(0, 7, 2))
    even_sum = sum(code[i] for i in range(1, 7, 2))
    total = (odd_sum * 3) + even_sum + code[7]
    return total % 10 == 0

def process_case(n, m, data):
    binary_data = [hex_to_bin(line) for line in data]
    seen_codes = set()
    total_sum = 0

    for row in binary_data:
        last_idx = len(row) - 1
        while last_idx >= 55:
            found_code = False
            for scale in range(1, 6):  # 암호코드의 가로 길이 56 ~ 280
                if last_idx + 1 < 56 * scale:
                    continue
                code = row[last_idx - (56*scale) + 1 : last_idx + 1]
                reduced_code = ''.join(['1' if '1' in code[i:i+scale] else '0' for i in range(0, 56*scale, scale)])
                decoded = decode_barcode(reduced_code)
                if decoded and check_validity(decoded):
                    code_tuple = tuple(decoded)
                    if code_tuple not in seen_codes:
                        total_sum += sum(decoded)
                        seen_codes.add(code_tuple)
                    found_code = True
                    last_idx = last_idx - 56*scale  # 찾은 코드의 시작 부분 바로 앞으로 이동
                    break
            if not found_code:
                last_idx = row.rfind('1', 0, last_idx)

    return total_sum


T = int(input())
for case_num in range(1, T + 1):
    n, m = map(int, input().split())
    data = [input().strip() for _ in range(n)]
    result = process_case(n, m, data)
    print(f"#{case_num} {result}")

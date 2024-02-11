"""
This script provides a function to convert Chinese text between Simplified and Traditional Chinese characters.
It uses the OpenCC library for the conversion.

Usage:
    python convert_chinese.py -i <input_file> -o <output_file> --conversion <conversion_direction> [--verbose]

Arguments:
    -i, --input: Input file path.
    -o, --output: Output file path.
    --conversion: Conversion direction. Choose 's2t' for Simplified to Traditional or 't2s' for Traditional to Simplified.
    --verbose: Display all replaced text. (Optional)

Example:
    python convert_chinese.py -i input.txt -o output.txt --conversion s2t --verbose
"""
#%%
import re
import argparse
from opencc import OpenCC

def convert_chinese(input_path, output_path, conversion, verbose=False):
    with open(input_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    def replace_text(match):
        cc = OpenCC(conversion)  # 根據用戶選擇設定繁簡轉換
        original = match.group()
        converted = cc.convert(original)
        if verbose:
            print(f"**{original} -> {converted}**")
        return converted
    
    converted_content = re.sub(r'[\u4e00-\u9fa5]+', replace_text, content)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)

#%%
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert between Simplified and Traditional Chinese.")
    parser.add_argument("-i", "--input", required=True, help="Input file path.")
    parser.add_argument("-o", "--output", required=True, help="Output file path.")
    parser.add_argument("--conversion", choices=['s2t', 't2s', 's2twp'], required=True, help="Conversion direction: 's2t' for Simplified to Traditional, 't2s' for Traditional to Simplified, 's2twp` for Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases).")
    parser.add_argument("--verbose", action="store_true", help="Display all replaced text.")

    args = parser.parse_args()

    convert_chinese(args.input, args.output, args.conversion, args.verbose)

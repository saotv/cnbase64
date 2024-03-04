import streamlit as st
import base64
import zlib

# Mapping for Base85 characters to I Ching hexagrams (partial for demonstration)
base85_to_hexagrams = {
    '0': '䷀', '1': '䷁', '2': '䷂', '3': '䷃', '4': '䷄', '5': '䷅', '6': '䷆', '7': '䷇',
    '8': '䷈', '9': '䷉', 'A': '䷊', 'B': '䷋', 'C': '䷌', 'D': '䷍', 'E': '䷎', 'F': '䷏',
    'G': '䷐', 'H': '䷑', 'I': '䷒', 'J': '䷓', 'K': '䷔', 'L': '䷕', 'M': '䷖', 'N': '䷗',
    'O': '䷘', 'P': '䷙', 'Q': '䷚', 'R': '䷛', 'S': '䷜', 'T': '䷝', 'U': '䷞', 'V': '䷟',
    'W': '䷠', 'X': '䷡', 'Y': '䷢', 'Z': '䷣', 'a': '䷤', 'b': '䷥', 'c': '䷦', 'd': '䷧',
    'e': '䷨', 'f': '䷩', 'g': '䷪', 'h': '䷫', 'i': '䷬', 'j': '䷭', 'k': '䷮', 'l': '䷯',
    'm': '䷰', 'n': '䷱', 'o': '䷲', 'p': '䷳', 'q': '䷴', 'r': '䷵', 's': '䷶', 't': '䷷',
    'u': '䷸', 'v': '䷹', 'w': '䷺', 'x': '䷻', 'y': '䷼', 'z': '䷽'
}

# Reverse mapping for decoding
hexagrams_to_base85 = {v: k for k, v in base85_to_hexagrams.items()}

def encode_to_hexagrams(text):
    try:
        # 压缩文本并转换为Base85
        compressed_text = zlib.compress(text.encode('utf-8'))
        encoded_text = base64.b85encode(compressed_text).decode('utf-8')
        # 替换Base85字符为易经卦象
        return ''.join(base85_to_hexagrams.get(char, char) for char in encoded_text)
    except Exception as e:
        return f"Error encoding text: {e}"

def decode_from_hexagrams(hexagram_str):
    try:
        # 将易经卦象替换为Base85字符
        base85_str = ''.join(hexagrams_to_base85.get(char, char) for char in hexagram_str)
        # 将Base85解码并解压
        decompressed_data = zlib.decompress(base64.b85decode(base85_str))
        return decompressed_data.decode('utf-8')
    except Exception as e:
        return f"Error decoding hexagrams: {e}"

# Streamlit界面
st.title('I Ching Encoder/Decoder with Compression')

import base64

def encode_to_hexagrams(text):
    # Encode text to Ascii85
    encoded_text = base64.a85encode(text.encode('utf-8'), pad=False).decode('utf-8')
    # Replace Ascii85 characters with I Ching hexagrams
    return ''.join(base85_to_hexagrams.get(char, char) for char in encoded_text)

def decode_from_hexagrams(hexagram_str):
    # Replace I Ching hexagrams with Ascii85 characters
    ascii85_str = ''.join(hexagrams_to_base85.get(char, char) for char in hexagram_str)
    # Decode Ascii85 to text
    return base64.a85decode(ascii85_str).decode('utf-8')

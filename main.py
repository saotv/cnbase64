import streamlit as st
import base64
import zlib

# Mapping for Base64 characters to I Ching hexagrams
base64_to_hexagrams = {
    'A': '䷀', 'B': '䷁', 'C': '䷂', 'D': '䷃', 'E': '䷄', 'F': '䷅', 'G': '䷆', 'H': '䷇',
    'I': '䷈', 'J': '䷉', 'K': '䷊', 'L': '䷋', 'M': '䷌', 'N': '䷍', 'O': '䷎', 'P': '䷏',
    'Q': '䷐', 'R': '䷑', 'S': '䷒', 'T': '䷓', 'U': '䷔', 'V': '䷕', 'W': '䷖', 'X': '䷗',
    'Y': '䷘', 'Z': '䷙', 'a': '䷚', 'b': '䷛', 'c': '䷜', 'd': '䷝', 'e': '䷞', 'f': '䷟',
    'g': '䷠', 'h': '䷡', 'i': '䷢', 'j': '䷣', 'k': '䷤', 'l': '䷥', 'm': '䷦', 'n': '䷧',
    'o': '䷨', 'p': '䷩', 'q': '䷪', 'r': '䷫', 's': '䷬', 't': '䷭', 'u': '䷮', 'v': '䷯',
    'w': '䷰', 'x': '䷱', 'y': '䷲', 'z': '䷳', '0': '䷴', '1': '䷵', '2': '䷶', '3': '䷷',
    '4': '䷸', '5': '䷹', '6': '䷺', '7': '䷻', '8': '䷼', '9': '䷽', '+': '䷾', '/': '䷿',
    '=': ' '  # Handle padding for Base64
}

# Reverse mapping for decoding
hexagrams_to_base64 = {v: k for k, v in base64_to_hexagrams.items()}

def encode_to_hexagrams(text):
    try:
        # Compress text and convert to Base64
        compressed_text = zlib.compress(text.encode('utf-8'))
        encoded_text = base64.b64encode(compressed_text).decode('utf-8')
        # Replace Base64 characters with I Ching hexagrams
        return ''.join(base64_to_hexagrams[char] for char in encoded_text if char in base64_to_hexagrams)
    except Exception as e:
        return f"Error encoding text: {e}"

def decode_from_hexagrams(hexagram_str):
    try:
        # Replace I Ching hexagrams with Base64 characters
        base64_str = ''.join(hexagrams_to_base64[char] for char in hexagram_str if char in hexagrams_to_base64)
        # Decode Base64 and decompress
        decompressed_data = zlib.decompress(base64.b64decode(base64_str))
        return decompressed_data.decode('utf-8')
    except Exception as e:
        return f"Error decoding hexagrams: {e}"

# Streamlit interface
st.title('I Ching Encoder/Decoder with Compression')

# Encoding
text_to_encode = st.text_area("Text to encode:")
if st.button('Encode'):
    encoded_message = encode_to_hexagrams(text_to_encode)
    st.text_area("Encoded hexagrams:", encoded_message, height=150)

# Decoding
hexagrams_to_decode = st.text_area("Hexagrams to decode:")
if st.button('Decode'):
    decoded_message = decode_from_hexagrams(hexagrams_to_decode)
    st.text_area("Decoded text:", decoded_message, height=150)

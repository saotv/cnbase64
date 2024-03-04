import streamlit as st
import base64
import zlib

# Mapping for Base85 characters to I Ching hexagrams
base85_to_hexagrams = {
    '0': '䷀', '1': '䷁', '2': '䷂', '3': '䷃', '4': '䷄', '5': '䷅', '6': '䷆', '7': '䷇',
    '8': '䷈', '9': '䷉', 'A': '䷊', 'B': '䷋', 'C': '䷌', 'D': '䷍', 'E': '䷎', 'F': '䷏',
    'G': '䷐', 'H': '䷑', 'I': '䷒', 'J': '䷓', 'K': '䷔', 'L': '䷕', 'M': '䷖', 'N': '䷗',
    'O': '䷘', 'P': '䷙', 'Q': '䷚', 'R': '䷛', 'S': '䷜', 'T': '䷝', 'U': '䷞', 'V': '䷟',
    'W': '䷠', 'X': '䷡', 'Y': '䷢', 'Z': '䷣', 'a': '䷤', 'b': '䷥', 'c': '䷦', 'd': '䷧',
    'e': '䷨', 'f': '䷩', 'g': '䷪', 'h': '䷫', 'i': '䷬', 'j': '䷭', 'k': '䷮', 'l': '䷯',
    'm': '䷰', 'n': '䷱', 'o': '䷲', 'p': '䷳', 'q': '䷴', 'r': '䷵', 's': '䷶', 't': '䷷',
    'u': '䷸', 'v': '䷹', 'w': '䷺', 'x': '䷻', 'y': '䷼', 'z': '䷽', '!': '䷾', '#': '䷿',
    '$': '䷀', '%': '䷁', '&': '䷂', '(': '䷃', ')': '䷄', '*': '䷅', '+': '䷆', '-': '䷇',
    ';': '䷈', '<': '䷉', '=': '䷊', '>': '䷋', '?': '䷌', '@': '䷍', '^': '䷎', '_': '䷏',
    '`': '䷐', '{': '䷑', '|': '䷒', '}': '䷓', '~': '䷔'
}

# Reverse mapping for decoding
hexagrams_to_base85 = {v: k for k, v in base85_to_hexagrams.items()}

def encode_to_hexagrams(text):
    try:
        # Compress text and convert to Base85
        compressed_text = zlib.compress(text.encode('utf-8'))
        encoded_text = base64.b85encode(compressed_text).decode('utf-8')
        # Replace Base85 characters with I Ching hexagrams
        return ''.join(base85_to_hexagrams[char] for char in encoded_text)  # Use direct mapping
    except Exception as e:
        return f"Error encoding text: {e}"

def decode_from_hexagrams(hexagram_str):
    try:
        # Replace I Ching hexagrams with Base85 characters
        base85_str = ''.join(hexagrams_to_base85[char] for char in hexagram_str)  # Use direct mapping
        # Decode Base85 and decompress
        decompressed_data = zlib.decompress(base64.b85decode(base85_str))
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

import streamlit as st
import base64

# Mapping Base64 characters to I Ching hexagrams
base64_to_hexagrams = {
    '䷀': 'A', '䷁': 'B', '䷂': 'C', '䷃': 'D', '䷄': 'E', '䷅': 'F', '䷆': 'G', '䷇': 'H',
    '䷈': 'I', '䷉': 'J', '䷊': 'K', '䷋': 'L', '䷌': 'M', '䷍': 'N', '䷎': 'O', '䷏': 'P',
    '䷐': 'Q', '䷑': 'R', '䷒': 'S', '䷓': 'T', '䷔': 'U', '䷕': 'V', '䷖': 'W', '䷗': 'X',
    '䷘': 'Y', '䷙': 'Z', '䷚': 'a', '䷛': 'b', '䷜': 'c', '䷝': 'd', '䷞': 'e', '䷟': 'f',
    '䷠': 'g', '䷡': 'h', '䷢': 'i', '䷣': 'j', '䷤': 'k', '䷥': 'l', '䷦': 'm', '䷧': 'n',
    '䷨': 'o', '䷩': 'p', '䷪': 'q', '䷫': 'r', '䷬': 's', '䷭': 't', '䷮': 'u', '䷯': 'v',
    '䷰': 'w', '䷱': 'x', '䷲': 'y', '䷳': 'z', '䷴': '0', '䷵': '1', '䷶': '2', '䷷': '3',
    '䷸': '4', '䷹': '5', '䷺': '6', '䷻': '7', '䷼': '8', '䷽': '9', '䷾': '+', '䷿': '/'
}
hexagrams_to_base64 = {v: k for k, v in base64_to_hexagrams.items()}

def encode_to_hexagrams(text):
    # Encode text to Base64
    encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    # Replace Base64 characters with I Ching hexagrams
    return ''.join(base64_to_hexagrams.get(char, char) for char in encoded_text)

def decode_from_hexagrams(hexagram_str):
    # Replace I Ching hexagrams with Base64 characters
    base64_str = ''.join(hexagrams_to_base64.get(char, char) for char in hexagram_str)
    # Decode Base64 to text
    return base64.b64decode(base64_str).decode('utf-8')

# Streamlit interface
st.title('I Ching Base64 Encoder/Decoder')

# Encoding
text_to_encode = st.text_area("Text to encode:")
if st.button('Encode'):
    st.write(encode_to_hexagrams(text_to_encode))

# Decoding
hexagrams_to_decode = st.text_area("Hexagrams to decode:")
if st.button('Decode'):
    st.write(decode_from_hexagrams(hexagrams_to_decode))

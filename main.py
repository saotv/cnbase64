import base64
import streamlit as st

# Example mapping of 6 hexagrams to base64 characters
# You need to create a complete mapping for all 64 hexagrams
hexagram_map = {
    '䷀': 'A', '䷁': 'B', '䷂': 'C', '䷃': 'D', '䷄': 'E', '䷅': 'F', '䷆': 'G', '䷇': 'H',
    '䷈': 'I', '䷉': 'J', '䷊': 'K', '䷋': 'L', '䷌': 'M', '䷍': 'N', '䷎': 'O', '䷏': 'P',
    '䷐': 'Q', '䷑': 'R', '䷒': 'S', '䷓': 'T', '䷔': 'U', '䷕': 'V', '䷖': 'W', '䷗': 'X',
    '䷘': 'Y', '䷙': 'Z', '䷚': 'a', '䷛': 'b', '䷜': 'c', '䷝': 'd', '䷞': 'e', '䷟': 'f',
    '䷠': 'g', '䷡': 'h', '䷢': 'i', '䷣': 'j', '䷤': 'k', '䷥': 'l', '䷦': 'm', '䷧': 'n',
    '䷨': 'o', '䷩': 'p', '䷪': 'q', '䷫': 'r', '䷬': 's', '䷭': 't', '䷮': 'u', '䷯': 'v',
    '䷰': 'w', '䷱': 'x', '䷲': 'y', '䷳': 'z', '䷴': '0', '䷵': '1', '䷶': '2', '䷷': '3',
    '䷸': '4', '䷹': '5', '䷺': '6', '䷻': '7', '䷼': '8', '䷽': '9', '䷾': '+', '䷿': '/'
}

# Reverse mapping for decoding
reverse_hexagram_map = {v: k for k, v in hexagram_map.items()}

def encode_to_hexagrams(input_string):
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8').rstrip('=')  # Strip padding characters
    encoded_hexagrams = ''.join(hexagram_map.get(character, '?') for character in encoded_str)
    return encoded_hexagrams
    
def decode_from_hexagrams(input_hexagrams):
    base64_str = ''.join(reverse_hexagram_map.get(hexagram, '?') for hexagram in input_hexagrams)
    try:
        decoded_bytes = base64.b64decode(base64_str)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"Error in decoding: {e}"

# Streamlit interface
st.title('I Ching Base64 Encoder/Decoder')

operation = st.radio("Choose operation", ('Encode', 'Decode'))

if operation == 'Encode':
    text = st.text_area("Enter text to encode")
    if st.button('Encode'):
        result = encode_to_hexagrams(text)
        if '?' not in result:
            st.text_area("Encoded Hexagrams", result, height=150)
        else:
            st.error("Encoding failed: Input contains characters not in the hexagram mapping.")
else:
    hexagrams = st.text_area("Enter hexagrams to decode")
    if st.button('Decode'):
        result = decode_from_hexagrams(hexagrams)
        if "Error in decoding" not in result:
            st.text_area("Decoded Text", result, height=150)
        else:
            st.error(result)

# Save this code to a file named `iching_base64_streamlit.py` and run with `streamlit run iching_base64_streamlit.py`.

import base64

def encode_message(message: str) -> str:
    encoded_bytes = base64.b64encode(message.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decode_message(encoded_message: str) -> str:
    decoded_bytes = base64.b64decode(encoded_message.encode("utf-8"))
    return decoded_bytes.decode("utf-8")
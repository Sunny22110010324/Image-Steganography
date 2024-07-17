from PIL import Image
from cryptography.fernet import Fernet
import base64

# Function to generate a key from a password
def generate_key(password):
    return base64.urlsafe_b64encode(password.ljust(32).encode('utf-8')[:32])

# Encrypt data
def encrypt_data(data, password):
    key = generate_key(password)
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    return encrypted

# Decrypt data
def decrypt_data(encrypted_data, password):
    key = generate_key(password)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data).decode()
    return decrypted

# Convert encoding data into 8-bit binary form using ASCII value of characters
def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

# Modify pixels according to the 8-bit binary data
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]

        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1

        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

# Encode data into image
def encode():
    img = input("Enter image name (with extension): ")
    image = Image.open(img, 'r')

    data = input("Enter data to be encoded: ")
    password = input("Enter password for encryption: ")
    if len(data) == 0:
        raise ValueError('Data is empty')

    encrypted_data = encrypt_data(data, password)
    newimg = image.copy()
    encode_enc(newimg, encrypted_data.decode())

    new_img_name = input("Enter the name of the new image (with extension): ")
    newimg.save(new_img_name)  # Automatically handles the format based on the file extension


# Decode the data in the image
def decode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')

    encrypted_data = b''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3]]

        binstr = ''
        for i in pixels[:8]:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'

        encrypted_data += chr(int(binstr, 2)).encode()
        if pixels[-1] % 2 != 0:
            break

    password = input("Enter password for decryption: ")
    decrypted_data = decrypt_data(encrypted_data, password)
    return decrypted_data

# Main Function
def main():
    a = int(input(":: Welcome to Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()
    elif (a == 2):
        print("Decoded data: " + decode())
    else:
        raise Exception("Enter correct input")

# Driver Code
if __name__ == '__main__':
    main()

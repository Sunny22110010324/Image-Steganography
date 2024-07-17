# Image-Steganography
Image steganography is a technique used to hide secret information within digital images, making the embedded data invisible to the human eye while preserving the image's original appearance. This method leverages the redundancy in pixel values to encode messages without significantly altering the image's visual quality. 

**Types of Image Steganography**

**1. Least Significant Bit (LSB) Method:**

This method involves modifying the least significant bits of the pixel values to encode the hidden message. Since changes in the LSB do not significantly alter the appearance of the image, the hidden data remains undetectable.

**2. RGB-Based Steganography:**

This technique manipulates the Red, Green, and Blue (RGB) color values of the image to conceal data. It can be a variant of the LSB method applied to the individual color channels or other more sophisticated strategies.

**Type Used in the Provided Code**

The provided code uses the Least Significant Bit (LSB) Method to hide encrypted data within an image.

**Libraries used in this code:**

1) **PIL (Python Imaging Library):**

a) Used for image manipulation such as opening, modifying, and saving images.

b) Functions: Image.open(), Image.putpixel(), Image.getdata()

**Install PIL (Pillow)**

        _pip install Pillow_

2) **cryptography.fernet:**

a) Provides symmetric encryption and decryption, using AES encryption for secure data handling.

b) Functions: Fernet(), Fernet.encrypt(), Fernet.decrypt()

**Install Cryptography**

        _pip install cryptography_

3) **base64:**

a) Encodes and decodes data to and from base64 format, ensuring the data is URL safe.

b) Functions: base64.urlsafe_b64encode()

**Install base64 (Built-in)**

The base64 module is part of the Python standard library, so you don't need to install it separately. It is included with Python by default.

<img src="C:\Users\itsme\OneDrive\Documents\EDUNET Proj\hacker.jpg" alt="Description" width="500" height="300">


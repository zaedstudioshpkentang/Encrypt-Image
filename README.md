# XOR Image Encryption

A simple Python script to encrypt and decrypt images using the XOR operation. This script works without the need for external libraries, making it lightweight and suitable for environments with limited resources, such as Termux.

## Features
- **Lightweight**: No need for heavy libraries; works with built-in Python modules.
- **XOR Encryption**: Uses a simple XOR operation for encryption and decryption.
- **Maintains Original Format**: The encrypted image keeps its original file extension, but the content becomes abstract and unreadable until decrypted.

## How It Works
1. The script reads the binary data of the image.
2. It applies the XOR operation between each byte of the image data and a user-provided password.
3. The same password is used to decrypt the image and recover the original content.


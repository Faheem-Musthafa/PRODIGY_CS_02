﻿# PRODIGY_CS_02
Here's a simple GitHub README template for your image encryption/decryption project:

markdown
Copy code
# Image Encryption and Decryption Tool

This is a simple Python-based tool for encrypting and decrypting images using pixel manipulation. The encryption process involves XORing pixel values with a user-provided key, and the decryption process reverses this operation to restore the original image.

## Features
- Encrypt and decrypt images using a basic XOR operation on pixel values.
- Allows the user to specify input and output file paths for images.
- User-friendly menu for easy interaction in the terminal.
- Option to enter a custom encryption/decryption key.

## Requirements
- Python 3.x
- `Pillow` library for image processing
- `NumPy` for handling arrays and mathematical operations

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/image-encryption-tool.git
   cd image-encryption-tool
Install the required dependencies:
bash
Copy code
pip install pillow numpy
Usage
Save the script as interactive_image_tool.py.

Run the script with Python:

bash
Copy code
python interactive_image_tool.py
The tool will display a menu with the following options:

Encrypt an Image: Encrypt an image using an encryption key.
Decrypt an Image: Decrypt an encrypted image using the same key used for encryption.
Exit: Exit the program.
For encryption and decryption:

You will be prompted to enter the file path for the input image.
You will also need to provide the output file path for saving the encrypted or decrypted image.
Enter an integer key for the encryption/decryption process.
Example Interaction
mathematica
Copy code
Welcome to the Image Encryption/Decryption Tool!

Choose an option:
1. Encrypt an Image
2. Decrypt an Image
3. Exit
Enter your choice (1/2/3): 1
Enter the path to the input image: input_image.jpg
Enter the path to save the encrypted image: encrypted_image.jpg
Enter the encryption key (integer): 123
Encrypted image saved at encrypted_image.jpg
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Pillow and NumPy libraries for image processing and array manipulation.
less
Copy code
--------------------------------------------------------------------------------------------------------------------------------------


from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """Encrypt an image by applying pixel manipulation."""
    try:
        image = Image.open(input_path)
        image_array = np.array(image)

        # Encrypt the pixels by applying a simple mathematical operation (XOR)
        encrypted_array = (image_array ^ key)  # XOR operation
        encrypted_array = np.clip(encrypted_array, 0, 255)  # Ensure values are within [0, 255]

        # Save the encrypted image
        encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_image.save(output_path)
        print(f"Encrypted image saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(input_path, output_path, key):
    """Decrypt an image by reversing the pixel manipulation."""
    try:
        image = Image.open(input_path)
        image_array = np.array(image)

        # Decrypt the pixels by reversing the XOR operation
        decrypted_array = (image_array ^ key)  # XOR operation
        decrypted_array = np.clip(decrypted_array, 0, 255)  # Ensure values are within [0, 255]

        # Save the decrypted image
        decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_image.save(output_path)
        print(f"Decrypted image saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Image Encryption/Decryption Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            input_path = input("Enter the path to the input image: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(input_path, output_path, key)

        elif choice == '2':
            input_path = input("Enter the path to the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(input_path, output_path, key)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

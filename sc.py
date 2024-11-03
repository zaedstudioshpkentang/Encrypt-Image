def xor_encrypt_decrypt_image(file_path, password):
    try:
        # Membaca data biner dari gambar
        with open(file_path, "rb") as file:
            file_data = bytearray(file.read())

        # Mengubah password menjadi byte
        password_bytes = password.encode()
        password_length = len(password_bytes)

        # Melakukan operasi XOR pada data biner
        for i in range(len(file_data)):
            file_data[i] ^= password_bytes[i % password_length]

        # Menyimpan file hasil enkripsi atau dekripsi
        if file_path.endswith("_xor"):
            output_file = file_path.replace("_xor", "_decrypted")
        else:
            output_file = file_path + "_xor"

        with open(output_file, "wb") as file:
            file.write(file_data)

        print(f"Operasi selesai. File disimpan sebagai: {output_file}")

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

if __name__ == "__main__":
    print("Pilih Opsi:")
    print("1. Enkripsi Foto")
    print("2. Dekripsi Foto")
    choice = input("Masukkan pilihan (1/2): ")

    file_path = input("Masukkan path foto: ")
    password = input("Masukkan password: ")

    if choice in ["1", "2"]:
        xor_encrypt_decrypt_image(file_path, password)
    else:
        print("Pilihan tidak valid!")
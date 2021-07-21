from functions import read_bin, read_bin2, create_csv


def main():
    print("Hello World!")

    choice = 1
    if choice == 0:
        byte_size = 2068
        bin_data = read_bin(byte_size)
        create_csv(bin_data)

    elif choice == 1:
        filename = "raw_conv_data.csv"
        bin_data2 = read_bin2()
        create_csv(bin_data2, filename)


main()
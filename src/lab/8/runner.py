from service import ConsumerServiceImpl


def main():
    data_file = "./files/consumers.csv"
    service = ConsumerServiceImpl(data_file)

    while True:
        print(f"1. Display states histogram\n"
              f"2. Display states pie chart\n"
              f"3. Display combined states diagram\n"
              f"0. Exit\n")
        option = input("Enter your choice: ")

        if option == "1":
            has_to_be_downloaded = True if input(
                    "Do you want to download the histogram? Enter 'y' or anything else not to download: ") == "y" else False
            service.create_states_histogram(has_to_be_downloaded)
        elif option == "2":
            has_to_be_downloaded = True if input(
                    "Do you want to download the pie chart? Enter 'y' or anything else not to download: ") == "y" else False
            max_quantity = int(input("Enter the maximum quantity of states: "))
            service.create_states_pie_chart(has_to_be_downloaded, max_quantity=max_quantity)
        elif option == "3":
            has_to_be_downloaded = True if input(
                    "Do you want to download the bar chart? Enter 'y' or anything else not to download: ") == "y" else False
            max_quantity = int(input("Enter the maximum quantity of states in the pie chart diagram included: "))
            service.create_combined_diagram(has_to_be_downloaded, max_quantity=max_quantity)
        elif option == "0":
            exit(0)
        else:
            print("Incorrect input. Enter again.")


if __name__ == '__main__':
    main()


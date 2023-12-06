def view_history(calculations_history, decimal_places):
    if len(calculations_history) == 0:
        print("The history is empty")
    else:
        print("Calculation history:")
        for i in calculations_history:
            for j in i:
                if isinstance(j, float):
                    print(str(round(j, decimal_places)) + " ", end="")
                else:
                    print(str(j) + " ", end="")
            print()


def view_settings(decimal_places):
    print("\tSettings:")
    print("\tDecimal places are " + str(decimal_places))

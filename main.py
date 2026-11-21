from data_operations import (add_record, display_records, search_record,
                            update_record, delete_record)
from analysis import show_numpy_analysis, show_pandas_analysis, compare_prices
from report import generate_summary_report
def demonstrate_data_structures():
    # 1. List and list methods
    grocery_list = ["Rice", "Sugar", "Milk"]
    grocery_list.append("Bread")
    grocery_list.sort()
    print("\nLIST:", grocery_list)

    # 2. Tuple
    store_details = ("DMart", "Reliance", "Local Store")
    print("TUPLE (stores):", store_details)

    # 3. Set: stores are unique
    unique_stores = set(store_details)
    print("SET (unique stores):", unique_stores)

    # 4. Dictionary
    sample_prices = {"Rice": 60, "Sugar": 45, "Milk": 58}
    print("DICTIONARY (sample prices):", sample_prices)

    # 5. Dictionary methods
    print("Dictionary keys:", list(sample_prices.keys()))
    print("Dictionary values:", list(sample_prices.values()))
    print("Rice price using get():", sample_prices.get("Rice"))
def main():
    while True:
        print("\n" + "=" * 50)
        print("   GROCERY PRICE COMPARISON & DATA ANALYSIS")
        print("=" * 50)
        print("1. Display all grocery records")
        print("2. Add a new grocery record")
        print("3. Search for a product")
        print("4. Update an existing record")
        print("5. Delete a record")
        print("6. Compare grocery prices")
        print("7. NumPy analysis")
        print("8. Pandas analysis")
        print("9. Generate summary report")
        print("10. Demonstrate Python data structures")
        print("0. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            display_records()
        elif choice == "2":
            add_record()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            compare_prices()
        elif choice == "7":
            show_numpy_analysis()
        elif choice == "8":
            show_pandas_analysis()
        elif choice == "9":
            generate_summary_report()
        elif choice == "10":
            demonstrate_data_structures()
        elif choice == "0":
            print("Thank you for using Grocery Price Analysis System!")
            break
        else:
            print("Invalid choice. Please select from 0 to 10.")
if __name__ == "__main__":
    main()

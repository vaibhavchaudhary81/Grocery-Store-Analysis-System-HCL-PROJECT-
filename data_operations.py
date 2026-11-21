import pandas as pd
FILE_NAME = "grocery_data.csv"
def load_data():
    """Read grocery records from the CSV file."""
    return pd.read_csv(FILE_NAME)
def save_data(df):
    """Save all records back to the CSV file."""
    df.to_csv(FILE_NAME, index=False)
def add_record():
    df = load_data()
    product = input("Enter product name: ").strip().title()
    category = input("Enter category: ").strip().title()
    store = input("Enter store name: ").strip().title()
    try:
        price = float(input("Enter price in rupees: "))
        if price <= 0:
            print("Price must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    next_id = int(df["Record_ID"].max()) + 1 if not df.empty else 1
    new_row = {"Record_ID": next_id, "Product": product,
               "Category": category, "Store": store, "Price": price}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    print("New grocery record added successfully.")
def display_records():
    df = load_data()
    print("\n--- ALL GROCERY RECORDS ---")
    print(df.to_string(index=False))
    print("\nTotal records:", len(df))
def search_record():
    df = load_data()
    product = input("Enter product name to search: ").strip()
    result = df[df["Product"].str.contains(product, case=False, na=False)]
    if result.empty:
        print("No matching product found.")
    else:
        print(result.to_string(index=False))
def update_record():
    df = load_data()
    try:
        record_id = int(input("Enter Record_ID to update: "))
        matches = df.index[df["Record_ID"] == record_id].tolist()
        if not matches:
            print("Record not found.")
            return
        index = matches[0]
        print(df.loc[index].to_string())
        new_price = float(input("Enter new price: "))
        if new_price <= 0:
            print("Price must be greater than zero.")
            return
        df.loc[index, "Price"] = new_price
        save_data(df)
        print("Record updated successfully.")
    except ValueError:
        print("Enter a valid record ID and price.")
def delete_record():
    df = load_data()
    try:
        record_id = int(input("Enter Record_ID to delete: "))
        if record_id not in df["Record_ID"].values:
            print("Record not found.")
            return
        df = df[df["Record_ID"] != record_id]
        save_data(df)
        print("Record deleted successfully.")
    except ValueError:
        print("Please enter a valid record ID.")

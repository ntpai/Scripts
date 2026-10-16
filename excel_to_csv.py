import pandas as pd
from sys import argv, exit

def title_in_name(title, name):
    return True if title in name else False

def create_contact_name(Title: None, Name, Membershipnumber):
    Membershipnumber = str(Membershipnumber)
    
    title_check = title_in_name(title=Title, name=Name)

    if title_check:
        return Membershipnumber + " " + Name
    else:
        return Membershipnumber + " " + Title + " " + Name
    

def main(csv_file: str, out_file: str):
    csv_fd = pd.read_excel(csv_file)
    excel_size = csv_fd.index.size

    export_data = pd.DataFrame(columns=['First Name', 'Phone 1 - Label', 'Phone 1- Value'])
    for i in range(0, excel_size):
        name = create_contact_name(csv_fd['Title'][i], csv_fd['Name'][i], csv_fd['Mem No.'][i])
        export_data.loc[len(export_data)] = [name, "Mobile", f"+91 {csv_fd['Mobile'][i]}"]
   
    export_data.to_csv(out_file, index=False)

if __name__ == "__main__":
    if len(argv) < 3:
        print(f"USAGE: {argv[0]} [file.xlsx] [output_file_name.csv]")
        exit(1)
    main(argv[1], argv[2])
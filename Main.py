import pylibdmtx
from barcode import Code128
from barcode.writer import ImageWriter
import datetime

def get_user_input():
    license_number = input("Enter License Number: ")
    issue_date = input("Enter Issue Date (MMDDYYYY): ")
    expiry_date = input("Enter Expiry Date (MMDDYYYY): ")
    dob = input("Enter Date of Birth (MMDDYYYY): ")
    name = input("Enter Full Name: ")
    address = input("Enter Address: ")

    sex_options = ["M", "F"]
    sex = input("Enter Sex (M/F): ").upper()
    while sex not in sex_options:
        print("Invalid input. Please enter M or F.")
        sex = input("Enter Sex (M/F): ").upper()

    height = input("Enter Height (e.g., 5-10): ")
    weight = input("Enter Weight in lbs: ")

    # Eye color options
    eye_color_options = ["BLU", "BRO", "GRN", "HAZ", "GRY"]
    print("Eye Color Options:", eye_color_options)
    eye_color = input("Enter Eye Color: ").upper()
    while eye_color not in eye_color_options:
        print("Invalid input. Please choose from the provided options.")
        eye_color = input("Enter Eye Color: ").upper()

    # Hair color options
    hair_color_options = ["BLK", "BRO", "BLD", "RED", "SDY", "GRY", "WHI", "UNK"]
    print("Hair Color Options:", hair_color_options)
    hair_color = input("Enter Hair Color: ").upper()
    while hair_color not in hair_color_options:
        print("Invalid input. Please choose from the provided options.")
        hair_color = input("Enter Hair Color: ").upper()

    license_class = input("Enter License Class: ")
    endorsements = input("Enter Endorsements: ")
    restrictions = input("Enter Restrictions: ")

    dd_info = input("Enter DD Information: ")

    return (
        license_number, issue_date, expiry_date, dob, name, address,
        sex, height, weight, license_class, endorsements, restrictions,
        eye_color, hair_color, dd_info
    )

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m%d%Y")
        return True
    except ValueError:
        return False

def generate_barcodes(license_number, issue_date, expiry_date, dob, name, address, sex, height, weight, license_class, endorsements, restrictions, eye_color, hair_color, dd_info):
    # Generate PDF417 barcode
    data_to_encode_pdf417 = f"@  ANSI 636054100002DL00410280ZN03210038DLDAQH{license_number} DCSDILTZ DDEN DAC{ name.replace(' ', '') } DDFN DADA DDGN DCAO DCBB DCDNONE DBD{issue_date} DBB{dob} DBA{expiry_date} DBC1 DAU{sex} in DAY{height} DAG{address} DAJNE DAK{weight} DCF{dd_info} DDAF DDGN DCAO DCBB DCDNONE"
    encoded_data_pdf417 = pylibdmtx.encode(data_to_encode_pdf417)
    barcode_image_pdf417 = pylibdmtx.make_image(encoded_data_pdf417)
    barcode_image_pdf417.save('generated_barcode_pdf417.png')

    # Generate CODE_128 barcode
    data_to_encode_code128 = f"{license_number}{dob}{issue_date}{expiry_date}"
    code128 = Code128(data_to_encode_code128, writer=ImageWriter(), add_checksum=False)
    barcode_image_code128 = code128.save('generated_barcode_code128')

# Example input data for CARD 1
generate_barcodes(
    license_number="13253296",
    issue_date="05252023",
    expiry_date="10282023",
    dob="10281991",
    name="CHRISTIAN A DILTZ",
    address="7788 HIGHLAND ST, RALSTON, NE 68127",
    sex="M",
    height="5-10",
    weight="130 lb",
    license_class="O",
    endorsements="NONE",
    restrictions="B",
    dd_info="054H13253296NENOCO0123146"
)

# Example input data for CARD 2
generate_barcodes(
    license_number="02059268",
    issue_date="10162022",
    expiry_date="10162027",
    dob="10161966",
    name="JACALYN J GROESSER",
    address="7788 HIGHLAND ST, OMAHA, NE 68127",
    sex="F",
    height="5-04",
    weight="154 lb",
    license_class="O",
    endorsements="NONE",
    restrictions="B",
    dd_info="054G02059268NESUCO0122290"
)

# Get user input
user_input = get_user_input()

# Generate barcodes using user input
generate_barcodes(*user_input)

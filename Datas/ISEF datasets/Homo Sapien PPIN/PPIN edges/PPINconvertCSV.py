import csv

txt_file = r"C:\Users\George\Desktop\ISEF datasets\Homo Sapien PPIN\idmapping_2023_09_24.tsv"
csv_file = r"C:\Users\George\Desktop\ISEF datasets\Homo Sapien PPIN\idmapping_2023_09_24.csv"

print(1)
# Open the text file in read mode
with open(txt_file, "r") as file:
    # Read the lines of the text file
    lines = file.readlines()

# Remove leading/trailing whitespaces and split each line by space
data = [line.strip().split() for line in lines[1:]]  # Exclude the header row
print(1)
# Write the data to a CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(lines[0].strip().split())
    # Write the data rows
    writer.writerows(data)

print("CSV file created successfully.")
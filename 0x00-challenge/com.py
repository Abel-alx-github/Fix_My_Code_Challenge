def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    for line_num, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if line1 != line2:
            print(f"Difference at line {line_num}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            print()


compare_files("3-user.py", "test.py")

import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip(), result.stderr.strip()

def main():
    print("Bat dau bai tap Docker Volume...")
    
    print("1. Tao docker volume: easy-volume")
    run_command("docker volume create easy-volume")
    
    print("2. Ghi du lieu vao volume...")
    run_command("docker run --rm -v easy-volume:/data alpine sh -c \"echo 'Luu tru du lieu Docker' > /data/test.txt\"")
    
    print("3. Doc du lieu tu volume...")
    out, err = run_command("docker run --rm -v easy-volume:/data alpine cat /data/test.txt")
    
    print(f"Ket qua doc du lieu: {out}")
    
    if out == "Luu tru du lieu Docker":
        print("Thanh cong! Du lieu duoc luu tru dung.")
    else:
        print("That bai!")

if __name__ == "__main__":
    main()

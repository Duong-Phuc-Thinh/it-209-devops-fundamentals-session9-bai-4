# Bài 4: Lưu trữ dữ liệu đơn giản với Docker Volume

## Giới thiệu
Bài tập này hướng dẫn cách sử dụng Docker Named Volume để lưu trữ dữ liệu bền vững, đảm bảo dữ liệu không bị mất khi container bị dừng hoặc xóa.

## Các bước thực hiện
1. Tạo Docker Volume:
   ```bash
   docker volume create easy-volume
   ```
2. Ghi dữ liệu vào volume bằng Alpine container:
   ```bash
   docker run --rm -v easy-volume:/data alpine sh -c "echo 'Luu tru du lieu Docker' > /data/test.txt"
   ```
3. Đọc dữ liệu từ volume bằng container thứ hai:
   ```bash
   docker run --rm -v easy-volume:/data alpine cat /data/test.txt
   ```

## Hướng dẫn chạy chương trình Python
Chương trình Python tự động hóa việc kiểm tra sự tồn tại của volume và đọc nội dung file thông qua Python subprocess.

```bash
python main.py
```
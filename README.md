pip3 install -r requirements.txt

python3 main.py

# prak1v2

chức năng trong file
setup.py:
    File setup.py này cung cấp tất cả thông tin cần thiết để đóng gói và phân phối dự án của bạn. Khi chạy lệnh như python setup.py install hoặc sử dụng pip install . trong thư mục chứa file setup.py, các thông tin này sẽ được sử dụng để cài đặt dự án cùng với các phụ thuộc, và tạo ra một command-line script có tên là prak1 để chạy chương trình.

main.py:
    File main.py thực hiện các bước sau:

        Phân tích đối số:
        Xác định đường dẫn dữ liệu và thời gian timeout.

        Khởi tạo file kết quả:
        Tạo hoặc làm trống file results.txt để ghi kết quả.

        Thu thập file:
        Duyệt thư mục dữ liệu và xây dựng danh sách các file cần xử lý.

        Xử lý file:
        Với mỗi file, trích xuất văn bản (sử dụng hàm process_file), phân loại văn bản (sử dụng hàm custom_classify) dựa trên từ khóa bằng regex, và ghi kết quả vào file results.txt.

        Kết thúc:
        Khi tất cả các file đã được xử lý (hoặc khi vượt quá timeout), chương trình kết thúc mà không in ra bất kỳ thông báo nào trên terminal (tất cả thông tin được ghi vào file kết quả).


File file_processor.py cung cấp các hàm xử lý và trích xuất văn bản từ nhiều định dạng file khác nhau


File deepseak_r1.py có chức năng chính là:
    Khởi tạo một pipeline phân loại văn bản sử dụng mô hình DeepSeek-R1 từ Hugging Face Hub.
    Xử lý các trường hợp lỗi (ví dụ như lỗi xác thực hoặc mô hình không tồn tại) bằng cách chuyển sang sử dụng một mô hình dự phòng.
    Cung cấp phương thức classify để nhận đầu vào là văn bản và trả về kết quả phân loại.


File ocr.py có nhiệm vụ:
    Xác định định dạng file từ đường dẫn được cung cấp.
    Nếu file là PDF:
    Chuyển đổi từng trang PDF thành ảnh.
    Thực hiện OCR trên từng ảnh để trích xuất văn bản.
    Nếu file là ảnh:
    Mở ảnh và thực hiện OCR để chuyển đổi hình ảnh chứa văn bản thành chuỗi văn bản.
    Sử dụng pytesseract với hỗ trợ ngôn ngữ (eng) để cải thiện khả năng nhận dạng cho các văn bản có thể chứa nhiều ngôn ngữ.
    Xử lý lỗi và trả về chuỗi rỗng nếu không thể trích xuất được văn bản.


cách hoạt động:
    
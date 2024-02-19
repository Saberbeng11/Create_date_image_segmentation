# Tạo môi trường ảo, chạy: 
    pip istall -r .\requirements.txt
# Giải thích chức năng:
- Ta có tập ảnh dữ liệu gốc "original image", tập "masks" là tập annotation trên Cvat (một tool annotate), tập "label" nơi lưu vị các file ghi vị trí tạo độ cần để train segmentation
- File main.py duyệt qua các ảnh trong tập "mask" đưa vào dạng ảnh xám.
- Nhờ có các giá trị điểm ảnh khác nhau lọc ra các class rồi trích xuất đường biên của chúng và ghi lại vào các file .txt tương ứng để hoàn thành tập dữ liệu cần để train YOLOv8 segmentation
# Ứng dụng của đoạn code:
- Giảm thời gian chuẩn bị dữ liệu tập train cho các mô hình image segmentation 
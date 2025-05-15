# Dự đoán bệnh dựa trên triệu chứng lâm sàng

## Giới thiệu
Dự án này sử dụng các kỹ thuật xử lý ngôn ngữ tự nhiên (NLP) để dự đoán bệnh dựa trên các triệu chứng lâm sàng do người dùng nhập vào. Hệ thống được xây dựng với Flask để cung cấp API cho việc nhập dữ liệu và nhận kết quả dự đoán.

## Công nghệ sử dụng
- **TF-IDF**: Biểu diễn văn bản dưới dạng vector để phục vụ cho mô hình máy học.
- **SVM (Support Vector Machine)**: Mô hình máy học truyền thống để phân loại bệnh.
- **LSTM (Long Short-Term Memory)**: Mô hình học sâu để xử lý chuỗi văn bản.
- **Flask**: Framework nhẹ để xây dựng API phục vụ cho việc nhập triệu chứng và nhận kết quả dự đoán.

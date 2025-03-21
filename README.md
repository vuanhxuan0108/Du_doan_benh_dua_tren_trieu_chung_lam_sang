# Dự đoán bệnh dựa trên triệu chứng lâm sàng

## Giới thiệu
Dự án này sử dụng các kỹ thuật xử lý ngôn ngữ tự nhiên (NLP) để dự đoán bệnh dựa trên các triệu chứng lâm sàng do người dùng nhập vào. Hệ thống được xây dựng với Flask để cung cấp API cho việc nhập dữ liệu và nhận kết quả dự đoán.

## Công nghệ sử dụng
- **TF-IDF**: Biểu diễn văn bản dưới dạng vector để phục vụ cho mô hình máy học.
- **SVM (Support Vector Machine)**: Mô hình máy học truyền thống để phân loại bệnh.
- **LSTM (Long Short-Term Memory)**: Mô hình học sâu để xử lý chuỗi văn bản.
- **Flask**: Framework nhẹ để xây dựng API phục vụ cho việc nhập triệu chứng và nhận kết quả dự đoán.

## Cách cài đặt và chạy dự án

### 1. Cài đặt môi trường
Trước tiên, cần cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 2. Chạy API Flask
```bash
python app.py
```
API sẽ chạy trên `http://127.0.0.1:5000/`.

### 3. Sử dụng API
API nhận đầu vào là một danh sách triệu chứng và trả về dự đoán bệnh.

#### Gửi yêu cầu dự đoán bệnh
```bash
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d '{"symptoms": "sốt, ho, đau họng"}'
```
#### Phản hồi mẫu từ API:
```json
{
  "predicted_disease": "Cảm cúm",
  "confidence": 0.85
}
```

## Cấu trúc thư mục
```
├── app.py  # Flask API
├── model/  # Chứa mô hình đã huấn luyện
├── data/   # Dữ liệu huấn luyện
├── requirements.txt  # Các thư viện cần thiết
└── README.md  # Tài liệu hướng dẫn
```

## Đóng góp
Nếu bạn muốn đóng góp vào dự án, hãy fork repository này và tạo pull request. Cảm ơn sự đóng góp của bạn!

## Giấy phép
Dự án này được phát hành theo giấy phép MIT.


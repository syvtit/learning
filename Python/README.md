## B1:
Sử dụng tool pyinstaller để compile thành file thực thi exe
- Tạo thành 1 file thực thi duy nhất (bao gồm tất cả thư viện, … trong file này): pyinstaller –onefile python_script_name.py
- noupx: việc sử dụng UPX sẽ giúp nén file thực thi làm file tạo ra nhỏ hơn, tuy nhiên việc sử dụng upx cũng sẽ có một số phần mềm chống mã độc phát hiện và không cho phép thực thi. Sử dụng option này để ko sử dụng upx: pyinstaller –noupx python_script_name.py
## B2:
Truy cập vào thư mục dist để lấy file thực thi

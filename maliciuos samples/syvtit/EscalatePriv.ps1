# Kiểm thử hành vi leo thang/định danh
# Kỳ vọng: Ghi nhận chuỗi hành vi dùng để đánh giá hệ thống, flag trong EDR nếu profile bật.
Start-Process cmd.exe -ArgumentList '/c whoami && net user && ipconfig /all && systeminfo'



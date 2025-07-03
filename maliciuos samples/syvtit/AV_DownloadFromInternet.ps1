#Kiểm thử tải file từ internet
#Kỳ vọng: Nếu có DNS Filtering/Firewall integration → alert hoặc log hành vi tải file từ domain.
Invoke-WebRequest -Uri "http://speedtest.tele2.net/10MB.zip" -OutFile "$env:TEMP\download.zip"

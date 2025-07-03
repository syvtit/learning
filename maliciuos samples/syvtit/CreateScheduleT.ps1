# Tạo tiến trình script giả lập persit
# Kỳ vọng: XDR flag hành vi thiết lập persist (Task Scheduler).
schtasks /create /tn "FakePersist" /tr "calc.exe" /sc onlogon


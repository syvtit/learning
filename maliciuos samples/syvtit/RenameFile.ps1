# Mô phỏng hành vi mã hóa - ransomware
# Kỳ vọng: Alert hành vi ransomware (rapid file change).
Get-ChildItem "C:\syvtit-testing" -Recurse -Include *.txt |
ForEach-Object {
  $content = Get-Content $_.FullName
  Set-Content -Path "$($_.FullName).enc" -Value $content
  Remove-Item $_.FullName
}


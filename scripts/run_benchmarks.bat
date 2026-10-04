@echo off
set SERVER_IP=192.168.0.108
set TIMESTAMP=%date:~-4%_%date:~3,2%_%date:~0,2%__%time:~0,2%_%time:~3,2%_%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

echo ========================================================
echo   Wi-Fi Performance Benchmark Automation Suite
echo ========================================================
set /p TEST_LABEL="Enter Test ID (e.g., W24_A, W50_A, ETH_01): "

echo.
echo Running Run 1 (UDP 100M, 20s)...
iperf3.exe -c %SERVER_IP% -u -b 100M -t 20 > "log_%TEST_LABEL%_run1_%TIMESTAMP%.txt"
timeout /t 3 > nul

echo Running Run 2 (UDP 100M, 20s)...
iperf3.exe -c %SERVER_IP% -u -b 100M -t 20 > "log_%TEST_LABEL%_run2_%TIMESTAMP%.txt"
timeout /t 3 > nul

echo Running Run 3 (UDP 100M, 20s)...
iperf3.exe -c %SERVER_IP% -u -b 100M -t 20 > "log_%TEST_LABEL%_run3_%TIMESTAMP%.txt"
timeout /t 3 > nul

echo Running TCP Throughput Peak Test (15s)...
iperf3.exe -c %SERVER_IP% -t 15 > "log_%TEST_LABEL%_tcp_%TIMESTAMP%.txt"

echo.
echo Benchmark for %TEST_LABEL% completed successfully!
echo Files saved with prefix log_%TEST_LABEL%
pause
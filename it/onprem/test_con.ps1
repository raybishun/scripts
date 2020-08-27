
$computerList = Get-Content ".\test_con_list.txt"

$total = 0
$failed = 0

Write-Host "Unreachable hosts:"

foreach($computer in $computerList)
{
    $total++

    try
    {
        # Return 'False if not reachable
        # ---------------------------------------------------------------------
        # Test-Connection -ComputerName $computer -Count 1 -Quiet

        # Show exception adn verbose ping info
        # ---------------------------------------------------------------------
        # Test-Connection -ComputerName $computer -Count 1 -ErrorAction Stop

        # Show exception
        # ---------------------------------------------------------------------
        $null = Test-Connection -ComputerName $computer -Count 3 -ErrorAction Stop
    }
    catch
    {   
        Write-Output "$computer - $($_.Exception.Message)"
        $failed++
    }
}

Write-Host "$failed/$total"
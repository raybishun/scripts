# =============================================================================
# Shutdown ESXi Lab VMs
# =============================================================================
Clear-Host

$computers = @("vmcentos8splunk", "vmw2k19eval1", "vmw2k16sccm19", "vmw2k12r2sql16", "vmw2k12r2dc1", "vmw2k12r2dc0")

$admin = Get-Credential domain\userId

foreach($computer in $computers)
{
    Write-Host $computer

    try
    {
        Stop-Computer -ComputerName $computer -Force -Credential $admin -ErrorAction Stop
        
        Start-Sleep -s 120
    }
    catch
    {
        Write-Host $_.Exception.Message
    }
}

Write-Host "Done."
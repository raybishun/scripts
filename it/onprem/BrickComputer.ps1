# =============================================================================
# File Name: BrickComputer.ps1
# Version: 1.0
# Author: Ray Bishun
# Creation Date: Wednesday, December 16, 2020
# Purpoose: Brick a BitLocker encrypted comptuer if not connected
#           to Active Directory for 40 ro more days
# =============================================================================
param (
    [string]$ComputerName = ([System.Net.Dns]::GetHostName()),
    [int]$BrickWatermark = 40
)

try {
    $today = (Get-Date)
    $lastLogon = (Get-AdComputer $ComputerName -Properties LastLogonDate).LastLogonDate
    $age = New-TimeSpan -Start $lastLogon -End $today

    if ($age.Days -ge $BrickWatermark) {
        Write-Output "Execute --> 1 of 2: manage-bde -ForceRecovery"
        Write-Output "Execute --> 2 of 2: shutdown -t 0 -r"
        Write-Output $age.Days
        return "Brick initiated on $ComputerName."
    }
    else{
        # Remove else statement in production
        Return "OK, below BrickWatermark."
    }
}
catch [Microsoft.ActiveDirectory.Management.ADServerDownException]{
    Write-Output $($_.Exception.GetType().FullName)
    Write-Output $($_.Exception.Message)
}
catch {
    # Write-Output $($_.Exception.Message)
    Write-Output $($_.Exception.GetType().FullName)
}
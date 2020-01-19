# =============================================================================
# Prerequisites 
# =============================================================================
#   1. An Azure Subscription
#   2. An Azure Key Vault
#   3. An Azure Virtual Machine
#   4. NOTE #1: Only Standard or above VMs support disk encryption
#   5. NOTE #2: The VM and Key Vault must be in the same region

# =============================================================================
# Key Vault Info
# =============================================================================
$keyVaultName   = ""
$keyVaultRgName = ""
$myKey          = ""

# =============================================================================
# VM Info
# =============================================================================
$vmRgName       = ""
$vmName         = ""

try
{
    # Authenticate
    Connect-AzureRmAccount

    # =========================================================================
    # Encrypt Disk
    # =========================================================================
    $keyVault = Get-AzureRmKeyVault -VaultName $keyVaultName -ResourceGroupName $keyVaultRgName;
    $diskEncryptionKeyVaultUrl = $keyVault.VaultUri;
    $keyVaultResourceId = $keyVault.ResourceId;
    $keyEncryptionKeyUrl = (Get-AzureKeyVaultKey -VaultName $keyVaultName -Name $myKey).Key.kid;

    Set-AzureRmVMDiskEncryptionExtension -ResourceGroupName $vmRgName `
        -VMName $vmName `
        -DiskEncryptionKeyVaultUrl $diskEncryptionKeyVaultUrl `
        -DiskEncryptionKeyVaultId $keyVaultResourceId `
        -KeyEncryptionKeyUrl $keyEncryptionKeyUrl `
        -KeyEncryptionKeyVaultId $keyVaultResourceId
}
catch
{
    Write-Host $_.Exception.Message
}
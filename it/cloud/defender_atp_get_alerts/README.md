# How to get alerts from Defender ATP using PowerShell

### Overview
1. Register an app in Azure
2. Create and run a PowerShell script to get alerts

### Requirements
1. Global Administrator is required to register Azure apps

## Steps

### App registration
1. http://portal.azure.com/
2. Azure Active Directory
3. App registration
4. New registration
5. Name: ATP_Demo
6. Who can use this app or access this API: Accounts in this org directory only...
7. Redirect URI: Leave at default
8. Register

### Add the WindowsDefenderATP API
1. View API permissions
2. You should find Microsoft Graph (1), User.Read already assigned by default
3. Add a permissions
4. APIs my organization uses
5. Search for: WindowsDefenderATP
6. Select WindowsDefenderATP

### Set (read-only) permissions 
1. Select - Application permissions (Your app runs as a background service or daemon without a signed-in user)
2. Under Permissions, select the below

	- AdvancedQuery\AdvancedQuery.Read.All (Run advanced queries)
	- Alert\Alert.Read.All (Read all alerts)
	- File\File.Read.All (Read file profiles)
	- Ip\Ip.Read.All (Read IP address profiles)
	- Machine\Machine.Read.All (Read all machine profiles)
	- Score\Score.Read.All (Read Threat and Vulnerability Management score)
	- SecurityConfiguration\SecurityConfiguration.Read.All (Read Threat and Vulnerability Management security information)
	- SecurityRecommendation\SecurityRecommendation.Read.All (Read Threat and Vulnerability Management security recommendations)
	- Software\Software.Read.All (Read Threat and Vulnerability Management software information)
	- Ti\Ti.Read.All (read all IOCs)
	- Url\Url.Read.All (Read URL profiles)
	- User\User.Read.All (Read user profiles)
	- Vulnerability\Vulnerability.Read.All (Read Threat and Vulnerability Management vulnerability information)
3. Add permissions

### Grant consent
1. Grant admin consent for <entity that has a subscription to this tenant>

### Add a secret to the app
1. Certificates & secrets
2. Client secrets\New client secret
3. Select the client secret's expiration: from 1, 2, or never expire
4. Add
5. You must now save the generated value to a secret store - you will never see it again

### Retrieve the app's ID and your tenant ID
1. Overview
2. Application (client) ID
3. Directory (tenant) ID

### Validate your token
1. https://jwt.ms/

### References
1. Microsoft Defender ATP API - Hello World: https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/api-hello-world
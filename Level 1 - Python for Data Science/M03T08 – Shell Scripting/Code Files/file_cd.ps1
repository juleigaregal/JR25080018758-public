# file_cd.ps1

# Create three main folders
New-Item -ItemType Directory -Name "FolderA"
New-Item -ItemType Directory -Name "FolderB"
New-Item -ItemType Directory -Name "FolderC"

# Navigate into FolderA
Set-Location -Path "FolderA"

# Create three subfolders inside FolderA
New-Item -ItemType Directory -Name "Subfolder1"
New-Item -ItemType Directory -Name "Subfolder2"
New-Item -ItemType Directory -Name "Subfolder3"

# Remove two of the subfolders
Remove-Item -Recurse -Force "Subfolder2"
Remove-Item -Recurse -Force "Subfolder3"

# Return to original location
Set-Location -Path ..
Write-Output "file_cd script executed successfully."

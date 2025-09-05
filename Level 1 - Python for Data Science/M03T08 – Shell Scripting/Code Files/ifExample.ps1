# ifExample.ps1

# If statement: create if_folder if new_folder exists
if (Test-Path -Path "new_folder") {
    New-Item -ItemType Directory -Name "if_folder"
}

# If-Else statement: create hyperionDev if if_folder exists, else create new-projects
if (Test-Path -Path "if_folder") {
    New-Item -ItemType Directory -Name "hyperionDev"
} else {
    New-Item -ItemType Directory -Name "new-projects"
}

Write-Output "ifExample script executed successfully."

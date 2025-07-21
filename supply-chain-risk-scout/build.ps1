param(
    [string]$Command
)

switch ($Command) {
    "install" { pip install -r requirements.txt }
    "lint" { ruff check src; black --check src }
    "test" { pytest }
    "dev" { docker-compose up --build }
    default { Write-Host "Usage: .\build.ps1 [install|lint|test|dev]" }
} 
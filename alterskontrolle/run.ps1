# Reset Env Variables
if ($null -ne $env:RUST_LOG) {
    Remove-Item -Path "Env:RUST_LOG"
}

$level = "warn"
$mode = "default"
$watch = "default"
$reset_vars_only = "no"

for ($i = 0; $i -lt $args.Length; $i++) {
    switch ($args[$i]) {
        "-t" {
            $level = "trace"
        }
        "--trace" {
            $level = "trace"
        }
        "-d" {
            $level = "debug"
        }
        "--debug" {
            $level = "debug"
        }
        "-i" {
            $level = "info"
        }
        "--info" {
            $level = "info"
        }
        "-w" {
            $level = "warn"
        }
        "--warn" {
            $level = "warn"
        }
        "-e" {
            $level = "error"
        }
        "--error" {
            $level = "error"
        }
        # Mode
        "-r" {
            $mode = "release"
        }
        "-re" {
            $mode = "release"
        }
        "--release" {
            $mode = "release"
        }
        # Watch?
        "-wa" {
            $watch = "watch"
        }
        "--watch" {
            $watch = "watch"
        }
        # Reset Env Variables
        "-rv" {
            $reset_vars_only = "yes"
        }
        "--reset-vars" {
            $reset_vars_only = "yes"
        }
        default {
            $level = "warning"
            $mode = "default"
            $watch = "default"
            $reset_vars_only = "no"
            Write-Host "Unknown argument: $($args[$i])"
        }
    }
}

# Run Program if not only resetting env variables
if ($reset_vars_only -eq "no") {

    # Set ENV Variables
    $env:RUST_LOG = $level;

    # Watch
    if ($watch -eq "watch") {
        # Run Program in Release Mode with Watch
        if ($mode -eq "release") {
            cargo watch -c -x "run --release"
        }
        # Run Program in the Default Mode with Watch
        else {
            cargo watch -c -x "run"
        }
    }
    # No Watch
    else {
        # Run Program in Release Mode
        if ($mode -eq "release") {
            cargo run --release
        }
        # Run Program in the Default Mode
        else {
            cargo run
        }
    
    }
}

# Reset Env Variables
if ($null -ne $env:RUST_LOG) {
    Remove-Item -Path "Env:RUST_LOG"
}

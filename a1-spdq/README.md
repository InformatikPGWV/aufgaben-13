# AstragoDE's Rust Template

## About this template

This template contains a basic Rust project with the pretty_env_logger crate and a basic logger setup.
It is recommended that you use the [Cargo Generate](https://github.com/cargo-generate/cargo-generate) crate to initialize a new project with this template.

If you want to use the `--watch` flag of the `run.ps1` script, you need to install [cargo-watch](https://github.com/watchexec/cargo-watch).

## Using this template

Install [Cargo Generate](https://github.com/cargo-generate/cargo-generate) by running `cargo install cargo-generate` in your terminal.

Then run

```bash
cargo generate --git https://github.com/AstragoDETechnologies/rust_template.git
```

## Adding the template as a favourite to Cargo Generate

To add this template as a favourite to [Cargo Generate](https://github.com/cargo-generate/cargo-generate) add the following snippit to your `$CARGO_HOME/cargo-generate.toml` file. [By default](https://doc.rust-lang.org/cargo/guide/cargo-home.html#cargo-home) this file is located at `$HOME/.cargo/cargo-generate.toml`.
If the file does not exist, create it.

```toml
[favorites.astra]
description = "AstragoDE's default Rust template."
git = "https://github.com/AstragoDETechnologies/rust_template.git"
branch = "main"
vcs = "Git"
```

You can then initialize a new project with this template by running `cargo generate astra`.

{ pkgs }: {
  deps = [
    # Rust
    pkgs.rustc
	pkgs.rustfmt
	pkgs.cargo
	pkgs.cargo-edit
    pkgs.cargo-watch
    pkgs.cargo-binstall
    pkgs.rust-analyzer

    # Python
    pkgs.python312
    pkgs.poetry
    pkgs.pipx
    pkgs.black

    # Utilities
    pkgs.htop
    
    # other Dependencies
      # OpenSSL
        pkgs.openssl.dev
        pkgs.pkg-config
      # Console
        pkgs.powershell
  ];
  env = {
    # OpenSSL
    PKG_CONFIG_PATH = "${pkgs.openssl.dev}/lib/pkgconfig";
  };
}
{ pkgs }: {
  deps = [
    # Rust
    pkgs.rustc
	pkgs.rustfmt
	pkgs.cargo
	pkgs.cargo-edit
    pkgs.rust-analyzer
    
    # other Dependencies
    pkgs.openssl.dev
    pkgs.powershell
  ];
  env = {
    PKG_CONFIG_PATH = "${pkgs.openssl.dev}/lib/pkgconfig";
  };
}
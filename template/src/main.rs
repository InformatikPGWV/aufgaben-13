// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

// // Import astralib (use `cargo update` to download the library)
// #[allow(unused_imports)]
// extern crate astralib;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    println!("Hello World!");
}

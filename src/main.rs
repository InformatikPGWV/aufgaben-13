// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    println!("Hello World!");
}

// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    let liste: [i32; 5] = [1, 2, 3, 4, 5];

    let mut sum = 0;

    for element in liste {
        sum += element;
    }

    let mittel: f64 = sum as f64 / liste.len() as f64;

    println!("Summe: {}", sum);
    println!("Mittel: {}", mittel);
}

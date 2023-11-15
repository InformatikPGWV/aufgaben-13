// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;
use tracing_subscriber;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    debug!("Wait for Input");
    let eingabe: String = iolib::input("Eingabe: ").unwrap();

    debug!("Convert input to seperate numbers in Vector");
    let mut numbers: Vec<f64> = Vec::new();
    for number_as_str in eingabe.split_ascii_whitespace() {
        match number_as_str.parse::<f64>() {
            Ok(number) => numbers.push(number),
            Err(error) => error!("Failed to parse '{}': {}", number_as_str, error),
        }
    }

    debug!("Calculate sum");
    let mut sum = 0.0;
    for element in &numbers {
        sum += element;
    }

    debug!("Calculate average");
    let mittel: f64 = sum / numbers.len() as f64;

    debug!("Print Results");
    println!("Summe: {}", sum);
    println!("Mittel: {}", mittel);
}

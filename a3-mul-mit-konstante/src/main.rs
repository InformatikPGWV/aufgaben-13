// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

use iolib;

fn main() {
    const KONSTANTE: f64 = 5.0;

    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    debug!("reading file");
    let input_contents = iolib::read_file("./input.txt").unwrap();

    debug!("Creating Output Variable");
    let mut output = String::new();

    input_contents
        .lines()
        .enumerate()
        .for_each(|(index, number_as_str)| {
            debug!("Parsing line {}", index + 1);
            match number_as_str.parse::<f64>() {
                Ok(number) => {
                    debug!("Calculating result");
                    let result = number * KONSTANTE;
                    output.push_str(&format!("{}\n", result));
                }
                Err(e) => {
                    error!("Failed to parse '{}': {}", number_as_str, e);
                    output.push_str("Error calculating Result\n");
                }
            }
        });

    debug!("Writing output to file");
    iolib::write_file("./output.txt", &output).unwrap();
}

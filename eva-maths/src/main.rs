// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

use iolib;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    debug!("reading file");
    let input_contents = iolib::read_file("./input.txt").unwrap();

    debug!("Preparing result variables");
    let mut sum: f64 = 0.0;
    let mut product: f64 = 1.0;
    let mut difference: f64 = 0.0;
    let mut quotient: f64 = 0.0;

    input_contents
        .lines()
        .enumerate()
        .for_each(|(index, number_as_str)| {
            debug!("Parsing line {}", index + 1);
            match number_as_str.parse::<f64>() {
                Ok(number) => {
                    debug!("Calculating result");
                    sum += number;
                    product *= number;
                    if index == 0 {
                        difference = number;
                        quotient = number;
                    } else {
                        difference -= number;
                        quotient /= number;
                    }
                }
                Err(e) => error!("Failed to parse '{}': {}", number_as_str, e),
            }
        });

    debug!("Generating output");

    let mut output_contents: String = String::new();

    output_contents.push_str(&format!("Summe: {}\n", sum));
    output_contents.push_str(&format!("Produkt: {}\n", product));
    output_contents.push_str(&format!("Differenz: {}\n", difference));
    output_contents.push_str(&format!("Quotient: {}\n", quotient));

    debug!("Writing output to file");
    iolib::write_file("./output.txt", &output_contents).unwrap();
}

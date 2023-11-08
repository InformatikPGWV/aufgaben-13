// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

mod io;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    debug!("reading file");
    let input_contents = io::read_file("./input.txt").unwrap();

    debug!("Preparing result variables");
    let mut sum: f64 = 0.0;
    let mut product: f64 = 1.0;
    let mut difference: f64 = 0.0;
    let mut quotient: f64 = 0.0;

    input_contents.lines().enumerate().for_each(|(idx, line)| {
        debug!("Parsing line {}", idx + 1);
        let num: f64 = line.parse().unwrap();
        debug!("Calculating result");
        sum += num;
        product *= num;
        if idx == 0 {
            difference = num;
            quotient = num;
        } else {
            difference -= num;
            quotient /= num;
        }
    });

    debug!("Generating output");

    let mut output_contents: String = String::new();

    output_contents.push_str(&format!("Summe: {}\n", sum));
    output_contents.push_str(&format!("Produkt: {}\n", product));
    output_contents.push_str(&format!("Differenz: {}\n", difference));
    output_contents.push_str(&format!("Quotient: {}\n", quotient));

    debug!("Writing output to file");
    io::write_file("./output.txt", &output_contents).unwrap();
}

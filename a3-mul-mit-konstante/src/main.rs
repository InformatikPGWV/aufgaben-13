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

    input_contents.lines().enumerate().for_each(|(idx, line)| {
        debug!("Parsing line {}", idx + 1);
        let num: f64 = line.parse().unwrap();

        debug!("Calculating result");
        let result = num * KONSTANTE;
        output.push_str(&format!("{}\n", result));
    });

    debug!("Writing output to file");
    iolib::write_file("./output.txt", &output).unwrap();
}

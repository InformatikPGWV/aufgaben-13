// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

use iolib;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    let eingabe = iolib::input("Wie alt bist du?: ").unwrap();

    let eingabe = eingabe.parse::<i32>().expect("Alter als Ganzzahl");

    if eingabe >= 18 {
        println!("Du bist alt genug, um Auto zu fahren. Du braucht trotzdem eine Fahrerlaubnis!");
    } else {
        println!("Du darfst nicht ans Steuer!")
    }
}

// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

use iolib;

fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    let eingabe = iolib::input("Zahl: ").unwrap();

    let eingabe = eingabe.parse::<i32>().unwrap();

    if is_prime(eingabe) {
        println!("{} ist eine Primzahl!", eingabe);
    } else {
        println!("{} ist KEINE Primzahl!", eingabe);
    }
}

fn is_prime(number: i32) -> bool {
    if number <= 1 {
        return false;
    }
    for i in 2..number {
        if number % i == 0 {
            return false;
        }
    }
    true
}

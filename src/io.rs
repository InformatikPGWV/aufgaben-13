use std::{error::Error, io::Write};
pub fn input(prompt: &str) -> Result<String, Box<dyn Error>> {
    print!("{}", prompt);
    match std::io::stdout().flush() {
        Err(_) => {
            println!("");
        }
        _ => (),
    }
    let mut input: String = String::new();
    std::io::stdin().read_line(&mut input)?;
    input = input.trim().to_string();
    Ok(input)
}

pub fn read_file(filename: &str) -> Result<String, Box<dyn Error>> {
    let contents: String = std::fs::read_to_string(filename)?;
    Ok(contents)
}

use std::path::Path;
pub fn write_file(filename: &str, contents: &str) -> Result<(), Box<dyn Error>> {
    let mut file = std::fs::File::create(Path::new(filename))?;
    file.write_all(contents.as_bytes())?;
    Ok(())
}

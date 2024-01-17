// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

// // Import astralib (use `cargo update` to download the library)
// #[allow(unused_imports)]
// extern crate astralib;

use serde_json::Value;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();
    
    debug!("Sending Request to API.");
    let body = reqwest::get("https://www.tagesschau.de/api2/news/?regions=9&resort=inland")
        .await
        .expect("The Request should return a Response.")
        .text()
        .await
        .expect("The Result should contain text.");

    debug!("Parsing Response.");
    let data: Value = serde_json::from_str(&body).expect("The data should be in JSON.");

    debug!("Extracting news.");
    let news = data["news"].as_array().expect("News should be available.");

    debug!("Displaying article previews.");
    for article in news {
        trace!("Printing Article preview.");
        println!(
            "{} - {}\n",
            article["title"].as_str().expect("The title should be available as a str."),
            article["firstSentence"].as_str().expect("The first sentence should be available as a str.")
        );
    }
}

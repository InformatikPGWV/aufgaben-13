// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

// // Import astralib (use `cargo update` to download the library)
// #[allow(unused_imports)]
// extern crate astralib;

use serde_json::Value;

#[tokio::main(flavor = "current_thread")]
async fn main() {
    let body = reqwest::get("https://www.tagesschau.de/api2/news/?regions=9&resort=inland")
        .await
        .expect("The Request should return a Response.")
        .text()
        .await
        .expect("The Result should contain text.");

    let data: Value = serde_json::from_str(&body).expect("The data should be in JSON.");

    let news = data["news"].as_array().expect("News should be available");
    for article in news {
        println!(
            "{} - {}\n",
            article["title"].as_str().expect("The title should be available as a str."),
            article["firstSentence"].as_str().expect("The first sentence should be available as a str.")
        );
    }
}

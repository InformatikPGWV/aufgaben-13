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

    for i in 0..=3 {
        let article = &data["news"][i];
        println!("{} - {}", &article["title"], &article["firstSentence"]);
    }
}

// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

// Import astralib (use `cargo update` to download the library)
#[allow(unused_imports)]
extern crate astralib;

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

    display_news_preview(&data);

    loop {
        let choice = astralib::io::input("Welchen Artikel möchten Sie lesen?: ")
            .expect("choice should be read.");

        if let Ok(choice) = choice.parse::<usize>() {
            if &choice
                <= &data["news"]
                    .as_array()
                    .expect("News should be available.")
                    .len()
            {
                display_news(&data, choice);
                
                break;
            } else {
                error!("User selected article that is out of range!");
                continue;
            }
        } else {
            error!("Failed to parse into u32");
        }
    }
}

fn display_news_preview(data: &Value) {
    debug!("Extracting news.");
    let news = &data["news"].as_array().expect("News should be available.");

    debug!("Displaying article previews.");
    for (idx, article) in news.iter().enumerate() {
        trace!("Printing Article preview.");
        println!(
            "Artikel {:02}:\n\t {} - {}\n",
            (idx + 1),
            article["title"]
                .as_str()
                .expect("The title should be available as a str."),
            article["firstSentence"]
                .as_str()
                .expect("The first sentence should be available as a str.")
        );
    }
}

fn display_news(data: &Value, choice: usize) {
    // TODO: Implement reading inside of console using the details file.
    let url = &data["news"][choice - 1]["detailsweb"]
        .as_str()
        .expect("The URL should be available.");
    match open::that(url) {
        Ok(_) => {
           
        }
        Err(error) => {
            error!("Could not open article: {:#?}", error);
            println!(
                "Could not open article automatically. Please visit\n{}",
                url
            )
            
        }
    }

    
}

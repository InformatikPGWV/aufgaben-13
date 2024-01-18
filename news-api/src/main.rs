// Import tracing (Logger)
#[allow(unused_imports)]
use tracing::*;

// Import astralib (use `cargo update` to download the library)
#[allow(unused_imports)]
extern crate astralib;

use regex::Regex;
use serde_json::Value;
use std::collections::HashSet;

// Use the current_thread runtime for the main function
// #[tokio::main(flavor = "current_thread")]
fn main() {
    // Initialize tracing (Logger)
    tracing_subscriber::fmt::init();

    debug!("Sending Request to API.");
    // Send a GET request to the Tagesschau API and retrieve the response body
    let body =
        reqwest::blocking::get("https://www.tagesschau.de/api2/news/?regions=9&resort=inland")
            .expect("The Request should return a Response.")
            .text()
            .expect("The Result should contain text.");

    debug!("Parsing Response.");
    // Parse the response body as JSON
    let data: Value = serde_json::from_str(&body).expect("The data should be in JSON.");

    // Display a preview of the news articles
    display_news_preview(&data);

    // Prompt the user to choose an article until a valid choice is made
    loop {
        let choice = astralib::io::input("Welchen Artikel möchten Sie lesen?: ")
            .expect("choice should be read.")
            .trim()
            .to_string();

        if let Ok(choice) = choice.parse::<usize>() {
            if choice <= 0 {
                error!("User selected article that is out of range.");
                continue;
            }

            if &choice
                <= &data["news"]
                    .as_array()
                    .expect("News should be available.")
                    .len()
            {
                // Display the selected news article
                display_news(&data, choice);
                break;
            } else {
                error!("User selected article that is out of range.");
                continue;
            }
        } else {
            error!("Failed to parse into u32");
        }
    }
}

// Display a preview of news articles
fn display_news_preview(data: &Value) {
    debug!("Extracting news.");
    let news = data["news"].as_array().expect("News should be available.");

    debug!("Displaying article previews.");
    for (idx, article) in news.iter().enumerate() {
        trace!("Printing Article preview.");
        // Print a formatted preview of each news article
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

// Display the content of a selected news article
fn display_news(data: &Value, choice: usize) {
    debug!("Downloading and displaying news article");

    trace!("Finding URL of the requested article");
    let article_url = data["news"][choice - 1]["details"]
        .as_str()
        .expect("The URL of the article JSON should be available.");

    trace!("Requesting Article JSON");
    // Send a GET request to the article URL and retrieve the response body
    let article_response = reqwest::blocking::get(article_url)
        .expect("The Request should return a Response.")
        .text()
        .expect("The Result should contain text.");

    // Parse the response body of the article as JSON
    let article: Value =
        serde_json::from_str(&article_response).expect("The article data should be in JSON.");

    // Extract and display the content of the article
    let content = article["content"]
        .as_array()
        .expect("Content should be available.");

    debug!("Content: {content:#?}");

    for segment in content {
        if segment["type"] == "text" {
            let text = filter_html_segments(
                segment["value"]
                    .as_str()
                    .expect("The value should be a string."),
            );
            // Print the cleaned text content of the article
            println!("{}", text);
        } else {
            // Print a placeholder for non-text segments
            println!("<NON-TEXT SEGMENT>");
        }
    }
}

// Remove HTML tags from a given string
fn filter_html_segments(source: &str) -> String {
    debug!("Removing HTML Tags.");
    // Regex expression that catches all HTML Tags
    let rx = Regex::new(r"<[^\/<>]+(?:\s[^<>]+)?(?:\s*\/)?>|<\/[^<>]+>")
        .expect("Pre-defined regex expression should be valid");
    let tags: Vec<&str> = rx.find_iter(source).map(|m| m.as_str()).collect();

    // Turn Tags Vector into a hash set to remove duplicate values
    let tags: HashSet<_> = tags.into_iter().collect();

    let mut cleaned: String = String::from(source);
    for tag in tags {
        cleaned = cleaned.replace(tag, "");
    }

    cleaned
}

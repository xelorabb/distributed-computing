use chrono::prelude::{DateTime, Utc};
use std::time::SystemTime;

fn main() {
    let now = SystemTime::now();
    let now: DateTime<Utc> = now.into();
    let timestamp = format!("{}", now.format("%FT%X%.3fZ"));

    println!("{{\"msg\": \"pong\", \"process\": \"rust\", \"created\":\"{}\"}}",timestamp);
}

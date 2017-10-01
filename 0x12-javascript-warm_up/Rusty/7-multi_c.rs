// prints message x times
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	if args.len() > 1 {
		let x = match args[1].parse() {
			Ok(n) => n,
			Err(_) => { println!("Missing number of occurrences"); 0 },
		};
		if x > 0 {
			for i in 0..x {
				println!("Rust is Awesome");
			}
		}
	}
}

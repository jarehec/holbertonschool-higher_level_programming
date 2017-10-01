/* prints 'My number:' and the first arguemnt that can be converted into an int */
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	print!("My number: ");
	if args.len() > 1 {
		match args[1].parse::<usize>() {
			Ok(n) => { println!("{}", args[1]); n },
			Err(_) => { println!(""); 0 },
		};
	}
}

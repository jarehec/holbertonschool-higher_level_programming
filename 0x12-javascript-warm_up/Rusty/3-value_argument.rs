/* prints the first argument passed to it */
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	if args.len() < 2 {
		println!("No argument");
	}
	else {
		println!("{}", args[1]);
	}
}

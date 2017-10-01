/* prints the first argument passed to it */
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	if (env::args().len() - 1) == 0 {
		println!("No argument");
	}
	else {
		println!("{}", args[1]);
	}
}

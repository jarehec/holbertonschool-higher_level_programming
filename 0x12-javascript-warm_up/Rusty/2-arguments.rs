/* prints a message based on the number of arguments */
use std::env;

fn main() {
	let arg_len = env::args().count() - 1;

	if arg_len == 0 {
		println!("No argument");
	}
	else if arg_len == 1 {
		println!("Argument found");
	}
	else if arg_len > 1 {
		println!("Arguments found");
	}
}

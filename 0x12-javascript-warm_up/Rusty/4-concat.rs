/* prints the two arguments passed to it, prints 'arg1 is arg2' */
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	if args.len() > 2 {
		println!("{} is {}", args[1], args[2]);
	}
}

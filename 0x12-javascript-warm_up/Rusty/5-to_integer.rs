/* prints 'My number:' and the first arguemnt can be converted into an int */
use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();

	if args.len() > 1 {
		match args[1].parse::<isize>() {
			Ok(n) => {
				println!("My number: {}", args[1]);
				n
			},
			Err(_) => {
				println!("My number: undefined");
				-1
			},
		};
	}
	else {
		println!("My number: undefined");
	}
}

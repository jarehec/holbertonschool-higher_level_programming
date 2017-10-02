// computes the factorial of x

use std::env;
fn main() {
	let args: Vec<String> = env::args().collect();

	if args.len() > 1 {
		match args[1].parse() {
			Ok(x) => { println!("{}", factorial(x)); x },
			Err(e) => { println!("{}", e); return },
		};
	}
}

fn factorial(x: isize) -> isize {
	if x < 0 {
		return -1;
	}
	if x <= 1 {
		return 1;
	}
	x * factorial(x - 1)
}

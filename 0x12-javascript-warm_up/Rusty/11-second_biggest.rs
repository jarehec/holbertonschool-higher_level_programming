// finds the second biggest int in a list of args

use std::env;
fn main() {
	let mut first = isize::min_value();
	let mut sec = first;

	for i in env::args().skip(1) {
		match i.parse::<isize>() {
			Ok(n) => {
				if n > first {
					sec = first;
					first = n;
				}
				if n > sec && n < first {
					sec = n;
				}
			},
			Err(e) => return println!("{}", e),
		};
	}
	println!("{}", sec);
}

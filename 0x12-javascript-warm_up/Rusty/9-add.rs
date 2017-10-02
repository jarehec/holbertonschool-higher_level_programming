// prints the addition of two integers

use std::env;
fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
        for i in 1..3 {
            match args[i].parse::<isize>() {
                Ok(n) => n,
                Err(e) => { println!("{}", e) ; return },
            };
        }
        add(args[1].parse().unwrap(), args[2].parse().unwrap());
    }
}
fn add(a: isize, b: isize) {
    println!("{}", a + b);
}

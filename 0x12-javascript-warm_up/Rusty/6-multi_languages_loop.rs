/* prints 'lang is desc' */
fn main() {
	let langs = ["C", "Python", "Javascript"];
	let desc = ["fun", "cool", "amazing"];

	for i in 0..langs.len() {
		println!("{} is {}", langs[i], desc[i]);
	}
}

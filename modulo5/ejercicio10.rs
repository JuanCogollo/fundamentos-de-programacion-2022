use std::io;

fn main() {
    let mut width = String::new();
    let mut height = String::new();

    io::stdin()
        .read_line(&mut width)
        .expect("Failed to read line");

    io::stdin()
        .read_line(&mut height)
        .expect("Failed to read line");

    let width: u32 = match width.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Error");
            return;
        }
    };
    let height: u32 = match width.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Error");
            return;
        }
    };

    println!("Widht: {width}, Height: {height}");
}

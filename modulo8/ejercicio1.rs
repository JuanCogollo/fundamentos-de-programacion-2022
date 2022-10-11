use std::io;

fn flag_printer(value: u32) {
    let mut flag = String::from("");

    for k in 0..value {
        for i in 0..value {
            if k == i || (i + k) == value - 1 {
                flag.push_str("#");
            } else {
                flag.push_str("0");
            }
        }

        flag.push_str("\n")
    }

    println!("{}", flag);
}

fn main() {
    loop {
        let mut ld = String::new();
        io::stdin()
            .read_line(&mut ld)
            .expect("Failed to read from stdin");

        let ld: u32 = match ld.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Type a number!");
                continue;
            }
        };

        if ld != 0 {
            flag_printer(ld);
        } else {
            break;
        }
    }
}
